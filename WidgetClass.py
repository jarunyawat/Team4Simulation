from abc import abstractmethod
from PyQt5.QtWidgets import QPushButton, QColorDialog, QCheckBox, QLabel
from PyQt5.QtCore import pyqtSignal , Qt


class ColorBoxA(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText("")
        self.setStyleSheet("background-color: #000000")
        #Signal
        self.clicked.connect(self.colorChange)

    @abstractmethod
    def colorChange(self):
        # Set ColorPlate for choosing Color
        colorPlate = QColorDialog.getColor()
        # Chang Color via choosing Color
        self.setStyleSheet("background-color: {0}".format(colorPlate.name()))
        # print(self.color)

    @property
    def color(self):
        colorText = self.styleSheet().split()[1]
        return colorText

class ColorBoxB(ColorBoxA):

    # Create Signal that Call AddWinclass
    sigShowW = pyqtSignal()

    def __init__(self, rowObject):
        super(ColorBoxB, self).__init__()

        # Signal Path
        self.sigShowW.connect(rowObject.sigShowWindow.emit)

    def colorChange(self):
        # Operate signal
        self.sigShowW.emit()

class CheckBoxB(QCheckBox):

    # Create Signal that Update BallA
    sigUpdateSender = pyqtSignal()

    def __init__(self, rowObject):
        super().__init__()
        self.setStyleSheet("font: 12pt \"Eras Demi ITC\";\n"
                           "background-color: #121824;\n"
                           "color: #85e1d3;\n")

        self.ball = rowObject.ball
        self.ball.sigDataChange.connect(self.textChange)

        self.veloStatus = {"False": "Disable", "True": "Enable"}
        self.setText(self.veloStatus["False"])

        # Self signal
        self.stateChanged.connect(self.checkStatus)

        # Signal Path
        self.sigUpdateSender.connect(rowObject.sigUpdateReceiver.emit)

    def textChange(self):
        if self.isChecked() == True:
            self.setText(self.veloStatus["True"])
        else:
            self.setText(self.veloStatus["False"])

    def checkStatus(self):
        self.textChange()

        # Operate signal
        self.sigUpdateSender.emit()

    @property
    def checkOrNot(self):
        return self.isChecked()


class LableBoxB(QLabel):

    # Create Signal that Update BallA
    sigUpdateSender = pyqtSignal()

    def __init__(self, rowObject):
        super().__init__()
        self.setStyleSheet("font: 12pt \"Eras Demi ITC\";\n"
                                             "background-color: #121824;\n"
                                             "color: #85e1d3;\n")
        self.ball = rowObject.ball
        self.setAlignment(Qt.AlignCenter)
        # Signal Path
        self.sigUpdateSender.connect(rowObject.sigUpdateReceiver.emit)

    @property
    def valueNow(self):
        return self.text()

class VelocityBoxB(LableBoxB):
    def __init__(self, rowObject):
        super().__init__(rowObject)
        self.ball.sigDataChange.connect(self.textChange)
        self.setText(str(self.ball.speed))

    def textChange(self):
        self.setText("{:.2f}".format(self.ball.speed))

class PositonBoxB(LableBoxB):
    def __init__(self, rowObject):
        super().__init__(rowObject)
        self.ball.sigDataChange.connect(self.textChange)

    def textChange(self):
        self.setText("({:.2f},{:.2f})".format(self.ball.positionX_text,abs(self.ball.positionY_text)))

