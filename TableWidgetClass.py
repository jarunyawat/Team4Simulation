
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView , QTableWidget
from RowClass import *

class TableA(QTableWidget):

    sigConfirmCreate = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._setUp()
        self.display = None
        self.rowBallBucket = RowBallBucket()

    def _setUp(self):
        self.setGeometry(QtCore.QRect(10, 740, 1000, 200))
        self.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";"
                           "background-color: #6faed5;\n")
        # self.setStyleSheet(" QTableView {\n"
        #                     "font: 14pt \"MS Shell Dlg 2\";\n"
        #                     "background-color: #6faed5;\n"
        #                     "selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5,\n"
        #                     "stop: 0 #121824, stop: 1 #344568);\n"
        #                     "}\n"
        #                     "\n"
        #                     "QHeaderView::section {\n"
        #                     "font: 14pt \"MS Shell Dlg 2\";\n"
        #                     "background-color: #121824;\n"
        #                     "color: #85e1d3 ;\n"
        #                     "}\n"
        #                     "\n"
        #                     "")
        self.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.setAlternatingRowColors(True)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.setGridStyle(QtCore.Qt.SolidLine)
        self.setRowCount(0)
        self.setColumnCount(4)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.setVerticalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(3, item)
        self.horizontalHeader().setVisible(True)
        self.horizontalHeader().setCascadingSectionResizes(False)
        self.horizontalHeader().setDefaultSectionSize(243)
        self.setSortingEnabled(False)
        item = self.horizontalHeaderItem(0)
        item.setText("Color")
        item = self.horizontalHeaderItem(1)
        item.setText("Position (m)")
        item = self.horizontalHeaderItem(2)
        item.setText("Speed (m/s)")
        item = self.horizontalHeaderItem(3)
        item.setText("Show Vector")
        __sortingEnabled = self.isSortingEnabled()
        self.setSortingEnabled(False)
        self.setSortingEnabled(__sortingEnabled)

    def checkBucket(self):
        return self.rowBallBucket

    def createRowObj(self):
        RowB(self)

    def createRow(self, rowobj):
        if rowobj.firstCreate == True and rowobj.addWin.allowToCreate == True:
            self.display.clock.timeout.connect(rowobj.ball.show)
            self.rowBallBucket.putIntoBucket(rowobj)
            rowobj.firstCreate = False
            rowobj.ball.calculation()
            rowobj.ball.sigDataChange.emit()
            rowCount = self.rowCount()
            self.insertRow(rowCount)
            self.setCellWidget(rowCount, 0, rowobj.ColorBox)
            self.setCellWidget(rowCount, 1, rowobj.PositionBox)
            self.setCellWidget(rowCount, 2, rowobj.VelocityBox)
            self.setCellWidget(rowCount, 3, rowobj.CheckBox)

    def delRow(self):
        if self.rowCount() > 0:
            ball = self.rowBallBucket.bucket[self.rowCount() - 1].ball
            self.display.clock.timeout.disconnect(ball.show)
            self.removeRow(self.rowCount() - 1)
            self.rowBallBucket.putOutofBucket(self.rowCount())
