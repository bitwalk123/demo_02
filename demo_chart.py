import pandas as pd

from PySide6.QtCore import QPointF, Qt
from PySide6.QtTest import QTest
from PySide6.QtGui import (
    QPainter,
    QPixmap,
)
from PySide6.QtCharts import (
    QChart,
    QChartView,
    QLineSeries,
    QValueAxis,
)
from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
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
        for r in range(len(self.df)):
            x = float(self.df.iat[r, 0])
            y = float(self.df.iat[r, 1])
            series.append(QPointF(x, y))

        chart = QChart()
        chart.setTitle(self.columns[1])
        chart.addSeries(series)
        chart.legend().hide()

        axisX = QValueAxis()
        axisX.setTitleText(self.columns[0])
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)

        axisY = QValueAxis()
        axisY.setTitleText(self.columns[1])
        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisY)

        return chart

    # -------------------------------------------------------------------------
    #  getChartPixmap
    #
    #  Reference
    #    https://stackoverflow.com/questions/43046875/qtchart-c-saving-a-chart-which-wasnt-displayed
    # -------------------------------------------------------------------------
    def getChartPixmap(self, width_image: float, height_image: float) -> QPixmap:
        w = QWidget()
        w.resize(width_image, height_image)
        vl = QVBoxLayout()
        w.setLayout(vl)
        vl.addWidget(self)
        w.show()
        # waiting for display could be needed but no need on my Fedora
        # QTest.qWaitForWindowExposed(w, 5000)
        # QTest.qWaitForWindowActive(w, 5000)
        pixmap: QPixmap = w.grab()
        w.hide()

        return pixmap
