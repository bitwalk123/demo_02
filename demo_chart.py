import pandas as pd

from PySide6.QtCore import QPointF
from PySide6.QtGui import QPainter
from PySide6.QtCharts import (
    QChart,
    QChartView,
    QLineSeries
)


class TrendChart(QChartView):
    df: pd.DataFrame = None
    columns: list = []

    def __init__(self, df: pd.DataFrame):
        super().__init__()
        self.df = df
        self.columns = df.columns.values.tolist()

        chart: QChart = self.init_ui()
        self.setChart(chart)
        self.setRenderHint(QPainter.Antialiasing)

    def init_ui(self) -> QChart:
        series = QLineSeries()
        series.append(0, 6)
        series.append(2, 4)
        series.append(3, 8)
        series.append(7, 4)
        series.append(10, 5)
        series.append(QPointF(11, 1))
        series.append(QPointF(13, 3))
        series.append(QPointF(17, 6))
        series.append(QPointF(18, 3))
        series.append(QPointF(20, 2))

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setTitle("Simple line chart example")

        return chart
