# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyautogui
import time, threading
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


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


def foo(window1, freq, redOn):

    threading.Timer(freq, foo, args=(window1, freq, redOn)).start()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    # parent_widget = tkinter.Tk()
    # canvas_widget = tkinter.Canvas(parent_widget,
    # bg = "blue",
    # width = 100,
    # height = 50)
    # canvas_widget.pack()
    # tkinter.mainloop()
    pyautogui.moveRel(10, 10)  # move mouse 10 pixels down

    app = QApplication([])
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

    app.exec_()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
