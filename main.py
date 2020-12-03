# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyautogui
import time, threading
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import socket
import pyautogui
import struct
from threading import Thread

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

threadList = []



class BlinkButton(QWidget):
    def __init__(self, rect_w, freq):
        super(BlinkButton, self).__init__()
        self.timer = QTimer(self)
        self.white = "white"
        self.black = "black"
        self.currentColor = self.white
        self.styleSheet = "background-color: {}"
        self.setGeometry(rect_w)
        self.freq = freq

    def start_show(self):
        self.currentColor = self.white
        self.setStyleSheet(self.styleSheet.format(self.currentColor))
        self.show()
        self.timer.timeout.connect(self.blink)
        print(round((1.0/self.freq)*1000))
        self.timer.start(round((1.0/self.freq)*1000))

    @pyqtSlot()
    def blink(self):
        if self.currentColor == self.white:
            self.currentColor = self.black
            self.setStyleSheet(self.styleSheet.format(self.currentColor))
        else:
            self.currentColor = self.white
            self.setStyleSheet(self.styleSheet.format(self.currentColor))


def foo():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    continue
                conn.sendall(b"Got IT")
                print("Got it")
                x = struct.unpack('!i', data[:4])[0]
                y = struct.unpack('!i', data[4:8])[0]
                #pyautogui.moveRel(x, y)  # move mouse 10 pixels down
                pyautogui.moveTo(x, y)  # move mouse 10 pixels down


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.window = []
        self.setWindowTitle("p300 App")
        layout = QGridLayout()

        nameLabel = QLabel("ON (ms)")
        nameLineEdit = QSpinBox()
        nameLabel.setBuddy(nameLineEdit)

        emailLabel = QLabel("OFF (ms)")
        emailLineEdit = QSpinBox()
        emailLabel.setBuddy(emailLineEdit)

        ageLabel = QLabel("Trails per Run:")
        ageSpinBox = QSpinBox()
        ageLabel.setBuddy(ageSpinBox);

        numBlocksLabel = QLabel("Blocks:")
        numBlocksSpinBox = QSpinBox()
        numBlocksLabel.setBuddy(numBlocksSpinBox);

        layout.addWidget(nameLabel, 0, 0);
        layout.addWidget(nameLineEdit, 0, 1);
        layout.addWidget(emailLabel, 1, 0);
        layout.addWidget(emailLineEdit, 1, 1);
        layout.addWidget(ageLabel, 2, 0);
        layout.addWidget(ageSpinBox, 2, 1);
        layout.addWidget(numBlocksLabel, 3, 0);
        layout.addWidget(numBlocksSpinBox, 3, 1);

        self.startButton = QPushButton("Start")
        self.stopButton  = QPushButton("Stop")
        self.startButton.clicked.connect(self.startShow)
        hLayout = QHBoxLayout()
        # hLayout.addSpacerItem(QSpacerItem())
        hLayout.addWidget(self.startButton)
        # hLayout.addSpacerItem()
        hLayout.addWidget(self.stopButton)
        # hLayout.addSpacerItem()

        vLayout = QVBoxLayout()
        vLayout.addLayout(layout)
        vLayout.addSpacing(10)
        vLayout.addLayout(hLayout)

        widget = QWidget()
        widget.setLayout(vLayout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def closeEvent(self, event):
        for i in range(0, len(self.window)):
            self.window[i].close()


    @pyqtSlot()
    def startShow(self):
        screen = qApp.primaryScreen()
        print('Screen: %s' % screen.name())
        size = screen.size()
        w = size.width()
        h = size.height()
        print('Size: %d x %d' % (size.width(), size.height()))
        rect = screen.availableGeometry()
        print('Available: %d x %d' % (rect.width(), rect.height()))
        wOfWgtTop = 250
        hOfWgtTop = 100
        wOfWgtLeft = 100
        hOfWgtLeft = 250
        wOfWgtRight = 100
        hOfWgtRight = 250
        wOfClickWgt = 130
        hOfClickWgt = 130
        position = [[(w - wOfWgtTop) / 2, 0], [0, (h - hOfWgtLeft) / 2],
                    [(w - wOfWgtRight), (h - hOfWgtRight) / 2], [0, h - hOfClickWgt],
                    [(w - wOfClickWgt), (h - hOfClickWgt)]]
        sizeOfButton = [[wOfWgtTop, hOfWgtTop], [wOfWgtLeft, hOfWgtLeft],
                        [wOfWgtRight, hOfWgtRight], [wOfClickWgt, hOfClickWgt], [wOfClickWgt, hOfClickWgt]]
        freqList = [12, 10, 7.5, 6.67, 8.57]
        for i in range(0, 5):
            pos = position[i]
            btnSize = sizeOfButton[i]
            rect = QRect(pos[0], pos[1], btnSize[0], btnSize[1])
            self.window.append(BlinkButton(rect, freqList[i]))
            # layout = QVBoxLayout()
            # layout.addWidget(QPushButton('Top'))
            # layout.addWidget(QPushButton('Bottom'))
            # window.setLayout(layout)
            # window[i].setStyleSheet("background-color: red")

            # window[i].setGeometry(pos[0], pos[1], btnSize[0], btnSize[1])
            self.window[i].setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.window[i].start_show()
            # foo(window[i], (i + 1) / 10, True)




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    app = QApplication([])
    theme = "themes/darkblue.css"
    style = open(theme, 'r')
    style = style.read()
    qApp.setStyleSheet(style)
    main_window = MainWindow()
    main_window.show()
    thread = Thread(target=foo)
    thread.start()
    app.exec_()
    thread.join()
    print("thread finished...exiting")

    """
    screen = app.primaryScreen()
    print('Screen: %s' % screen.name())
    size = screen.size()
    w = size.width()
    h = size.height()
    print('Size: %d x %d' % (size.width(), size.height()))
    rect = screen.availableGeometry()
    print('Available: %d x %d' % (rect.width(), rect.height()))
    wOfWgtTop = 250
    hOfWgtTop = 100
    wOfWgtLeft = 100
    hOfWgtLeft = 250
    wOfWgtRight = 100
    hOfWgtRight = 250
    wOfClickWgt = 130
    hOfClickWgt = 130
    position = [[(w - wOfWgtTop) / 2, 0], [0, (h - hOfWgtLeft) / 2],
                [(w - wOfWgtRight), (h - hOfWgtRight) / 2], [0, h - hOfClickWgt],
                [(w - wOfClickWgt), (h - hOfClickWgt)]]
    sizeOfButton = [[wOfWgtTop, hOfWgtTop], [wOfWgtLeft, hOfWgtLeft],
                    [wOfWgtRight, hOfWgtRight], [wOfClickWgt, hOfClickWgt], [wOfClickWgt, hOfClickWgt]]
    window = []
    freqList = [12, 10, 7.5, 6.67, 8.57]
    for i in range(0, 5):
        pos = position[i]
        btnSize = sizeOfButton[i]
        rect = QRect(pos[0], pos[1], btnSize[0], btnSize[1])
        window.append(BlinkButton(rect, freqList[i]))
        # layout = QVBoxLayout()
        # layout.addWidget(QPushButton('Top'))
        # layout.addWidget(QPushButton('Bottom'))
        # window.setLayout(layout)
        # window[i].setStyleSheet("background-color: red")

        # window[i].setGeometry(pos[0], pos[1], btnSize[0], btnSize[1])
        window[i].setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        window[i].start_show()
        # foo(window[i], (i + 1) / 10, True)

    thread = Thread(target=foo)
    thread.start()
    app.exec_()
    thread.join()
    print("thread finished...exiting")
    """

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
