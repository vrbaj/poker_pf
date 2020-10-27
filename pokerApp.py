# importing the required libraries

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
import random

import sys
import os


class Window(QMainWindow):
    ranges_texts = {'UTG': ['OPEN', 'vs 3bet', 'vs 3bet', 'vs 3bet', 'vs 3bet', 'vs 3bet'],
            'MP': ['vs Open', 'OPEN', 'vs 3bet', 'vs 3bet', 'vs 3bet', 'vs 3bet'],
            'CO': ['vs Open', 'vs Open', 'OPEN', 'vs 3bet', 'vs 3bet', 'vs 3bet'],
            'BTN': ['vs Open', 'vs Open', 'vs Open', 'OPEN', 'vs 3bet', 'vs 3bet'],
            'SB': ['vs Open', 'vs Open', 'vs Open', 'vs Open', 'OPEN', 'vs 3bet'],
            'BB': ['vs Open', 'vs Open', 'vs Open', 'vs Open', 'vs Open', 'OPEN']}


    def __init__(self):
        super().__init__()

        self.acceptDrops()
        # set the title
        self.setWindowTitle("Poker range helper")
        # setting  the geometry of window
        self.setGeometry(0, 0, 820, 880)

        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 334, 165))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(6)
        self.setData()
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.cellClicked.connect(self.select_range)
        # creating label

        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 175, 700, 700))

        # loading image
        self.pixmap = QPixmap(os.path.join('range_img','or_sb_vs_bb.jpg')).scaled(700,700, QtCore.Qt.KeepAspectRatio,
                                                                                  QtCore.Qt.SmoothTransformation)

        # adding image to label
        self.label.setPixmap(self.pixmap)


        # Optional, resize label to image size
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())

        self.timerLabel = QLabel(self)
        self.timerLabel.setGeometry(QtCore.QRect(650, 10, 40, 50))
        self.timerLabel.setText("RNG")
        self.timerLabel.setFont(QFont("Arial", 16))
        self.timerLabel.setAlignment(QtCore.Qt.AlignCenter)
        # timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.getRandomNumberTimer)
        self.timer.start(10000)
        # show all the widgets
        self.show()

    # create pyqt5 app
    def getRandomNumberTimer(self):
        rndNumber = random.randint(1, 100)
        self.timerLabel.setText(str(rndNumber))
        if rndNumber > 69:
            self.timerLabel.setStyleSheet("background-color: red")
        elif rndNumber < 31:
            self.timerLabel.setStyleSheet("background-color: green")
        else:
            self.timerLabel.setStyleSheet("background-color: yellow")

    def setData(self):
        horHeaders = []
        for n, key in enumerate(self.ranges_texts.keys()):
            horHeaders.append(key)
            for m, item in enumerate(self.ranges_texts[key]):
                newitem = QTableWidgetItem(item)
                self.tableWidget.setItem(m, n, newitem)
        self.tableWidget.setHorizontalHeaderLabels(horHeaders)
        self.tableWidget.setVerticalHeaderLabels((horHeaders))


    def select_range(self, row, column):
        print(row, column)
        range_to_show = ""
        print(self.tableWidget.item(row, column).text())
        player_position = self.tableWidget.horizontalHeaderItem(column).text()
        villain_position = self.tableWidget.verticalHeaderItem(row).text()
        print("player: ", player_position)
        print("villain: ", villain_position)
        if row > column:
            pass
            # vs 3bet
            range_to_show = 'or_' + player_position + '_vs_' + villain_position + '.jpg'
        elif row == column:
            pass
            # open
        elif row < column:
            pass
            # vs open
            range_to_show = player_position + '_vs_' + villain_position + '.jpg'

        print(range_to_show.lower())
        self.pixmap = QPixmap(os.path.join('range_img', range_to_show.lower())).scaled(700, 700,
                                                        QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())
        self.show()

App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())