from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from mainWindow import MainWindow

import sys

def main():
    serial = QSerialPort()
    serial.setBaudRate(115200)

    ports = QSerialPortInfo().availablePorts()
    portList = [port for port in ports]
    print(ports)
    app = QApplication(sys.argv)
    window = MainWindow(serial)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()