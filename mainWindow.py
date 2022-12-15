from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from mainWindowUi import Ui_Dialog

class MainWindow(Ui_Dialog, QDialog):
    
    def __init__(self) -> None:
        super().__init__()
        self.setupUI()


    def setupUI(self):
        super().setupUi(self)

    
