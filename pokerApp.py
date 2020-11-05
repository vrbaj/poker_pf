# importing the required libraries

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from random import randint
from datetime import timedelta

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
        self.seconds_elapsed = 0
        self.session_time = 0
        self.session_running = False
        self.acceptDrops()
        # set the title
        self.setWindowTitle("Poker helper")
        # setting  the geometry of window
        self.setGeometry(0, 0, 820, 880)
        # set the table widget
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 334, 165))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(6)
        self.set_table_texts()
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.cellClicked.connect(self.select_range)
        # creating label_pixmap for pixmap
        self.label_pixmap = QLabel(self)
        self.label_pixmap.setGeometry(QtCore.QRect(10, 175, 700, 700))

        # loading default image
        self.pixmap = QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                           'range_img', 'or_sb_vs_bb.jpg')).scaled(700, 700, QtCore.Qt.KeepAspectRatio,
                                                                                   QtCore.Qt.SmoothTransformation)

        # adding image to label_pixmap
        self.label_pixmap.setPixmap(self.pixmap)
        # Optional, resize label_pixmap to image size
        self.label_pixmap.resize(self.pixmap.width(),
                                 self.pixmap.height())
        # random number
        self.randomRNGLabel = QLabel(self)
        self.randomRNGLabel.setGeometry(QtCore.QRect(380, 22, 200, 50))
        self.randomRNGLabel.setText("Random number:")
        self.randomRNGLabel.setFont(QFont("Arial", 16))
        self.randomRNGLabel.setAlignment(QtCore.Qt.AlignLeft)
        self.randomNumberLabel = QLabel(self)
        self.randomNumberLabel.setGeometry(QtCore.QRect(550, 10, 55, 50))
        self.randomNumberLabel.setText("RNG")
        self.randomNumberLabel.setFont(QFont("Arial", 16))
        self.randomNumberLabel.setAlignment(QtCore.Qt.AlignCenter)
        # session time
        self.sessionLabel = QLabel(self)
        self.sessionLabel.setGeometry(QtCore.QRect(380, 70, 150, 50))
        self.sessionLabel.setText("Session time:")
        self.sessionLabel.setFont(QFont("Arial", 16))
        self.sessionDurationLabel = QLabel(self)
        self.sessionDurationLabel.setGeometry(QtCore.QRect(520, 70, 180, 50))
        self.sessionDurationLabel.setText("00:00:00")
        self.sessionDurationLabel.setFont(QFont("Arial", 16))
        # start/pause session button
        self.sessionButton = QPushButton(self)
        self.sessionButton.setGeometry(QtCore.QRect(380, 120, 120, 36))
        self.sessionButton.setText("Start session")
        self.sessionButton.setFont(QFont("Arial", 12))
        self.sessionButton.clicked.connect(self.session_switch)
        # reset session
        self.resetButton = QPushButton(self)
        self.resetButton.setGeometry(QtCore.QRect(520, 120, 120, 36))
        self.resetButton.setText("Reset time")
        self.resetButton.setFont(QFont("Arial", 12))
        self.resetButton.clicked.connect(self.session_reset)

        # timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timer_action)
        self.timer.start(1000)
        # show all the widgets
        self.show()

    def session_switch(self):
        if not self.session_running:
            self.sessionButton.setText("Pause session")
        else:
            self.sessionButton.setText("Start session")
        self.session_running = not self.session_running

    def session_reset(self):
        self.session_time = -1
        self.sessionDurationLabel.setText("0:00:00")

    # create PyQt5 app
    def timer_action(self):
        self.seconds_elapsed += 1
        if self.seconds_elapsed % 10 == 0:
            rnd_number = randint(1, 100)
            self.randomNumberLabel.setText(str(rnd_number))
            if rnd_number > 69:
                self.randomNumberLabel.setStyleSheet("background-color: red")
            elif rnd_number < 31:
                self.randomNumberLabel.setStyleSheet("background-color: green")
            else:
                self.randomNumberLabel.setStyleSheet("background-color: yellow")
        if self.session_running:
            self.session_time += 1
            self.sessionDurationLabel.setText(str(timedelta(seconds=self.session_time)))



    def set_table_texts(self):
        horizontal_headrs = []
        for n, key in enumerate(self.ranges_texts.keys()):
            horizontal_headrs.append(key)
            for m, item in enumerate(self.ranges_texts[key]):
                new_item = QTableWidgetItem(item)
                self.tableWidget.setItem(m, n, new_item)
        self.tableWidget.setHorizontalHeaderLabels(horizontal_headrs)
        self.tableWidget.setVerticalHeaderLabels(horizontal_headrs)

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
        self.pixmap = QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                           'range_img', range_to_show.lower())).scaled(700, 700,
                                                                                       QtCore.Qt.KeepAspectRatio,
                                                                                       QtCore.Qt.SmoothTransformation)
        self.label_pixmap.setPixmap(self.pixmap)
        self.label_pixmap.resize(self.pixmap.width(),
                                 self.pixmap.height())
        self.show()


App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
