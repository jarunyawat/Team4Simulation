from PyQt5.QtWidgets import QTableWidget
from AddWinClass import *

class RowB(QTableWidget):

    sigShowWindow = pyqtSignal()

    sigrowColorChange = pyqtSignal()

    sigUpdateReceiver = pyqtSignal()

    def __init__(self, table):
        super().__init__()
        self.table = table
        self.firstCreate = True

        self.addWin = AddBallWindow(self)
        self.showWindow()
        self.allowToCreate = self.addWin.allowToCreate

        self.ball = self.addWin.ball

        self.ColorBox = ColorBoxB(self)
        self.PositionBox = PositonBoxB(self)
        self.VelocityBox = VelocityBoxB(self)
        self.CheckBox = CheckBoxB(self)
        self._updataVisible()

        self.sigUpdateReceiver.connect(self._updataVisible)
        self.sigrowColorChange.connect(self._updateColorDisplay)
        self.sigShowWindow.connect(self.showWindow)

        self.addWin.pushButton_ok.clicked.connect(lambda: self.table.createRow(self))

    def _updataVisible(self):
        self.ball.visible = self.CheckBox.checkOrNot

    def _updateColorDisplay(self):
        self.ColorBox.setStyleSheet("background-color: {0}".format(self.addWin.ball.color))

    def showWindow(self):
        self.addWin.show()

class RowBallBucket:
    def __init__(self):
        self.bucket = []

    def putIntoBucket(self, rowObj):
        self.bucket.append(rowObj)

    def putOutofBucket(self, rowObjIndex):
        self.bucket.pop(rowObjIndex)

    @property
    def printAllBall(self):
        if (len(self.bucket)) !=0:
            outputText = ""
            for i,e in enumerate(self.bucket):
                outputText += "Ball number : {}\n".format(i+1)
                outputText += e.ball.outputText()
                outputText += "=============================================\n"
            return outputText
        else:
            return "No Ball in this simulation"

    @property
    def balls(self):
        return [rowObj.ball for rowObj in self.bucket]




