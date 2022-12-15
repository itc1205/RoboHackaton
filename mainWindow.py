from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from mainWindowUi import Ui_Dialog

from PyQt5 import QtCore

from control import Servo

class MainWindow(Ui_Dialog, QDialog):
    
    def __init__(self, port, portList) -> None:
        super().__init__()
        self.port = port
        self.setupUI()
        for potr_i in portList:
            self.PortCombobox.addItem("/dev/" + potr_i)
        self.servo_a = Servo("a", port)
        self.servo_b = Servo("b", port)
        self.servo_c = Servo("c", port)
        self.servo_d = Servo("d", port)
        self.servo_e = Servo("e", port)
        self.servo_f = Servo("f", port)

        self.sliders = [
            self.PortsliderA,
            self.PortsliderB,
            self.PortsliderC,
            self.PortsliderD,
            self.PortsliderE,
            self.PortsliderF,
        ]

        self.spinBoxes = [
            self.miauA,
            self.miauB,
            self.miauC,
            self.miauD,
            self.miauE,
            self.miauF,
        ]

        self.servos = [
            self.servo_a,
            self.servo_b,
            self.servo_c,
            self.servo_d,
            self.servo_e,
            self.servo_f,
        ]


        self.PortsliderA.valueChanged.connect(lambda x: self.servoChange(0, True))
        self.PortsliderB.valueChanged.connect(lambda x: self.servoChange(1, True))
        self.PortsliderC.valueChanged.connect(lambda x: self.servoChange(2, True))
        self.PortsliderD.valueChanged.connect(lambda x: self.servoChange(3, True))
        self.PortsliderE.valueChanged.connect(lambda x: self.servoChange(4, True))
        self.PortsliderF.valueChanged.connect(lambda x: self.servoChange(5, True))

        self.miauA.valueChanged.connect(lambda x: self.servoChange(0))
        self.miauB.valueChanged.connect(lambda x: self.servoChange(1))
        self.miauC.valueChanged.connect(lambda x: self.servoChange(2))
        self.miauD.valueChanged.connect(lambda x: self.servoChange(3))
        self.miauE.valueChanged.connect(lambda x: self.servoChange(4))
        self.miauF.valueChanged.connect(lambda x: self.servoChange(5))
        
        self.OPENPORT.clicked.connect(self.openport)
        self.CLOSEPORT.clicked.connect(self.closeport)

        self.Portautomode.clicked.connect(lambda x: self.send("#auto"))
        self.Portstopmode.clicked.connect(lambda x: self.send("#stop"))
        self.Portprogrammingmode.clicked.connect(lambda x: self.send("#com"))


    def setupUI(self):
        super().setupUi(self)


    def servoChange(self, index:int, slider = False):
        value_to_change = 0
        if slider:
            value_to_change = self.sliders[index].value()
        else:
            value_to_change = self.spinBoxes[index].value()

        self.servos[index].change_val(value_to_change)
        self.sliders[index].setValue(value_to_change)
        self.spinBoxes[index].setValue(value_to_change)

    def openport(self):
        if not self.serial.isOpen():
            self.serial.setPortName(self.PortCombobox.currentText())
            self.serial.open(QtCore.QIODevice.ReadWrite)
        else:
            self.serial.close()
            self.serial.setPortName(self.PortCombobox.currentText())
            self.serial.open(QtCore.QIODevice.ReadWrite)

    def send(self, command: str):
        
        self.serial.write(command.encode())
    
    def closeport(self):
        self.serial.close()