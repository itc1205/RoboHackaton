from PyQt5 import QtSerialPort

class Servo:
    
    def __init__(self, portchar: str, port: QtSerialPort.QSerialPort):
        self.portchar = portchar
        self.port = port

    def change_val(self, val):
        command = ""
        command += str(val + 5)
        command += self.portchar
        self.port.write(command)
    #Send it to the port
    