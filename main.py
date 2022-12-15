from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5 import QtCore
from mainWindow import MainWindow

import sys

def main():
    serial = QSerialPort()
    serial.setBaudRate(115200)

    ports = QSerialPortInfo().availablePorts()
    portList = []
    for port in ports:
        portList.append(port.portName())
    print(portList)
    if not serial.isOpen():
        serial.open(QtCore.QIODevice.ReadWrite)
    app = QApplication(sys.argv)
    window = MainWindow(serial, portList)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()