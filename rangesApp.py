import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5 import QtCore, QtGui, QtWidgets

# Subclass QMainWindow to customise your application's main window
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    ranges_texts = {'EP': ['OPEN', 'vs 3bet', 'vs 3bet', 'vs 3bet', 'vs 3bet', 'vs 3bet'],
            'MP': ['vs OPEN', 'OPEN', 'vs 3bet', 'vs 3bet', 'vs 3bet', 'vs 3bet'],
            'CO': ['vs OPEN', 'vs OPEN', 'OPEN', 'vs 3bet', 'vs 3bet', 'vs 3bet'],
            'BU': ['vs OPEN', 'vs OPEN', 'vs OPEN', 'OPEN', 'vs 3bet', 'vs 3bet'],
            'SB': ['vs OPEN', 'vs OPEN', 'vs OPEN', 'vs OPEN', 'OPEN', 'vs 3bet'],
            'BB': ['vs OPEN', 'vs OPEN', 'vs OPEN', 'vs OPEN', 'vs OPEN', 'OPEN']}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(110, 10,400, 400))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(6)
        self.setData()
        _translate = QtCore.QCoreApplication.translate

    def setData(self):
        horHeaders = []
        for n, key in enumerate(self.ranges_texts.keys()):
            horHeaders.append(key)
            for m, item in enumerate(self.ranges_texts[key]):
                newitem = QTableWidgetItem(item)
                self.tableWidget.setItem(m, n, newitem)
        self.tableWidget.setHorizontalHeaderLabels(horHeaders)
        self.tableWidget.setVerticalHeaderLabels((horHeaders))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "x"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "y"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "z"))
        self.addButton.setText(_translate("MainWindow", "Add Row"))
        self.sumColButton.setText(_translate("MainWindow", "Sum Column"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())