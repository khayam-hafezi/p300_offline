# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyautogui
import time, threading
import tkinter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets

def foo(window1, freq, redOn):
    redStyle = "background-color: red"
    blueStyle = "background-color: blue"
    if redOn:
        window1.setStyleSheet(redStyle)
    else:
        window1.setStyleSheet(blueStyle)
    redOn = not redOn
    # print(time.ctime())
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
    position = [[(w-wOfWgtTop)/2, 0], [0,(h-hOfWgtLeft)/2],
                [(w-wOfWgtRight), (h-hOfWgtRight)/2], [0, h-hOfClickWgt],
                [(w-wOfClickWgt), (h-hOfClickWgt)]]
    sizeOfButton = [[wOfWgtTop, hOfWgtTop], [wOfWgtLeft, hOfWgtLeft],
                    [wOfWgtRight, hOfWgtRight], [wOfClickWgt, hOfClickWgt], [wOfClickWgt, hOfClickWgt]]
    window = []
    for i in range(0,5):

        window.append(QWidget())
        # layout = QVBoxLayout()
        # layout.addWidget(QPushButton('Top'))
        # layout.addWidget(QPushButton('Bottom'))
        # window.setLayout(layout)
        window[i].setStyleSheet("background-color: red")
        pos = position[i]
        btnSize = sizeOfButton[i]
        window[i].setGeometry(pos[0], pos[1], btnSize[0], btnSize[1])
        window[i].setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        window[i].show()
        foo(window[i], (i+1)/10, True)

    app.exec_()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
