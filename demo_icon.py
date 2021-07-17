import os
from PySide6.QtGui import QIcon


class AppIcon(QIcon):
    base_dir = 'images'

    def __init__(self, name_image):
        super().__init__()

        path: str = os.path.join(self.base_dir, name_image) + '.png'
        self.addFile(path)
