from PyQt5 import QtWidgets, uic
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

import sys

def main():
    serial = QSerialPort()
    serial.setBaudRate(115200)

    ports = QSerialPortInfo().availablePorts()
    portList = [port for port in ports]
    print(ports)

if __name__ == "__main__":
    main()