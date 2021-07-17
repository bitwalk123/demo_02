from PySide6.QtWidgets import (
    QDialog,
    QGridLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
from demo_icon import AppIcon


class AboutDlg(QDialog):
    css_label_title: str = "QLabel {font-size:14pt; padding: 2px 2px;}"
    css_label_normal: str = "QLabel {font-size:10pt; padding: 0 2px;}"

    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_ui(parent)
        self.setWindowIcon(AppIcon('info'))
        self.setWindowTitle('About this')
        self.setFixedSize(self.sizeHint())

    def init_ui(self, parent):
        grid = QGridLayout()
        base = QWidget()
        base.setLayout(grid)
        but = QPushButton('OK')
        but.clicked.connect(self.closeEvent)

        layout = QVBoxLayout()
        layout.addWidget(base)
        layout.addWidget(but)
        self.setLayout(layout)
        row: int = 0

        lab_app_name = QLabel(parent.APP_NAME)
        lab_app_name.setStyleSheet(self.css_label_title)
        grid.addWidget(lab_app_name, row, 0, 1, 2)
        row += 1

        lab_app_ver_l = QLabel('VERSION')
        lab_app_ver_l.setStyleSheet(self.css_label_normal)
        lab_app_ver_l.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        lab_app_ver_r = QLabel(parent.APP_VER)
        lab_app_ver_r.setStyleSheet(self.css_label_normal)
        lab_app_ver_r.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        grid.addWidget(lab_app_ver_l, row, 0)
        grid.addWidget(lab_app_ver_r, row, 1)
        row += 1

        lab_app_copyright_l = QLabel('COPYRIGHT')
        lab_app_copyright_l.setStyleSheet(self.css_label_normal)
        lab_app_copyright_r = QLabel(parent.APP_COPYRIGHT)
        lab_app_copyright_r.setStyleSheet(self.css_label_normal)
        grid.addWidget(lab_app_copyright_l, row, 0)
        grid.addWidget(lab_app_copyright_r, row, 1)
        row += 1

        lab_app_license_l = QLabel('LICENSE')
        lab_app_license_l.setStyleSheet(self.css_label_normal)
        lab_app_license_r = QLabel(parent.APP_LICENSE)
        lab_app_license_r.setStyleSheet(self.css_label_normal)
        lab_app_license_r.setOpenExternalLinks(True)
        grid.addWidget(lab_app_license_l, row, 0)
        grid.addWidget(lab_app_license_r, row, 1)
        row += 1

    # Greets the user
    def closeEvent(self, event):
        self.close()
