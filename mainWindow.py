from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys

data = {'EP': ['OPEN', 'vs 3bet', 'vs 3bet', 'vs 3bet', 'vs 3bet', 'vs 3bet'],
        'MP': ['vs OPEN', 'OPEN', 'vs 3bet', 'vs 3bet', 'vs 3bet', 'vs 3bet'],
        'CO': ['vs OPEN', 'vs OPEN', 'OPEN', 'vs 3bet', 'vs 3bet', 'vs 3bet'],
        'BU': ['vs OPEN', 'vs OPEN', 'vs OPEN', 'OPEN', 'vs 3bet', 'vs 3bet'],
        'SB': ['vs OPEN', 'vs OPEN', 'vs OPEN', 'vs OPEN', 'OPEN', 'vs 3bet'],
        'BB': ['vs OPEN', 'vs OPEN', 'vs OPEN', 'vs OPEN', 'vs OPEN', 'OPEN']}


class TableView(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.setData()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.cellClicked.connect(self.click_func)

    def setData(self):
        horHeaders = []
        for n, key in enumerate(self.data.keys()):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)
        self.setVerticalHeaderLabels((horHeaders))

    def click_func(self, row, column):
        print(row)

def main(args):
    app = QApplication(args)
    table = TableView(data, 6, 6)
    table.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)