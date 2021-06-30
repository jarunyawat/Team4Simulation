from os import error
import sys , math
import picture.allPic
sys.path.insert(1, 'picture')

from PyQt5.QtWidgets import QMainWindow, QErrorMessage, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from BallAClass import *
from WidgetClass import *


class AddBallWindow(QMainWindow):

    sigAddWindS = pyqtSignal()

    def __init__(self, rowObj):
        super().__init__()
        self.rowObj = rowObj
        self.ball = BallA()
        self.color = self.ball.color
        self.allowToCreate = False
        self.__setupUi()

        # Button
        self.pushButton_cancel.clicked.connect(self.close)

        self.pushButton_ok.clicked.connect(self.okPress)
        self.pushButton_ok.clicked.connect(self.rowObj.sigrowColorChange.emit)

        self.pushButton_choose_endpoint.clicked.connect(self.calSpringK)

        self.pushButton_choose_springX.clicked.connect(self.calEndpoint)

        # Color
        self.pushButton_color.clicked.connect(self.colorChange)

    def __setupUi(self):
        self.setWindowTitle("Add Ball Window")
        self.resize(1039, 574)
        self.setMinimumSize(QtCore.QSize(1039, 574))
        self.setMaximumSize(QtCore.QSize(1039, 574))
        self.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("background-image: url(:/bg/Add_ball_Setting_png.png);")
        self.error_msgChooseEndPoint = QErrorMessage()
        self.error_msgChooseEndPoint.setWindowTitle("Error")
        self.error_msgChooseSpring = QErrorMessage()
        self.error_msgChooseSpring.setWindowTitle("Error")
        self.error_msgChooseEndPoint.setWindowIcon(icon)
        self.error_msgChooseSpring.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_choose_endpoint = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_choose_endpoint.setGeometry(QtCore.QRect(700, 180, 163, 45))
        self.pushButton_choose_endpoint.setText("")
        self.pushButton_choose_endpoint.setObjectName("pushButton_choose_endpoint")
        self.pushButton_choose_springX = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_choose_springX.setGeometry(QtCore.QRect(700, 350, 163, 45))
        self.pushButton_choose_springX.setText("")
        self.pushButton_choose_springX.setObjectName("pushButton_choose_springX")
        self.lineEdit_spring_x = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_spring_x.setGeometry(QtCore.QRect(730, 270, 221, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_spring_x.sizePolicy().hasHeightForWidth())
        self.lineEdit_spring_x.setSizePolicy(sizePolicy)
        self.lineEdit_spring_x.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_spring_x.setStyleSheet("font: 18pt \"Eras Demi ITC\";\n"
                                             "background:transparent;\n"
                                             "color: rgb(255, 0, 0);\n"
                                             "border-style: outset;\n"
                                             "border-width: 2px;\n"
                                             "border-color: rgb(255, 0, 0);\n"
                                             "border-radius: 10px;\n"
                                             "padding: 6px;")
        self.lineEdit_spring_x.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_spring_x.setObjectName("lineEdit_spring_x")
        self.lineEdit_endpoint_y = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_endpoint_y.setGeometry(QtCore.QRect(820, 100, 121, 41))
        self.lineEdit_endpoint_y.setStyleSheet("font: 18pt \"Eras Demi ITC\";\n"
                                               "background:transparent;\n"
                                               "color: rgb(255, 0, 0);\n"
                                               "border-style: outset;\n"
                                               "border-width: 2px;\n"
                                               "border-color: rgb(255, 0, 0);\n"
                                               "border-radius: 10px;\n"
                                               "padding: 6px;")
        self.lineEdit_endpoint_y.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_endpoint_y.setObjectName("lineEdit_endpoint_y")
        self.lineEdit_endpoint_x = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_endpoint_x.setGeometry(QtCore.QRect(690, 100, 121, 41))
        self.lineEdit_endpoint_x.setStyleSheet("font: 18pt \"Eras Demi ITC\";\n"
                                               "background:transparent;\n"
                                               "color: rgb(255, 0, 0);\n"
                                               "border-style: outset;\n"
                                               "border-width: 2px;\n"
                                               "border-color: rgb(255, 0, 0);\n"
                                               "border-radius: 10px;\n"
                                               "padding: 6px;")
        self.lineEdit_endpoint_x.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_endpoint_x.setObjectName("lineEdit_endpoint_x")
        self.lineEdit_spring_k = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_spring_k.setGeometry(QtCore.QRect(240, 110, 191, 38))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_spring_k.sizePolicy().hasHeightForWidth())
        self.lineEdit_spring_k.setSizePolicy(sizePolicy)
        self.lineEdit_spring_k.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_spring_k.setStyleSheet("font: 18pt \"Eras Demi ITC\";\n"
                                             "background:transparent;\n"
                                             "color: rgb(255, 0, 0);\n"
                                             "border-style: outset;\n"
                                             "border-width: 2px;\n"
                                             "border-color: rgb(255, 0, 0);\n"
                                             "border-radius: 10px;\n"
                                             "padding: 6px;")
        self.lineEdit_spring_k.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_spring_k.setObjectName("lineEdit_spring_k")
        self.lineEdit_origin_x = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_origin_x.setGeometry(QtCore.QRect(240, 180, 92, 38))
        self.lineEdit_origin_x.setStyleSheet("font: 18pt \"Eras Demi ITC\";\n"
                                             "background:transparent;\n"
                                             "color: rgb(255, 0, 0);\n"
                                             "border-style: outset;\n"
                                             "border-width: 2px;\n"
                                             "border-color: rgb(255, 0, 0);\n"
                                             "border-radius: 10px;\n"
                                             "padding: 6px;")
        self.lineEdit_origin_x.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_origin_x.setObjectName("lineEdit_origin_x")
        self.lineEdit_origin_y = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_origin_y.setGeometry(QtCore.QRect(340, 180, 91, 38))
        self.lineEdit_origin_y.setStyleSheet("font: 18pt \"Eras Demi ITC\";\n"
                                             "background:transparent;\n"
                                             "color: rgb(255, 0, 0);\n"
                                             "border-style: outset;\n"
                                             "border-width: 2px;\n"
                                             "border-color: rgb(255, 0, 0);\n"
                                             "border-radius: 10px;\n"
                                             "padding: 6px;")
        self.lineEdit_origin_y.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_origin_y.setObjectName("lineEdit_origin_y")
        self.lineEdit_angle = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_angle.setGeometry(QtCore.QRect(240, 250, 191, 38))
        self.lineEdit_angle.setStyleSheet("font: 18pt \"Eras Demi ITC\";\n"
                                          "background:transparent;\n"
                                          "color: rgb(255, 0, 0);\n"
                                          "border-style: outset;\n"
                                          "border-width: 2px;\n"
                                          "border-color: rgb(255, 0, 0);\n"
                                          "border-radius: 10px;\n"
                                          "padding: 6px;")
        self.lineEdit_angle.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_angle.setObjectName("lineEdit_angle")
        self.lineEdit_mass = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_mass.setGeometry(QtCore.QRect(240, 320, 191, 38))
        self.lineEdit_mass.setStyleSheet("font: 18pt \"Eras Demi ITC\";\n"
                                         "background:transparent;\n"
                                         "color: rgb(255, 0, 0);\n"
                                         "border-style: outset;\n"
                                         "border-width: 2px;\n"
                                         "border-color: rgb(255, 0, 0);\n"
                                         "border-radius: 10px;\n"
                                         "padding: 6px;")
        self.lineEdit_mass.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_mass.setObjectName("lineEdit_mass")
        self.lineEdit_g = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_g.setGeometry(QtCore.QRect(240, 390, 191, 38))
        self.lineEdit_g.setStyleSheet("font: 18pt \"Eras Demi ITC\";\n"
                                      "background:transparent;\n"
                                      "color: rgb(255, 0, 0);\n"
                                      "border-style: outset;\n"
                                      "border-width: 2px;\n"
                                      "border-color: rgb(255, 0, 0);\n"
                                      "border-radius: 10px;\n"
                                      "padding: 6px;")
        self.lineEdit_g.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_g.setObjectName("lineEdit_g")
        self.pushButton_color = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_color.setGeometry(QtCore.QRect(240, 450, 191, 40))
        self.pushButton_color.setStyleSheet("font: 18pt \"Eras Demi ITC\";\n"
                                            "background:transparent;\n"
                                            "background-color: rgb(255, 255, 255);\n"
                                            "border-style: outset;\n"
                                            "border-width: 5px;\n"
                                            "border-color: rgb(255, 0, 0);\n"
                                            "border-radius: 10px;\n"
                                            "padding: 6px;")
        self.pushButton_color.setText("")
        self.pushButton_color.setObjectName("pushButton_color")
        self.pushButton_ok = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ok.setGeometry(QtCore.QRect(610, 450, 163, 43))
        self.pushButton_ok.setText("")
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.pushButton_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancel.setGeometry(QtCore.QRect(800, 450, 163, 43))
        self.pushButton_cancel.setText("")
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1039, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.__resetDefaultUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def __resetDefaultUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit_spring_x.setText(_translate("AddBallWindow", "0.00"))
        self.lineEdit_endpoint_y.setText(_translate("AddBallWindow", "0.00"))
        self.lineEdit_endpoint_x.setText(_translate("AddBallWindow", "0.00"))
        self.lineEdit_spring_k.setText(_translate("AddBallWindow", "0.00"))
        self.lineEdit_origin_x.setText(_translate("AddBallWindow", "0.00"))
        self.lineEdit_origin_y.setText(_translate("AddBallWindow", "0"))
        self.lineEdit_angle.setText(_translate("AddBallWindow", "45"))
        self.lineEdit_mass.setText(_translate("AddBallWindow", "0.5"))
        self.lineEdit_g.setText(_translate("AddBallWindow", "9.81"))
        self.pushButton_ok.setText("Ok")
        self.pushButton_cancel.setText("Cancel")
        self.pushButton_choose_springX.setText("Choose")
        self.pushButton_choose_endpoint.setText("Choose")
        self.pushButton_choose_endpoint.setStyleSheet("QPushButton{\n"
                                         "font: 18pt \"Eras Demi ITC\";\n"
                                         "background:transparent;\n"
                                         "background-color: #121824;\n"
                                         "color: #85e1d3;\n"
                                         "border-style: outset;\n"
                                         "border-width: 5px;\n"
                                         "border-radius: 10px;\n"
                                         "border-color: rgb(255, 0, 0);\n"
                                         "font: bold 18px;\n"
                                         "padding: 6px;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "background-color: #192730;\n"   
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "background-color: #121824;\n"       
                                         "}")
        self.pushButton_choose_springX.setStyleSheet("QPushButton{\n"
                                         "font: 18pt \"Eras Demi ITC\";\n"
                                         "background:transparent;\n"
                                         "background-color: #121824;\n"
                                         "color: #85e1d3;\n"
                                         "    border-style: outset;\n"
                                         "    border-width: 5px;\n"
                                         "    border-radius: 10px;\n"
                                         "    border-color: rgb(255, 0, 0);\n"
                                         "    font: bold 18px;\n"
                                         "    padding: 6px;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "background-color: #192730;\n"   
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "background-color: #121824;\n"       
                                         "}")
        self.pushButton_ok.setStyleSheet("QPushButton{\n"
                                         "font: 18pt \"Eras Demi ITC\";\n"
                                         "background:transparent;\n"
                                         "background-color: #121824;\n"
                                         "color: #85e1d3;\n"
                                         "    border-style: outset;\n"
                                         "    border-width: 5px;\n"
                                         "    border-radius: 10px;\n"
                                         "    border-color: rgb(255, 0, 0);\n"
                                         "    font: bold 18px;\n"
                                         "    padding: 6px;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "background-color: #192730;\n"   
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "background-color: #121824;\n"       
                                         "}")
        self.pushButton_cancel.setStyleSheet("QPushButton{\n"
                                         "font: 18pt \"Eras Demi ITC\";\n"
                                         "background:transparent;\n"
                                         "background-color: #121824;\n"
                                         "color: #85e1d3;\n"
                                         "border-style: outset;\n"
                                         "border-width: 5px;\n"
                                         "border-radius: 10px;\n"
                                         "border-color: rgb(255, 0, 0);\n"
                                         "font: bold 18px;\n"
                                         "padding: 6px;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "background-color: #192730;\n"   
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "background-color: #121824;\n"       
                                         "}")
        
        self.pushButton_color.setStyleSheet("font: 18pt \"Eras Demi ITC\";\n"
                                            "background:transparent;\n"
                                            "background-color: {0};\n"
                                            "border-style: outset;\n"
                                            "border-width: 2px;\n"
                                            "border-color: rgb(255, 0, 0);\n"
                                            "border-radius: 10px;\n"
                                            "padding: 6px;".format(self.ball.color))
        self.error_msgChooseSpring.setStyleSheet("QErrorMessage{\n"
                                         "background-color: #121824;\n"
                                         "}\n"
                                       "QPushButton{\n"
                                       "font: 18pt \"Eras Demi ITC\";\n"
                                       "background:transparent;\n"
                                       "background-color: #121824;\n"
                                       "color: #85e1d3;\n"
                                       "border-style: solid;\n"
                                       "border-width: 2px;\n"
                                       "border-radius: 10px;\n"
                                       "border-color: rgb(255, 0, 0);\n"
                                       "font: bold 16px;\n"
                                       "padding: 6px;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "background-color: #192730;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed{\n"
                                       "background-color: #121824;\n"
                                       "}"
                                       "QPushButton:disabled{\n"
                                       "border-style: double;\n"
                                       "background-color: #121824;\n"
                                       "color: #ff0000;\n"
                                       "}\n"
                                       "\n"
                                      "QErrorMessage QCheckBox { color: #85e1d3 }"
                                      "QErrorMessage QTextEdit { background-color: #121824; color: #85e1d3 }"
                                       )
        
       self.error_msgChooseEndPoint.setStyleSheet("QErrorMessage{\n"
                                         "background-color: #121824;\n"
                                         "}\n"
                                       "QPushButton{\n"
                                       "font: 18pt \"Eras Demi ITC\";\n"
                                       "background:transparent;\n"
                                       "background-color: #121824;\n"
                                       "color: #85e1d3;\n"
                                       "border-style: solid;\n"
                                       "border-width: 2px;\n"
                                       "border-radius: 10px;\n"
                                       "border-color: rgb(255, 0, 0);\n"
                                       "font: bold 16px;\n"
                                       "padding: 6px;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "background-color: #192730;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed{\n"
                                       "background-color: #121824;\n"
                                       "}"
                                       "QPushButton:disabled{\n"
                                       "border-style: double;\n"
                                       "background-color: #121824;\n"
                                       "color: #ff0000;\n"
                                       "}\n"
                                       "\n"
                                      "QErrorMessage QCheckBox { color: #85e1d3 }"
                                      "QErrorMessage QTextEdit { background-color: #121824; color: #85e1d3 }"
                                       )
    
        self.lineEdit_spring_k.setText(str(self.ball.springK))
        self.lineEdit_spring_x.setText(str(self.ball.springX))
        self.lineEdit_origin_x.setText(str(self.ball.positionX))
        self.lineEdit_origin_y.setText(str(self.ball.positionY))
        self.lineEdit_g.setText(str(self.ball.gConst))
        self.lineEdit_angle.setText(str(self.ball.angle * 180/math.pi))
        self.lineEdit_mass.setText(str(self.ball.mass))

    def colorChange(self):
        # Set ColorPlate for choosing Color
        colorPlate = QtWidgets.QColorDialog.getColor()
        # Chang Color via choosing Color
        self.pushButton_color.setStyleSheet("font: 18pt \"Eras Demi ITC\";\n"
                                            "background:transparent;\n"
                                            "background-color: {0};\n"
                                            "border-style: outset;\n"
                                            "border-width: 2px;\n"
                                            "border-color: rgb(255, 0, 0);\n"
                                            "border-radius: 10px;\n"
                                            "padding: 6px;".format(colorPlate.name()))
        self.color = "background-color: {0}".format(colorPlate.name()).split()[1]

    def passingData(self):

        passkey = True

        checkdigit = {
                 'Spring constant': self.lineEdit_spring_k.text().replace('.', '').isdigit(),
                 'Spring displacement': self.lineEdit_spring_x.text().replace('.', '').isdigit(),
                 'Start position(X)': self.lineEdit_origin_x.text().replace('.', '').isdigit(),
                 'Start position(Y)': self.lineEdit_origin_y.text().replace('.', '').isdigit(),
                 'Angle'   : self.lineEdit_angle.text().replace('.', '').isdigit(),
                 'Mass'    : self.lineEdit_mass.text().replace('.', '').isdigit(),
                 'Gravitational Constant': self.lineEdit_g.text().replace('.', '').isdigit()
                 }

        checkCondition = {
                 'Spring constant': False,
                 'Spring displacement': False,
                 'Start position(X)': False,
                 'Start position(Y)': False,
                 'Angle'   : False,
                 'Mass'    : False,
                 'Gravitational Constant': False
                 }

        for key in checkdigit:
            if checkdigit[key] and key == 'Spring constant':
                checkCondition[key] = True if float(self.lineEdit_spring_k.text()) > 0 else False
            elif checkdigit[key] and key == 'Spring displacement':
                checkCondition[key] = True if float(self.lineEdit_spring_x.text()) >= 0 else False
            elif checkdigit[key] and key == 'Start position(X)':
                checkCondition[key] = True if float(self.lineEdit_origin_x.text()) >= 0 else False
            elif checkdigit[key] and key == 'Start position(Y)':
                checkCondition[key] = True if float(self.lineEdit_origin_y.text()) >= 0 else False
            elif checkdigit[key] and key == 'Angle':
                checkCondition[key] = True if 0 <= float(self.lineEdit_angle.text()) <= 90 else False
            elif checkdigit[key] and key == 'Mass':
                checkCondition[key] = True if float(self.lineEdit_mass.text()) > 0 else False
            elif checkdigit[key] and key == 'Gravitational Constant':
                checkCondition[key] = True if float(self.lineEdit_g.text()) > 0 else False
            else:
                checkCondition[key] = False

        for key in checkdigit:
            if not checkdigit[key]:
                passkey = False
            if not checkCondition[key]:
                passkey = False

        if passkey:

            self.ball.springK = float(self.lineEdit_spring_k.text())
            self.ball.springX = float(self.lineEdit_spring_x.text())
            self.ball.positionX = float(self.lineEdit_origin_x.text())
            self.ball.positionY = float(self.lineEdit_origin_y.text())
            self.ball.positionX_text = float(self.lineEdit_origin_x.text())
            self.ball.positionY_text = float(self.lineEdit_origin_y.text())
            self.ball.angle = float(float(self.lineEdit_angle.text()) * math.pi/180)
            self.ball.mass = float(self.lineEdit_mass.text())
            self.ball.gConst = float(self.lineEdit_g.text())
            self.ball.color = self.color
            self.allowToCreate = True

            # Send Signal to MainWindow
            self.sigAddWindS.emit()

        else:
            self.allowToCreate = False
            errortext = ''
            numError = 0

            for key in checkdigit:
                if not checkdigit[key] or not checkCondition[key]:
                    numError += 1
                if not checkdigit[key]:
                    errortext += ' {} is not a number | '.format(key)
                if not checkdigit[key] and key == 'Spring displacement':
                    self.ball.springX = 0
                    self.ball.goalX = 0
                    self.ball.goalY = 0
                    self.lineEdit_spring_x.setText("0.00")
                    self.lineEdit_endpoint_x.setText("0.00")
                    self.lineEdit_endpoint_y.setText("0.00")
                if not checkCondition[key] and key == 'Spring constant' and checkdigit[key]:
                    errortext += ' Spring constant > 0 | '
                elif not checkCondition[key] and key == 'Spring displacement' and checkdigit[key]:
                    errortext += ' Spring displacement > 0 | '
                elif not checkCondition[key] and key == 'Start position(X)' and checkdigit[key]:
                    errortext += ' Start position(X) > 0 | '
                elif not checkCondition[key] and key == 'Start position(Y)' and checkdigit[key]:
                    errortext += ' Start position(Y) > 0 | '
                elif not checkCondition[key] and key == 'Angle' and checkdigit[key]:
                    errortext += ' Angle must be in quadrant1   |  '
                elif not checkCondition[key] and key == 'Mass' and checkdigit[key]:
                    errortext += ' Mass > 0 | '
                elif not checkCondition[key] and key == 'Gravitational Constant' and checkdigit[key]:
                    errortext += ' Gravitational Constant > 0 | '

            outputText = '| Error found = {} |'.format(numError)
            self.error_msgChooseEndPoint.showMessage(outputText + errortext)

    def okPress(self):
        self.passingData()
        if self.allowToCreate:
            self.close()

    def calSpringK(self):
        try:
            self.passingData()
            self.ball.goalX = float(self.lineEdit_endpoint_x.text())
            self.ball.goalY = float(self.lineEdit_endpoint_y.text())
            if self.ball.goalX-self.ball.positionX<=0:
                self.ball.goalX=self.ball.positionX
                if self.ball.angle>math.pi/2+0.001 or self.ball.angle<math.pi/2-0.001:
                    raise error
                else:
                    self.ball.angle = math.pi/2
                    self.ball.springX = (2 * self.ball.gConst * (math.sin(self.ball.angle) - self.ball.drag * math.cos(self.ball.angle)) + math.sqrt((2 * self.ball.gConst * (math.sin(self.ball.angle) - self.ball.drag * math.cos(self.ball.angle))) ** 2 + (8 * self.ball.springK / self.ball.mass) * ((self.ball.gConst)*(self.ball.goalY - self.ball.positionY)))) / (2 * self.ball.springK / self.ball.mass)
            elif self.ball.angle>math.pi/2+0.001 or self.ball.angle<math.pi/2-0.001:
                self.ball.springX = (2 * self.ball.gConst * (math.sin(self.ball.angle) - self.ball.drag * math.cos(self.ball.angle)) + math.sqrt((2 * self.ball.gConst * (math.sin(self.ball.angle) - self.ball.drag * math.cos(self.ball.angle))) ** 2 + (4 * self.ball.springK / self.ball.mass) * ((self.ball.gConst * ((self.ball.goalX - self.ball.positionX)) ** 2) / ((2 * math.cos(self.ball.angle) ** 2) * (((self.ball.goalX - self.ball.positionX)) * math.tan(self.ball.angle) - ((self.ball.goalY - self.ball.positionY))))))) / (2 * self.ball.springK / self.ball.mass)
            else:
                raise error
            self.lineEdit_spring_x.setText('{:.6f}'.format(self.ball.springX))
        except:
            self.ball.springX = 0
            self.ball.goalX = 0
            self.ball.goalY = 0
            self.lineEdit_spring_x.setText("0.00")
            self.lineEdit_endpoint_x.setText("0.00")
            self.lineEdit_endpoint_y.setText("0.00")
            self.error_msgChooseSpring.showMessage("Cannot shoot | End Position out of safety parabola or not a number")

    def calEndpoint(self):
        try:
            self.passingData()
            self.ball.calculation()
            self.lineEdit_endpoint_x.setText('{:.2f}'.format(self.ball.trajectory_x[self.ball.max_index]))
            self.lineEdit_endpoint_y.setText("0.00")

        except:
            self.ball.springX = 0
            self.ball.goalX = 0
            self.ball.goalY = 0
            self.lineEdit_spring_x.setText("0.00")
            self.lineEdit_endpoint_x.setText("0.00")
            self.lineEdit_endpoint_y.setText("0.00")
            self.error_msgChooseSpring.showMessage("Cannot shoot | Spring Constant > 0 or not a number")
