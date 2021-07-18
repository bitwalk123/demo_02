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
    QLabel,
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

        self.init_ui()
        self.setChart(self.chart)
        self.setRenderHint(QPainter.Antialiasing)
        self.value_label = QLabel(self)

    def init_ui(self) -> QChart:
        series = QLineSeries()
        for r in range(len(self.df)):
            x = float(self.df.iat[r, 0])
            y = float(self.df.iat[r, 1])
            series.append(QPointF(x, y))

        self.chart = QChart()
        # series.setPointsVisible(True)
        series.hovered.connect(self.show_tool_tip)

        self.chart.setTitle(self.columns[1])
        self.chart.addSeries(series)
        self.chart.legend().hide()

        axisX = QValueAxis()
        axisX.setTitleText(self.columns[0])
        self.chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)

        axisY = QValueAxis()
        axisY.setTitleText(self.columns[1])
        self.chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisY)

    # -------------------------------------------------------------------------
    #  show_tool_tip
    #
    #  Reference
    #    https://stackoverflow.com/questions/58350723/qchart-add-axis-not-show-and-when-hovered-info-not-work-correct
    # -------------------------------------------------------------------------
    def show_tool_tip(self, point: QPointF, state: bool):
        if state:
            pos = self.chart.mapToPosition(point)
            x = pos.x()
            y = pos.y()
            self.value_label.move(int(x), int(y))
            label_str: str = '\n({0}, {1})'.format(str(x), str(y))
            self.value_label.setText(label_str)
            self.value_label.show()
        else:
            self.value_label.hide()

    # -------------------------------------------------------------------------
    #  getChartPixmap
    #
    #  Reference
    #    https://stackoverflow.com/questions/43046875/qtchart-c-saving-a-chart-which-wasnt-displayed
    # -------------------------------------------------------------------------
    def getChartPixmap(self, width_image: int, height_image: int) -> QPixmap:
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
