from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from mainWindowUi import Ui_Dialog

from control import Servo

class MainWindow(Ui_Dialog, QDialog):
    
    def __init__(self, port) -> None:
        super().__init__()
        self.port = port
        self.setupUI()

        self.servo_a = Servo("a", port)
        self.servo_b = Servo("b", port)
        self.servo_c = Servo("c", port)
        self.servo_d = Servo("d", port)
        self.servo_e = Servo("e", port)
        self.servo_f = Servo("f", port)



    def setupUI(self):
        super().setupUi(self)

    
