import sys
sys.path.insert(1, 'picture')
import picture.allPic
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from TableWidgetClass import *
from RowClass import *
from SceneClass import *
from PlotGraphClass import *
from savefile import *

class Team4SIM(QMainWindow):

    def __init__(self, *args):
        super(Team4SIM, self).__init__(*args)
        self.__setupUi()
        self.ballTable = TableA()
        self.ballTable.display = self.displayScreen
        self.rowBucket = self.ballTable.rowBallBucket
        self.tableScreen.addWidget(self.ballTable)
        self.timeMaxBall = None
        self.timeMaxBallIndex = None
        self.ellipseAll = []
        self.rows = self.ballTable.rowBallBucket.bucket
        self.displayScreen.rowBucket = self.rows

        self.btn_add.clicked.connect(self.addRow)
        self.btn_del.clicked.connect(self.delRow)
        self.btn_prt.clicked.connect(self.prtBall)
        self.btn_graph.clicked.connect(self.plotGraph)

        self.btn_reset.clicked.connect(self.resetAnimation)
        self.btn_start.clicked.connect(self.startAnimation)
        self.btn_start.clicked.connect(self.setAnimationTimeText)

    def __setupUi(self):
        self.resize(1500, 1000)
        self.setMinimumSize(QtCore.QSize(1500, 1000))
        self.setMaximumSize(QtCore.QSize(1500, 1000))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(self)
        self.msg_prtBall = QMessageBox()
        self.msg_prtBall.setWindowTitle("Ball Indformation")
        self.msg_prtBall.setWindowIcon(icon)
        #Screen
        self.displayScreen = DisplayScreen(self)
        self.tableScreen = QtWidgets.QGraphicsScene()
        #View
        self.displayView = QtWidgets.QGraphicsView(self.displayScreen,self.centralwidget)
        self.displayView.setGeometry(QtCore.QRect(10, 20, 1470, 650))
        self.displayView.setMaximumSize(QtCore.QSize(1470, 650))
        self.displayView.setFocusPolicy(QtCore.Qt.NoFocus)
        self.displayView.setAlignment(QtCore.Qt.AlignLeft|QtCore. Qt.AlignBottom)

        self.tableview = QtWidgets.QGraphicsView(self.tableScreen,self.centralwidget)
        self.tableview.setGeometry(QtCore.QRect(10, 740, 1000, 200))
        self.tableview.setObjectName("tableview")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 670, 601, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_add = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout.addWidget(self.btn_add)
        self.btn_del = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_del.setObjectName("btn_del")
        self.horizontalLayout.addWidget(self.btn_del)
        self.btn_prt = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_prt.setObjectName("btn_edit")
        self.horizontalLayout.addWidget(self.btn_prt)
        self.btn_graph = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_graph.setObjectName("btn_graph")
        self.horizontalLayout.addWidget(self.btn_graph)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(1080, 850, 371, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_start = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout_2.addWidget(self.btn_start)
        self.btn_reset = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_reset.setObjectName("btn_reset")
        self.horizontalLayout_2.addWidget(self.btn_reset)
        self.scrollBar_time = QtWidgets.QScrollBar(self.centralwidget)
        self.scrollBar_time.setGeometry(QtCore.QRect(1090, 770, 341, 41))
        self.scrollBar_time.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.scrollBar_time.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.scrollBar_time.setMaximum(100)
        self.scrollBar_time.setOrientation(QtCore.Qt.Horizontal)
        self.scrollBar_time.setObjectName("ScrollBar_time")
        self.scrollBar_time.setEnabled(False)

        self.lineEdit_time = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_time.setGeometry(QtCore.QRect(1230, 690, 221, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_time.sizePolicy().hasHeightForWidth())
        self.lineEdit_time.setSizePolicy(sizePolicy)
        self.lineEdit_time.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_time.setStyleSheet("font: 18pt \"Yu Gothic UI Semilight\";")
        self.lineEdit_time.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_time.setReadOnly(True)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1500, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.__resetDefaultUi()
        self.scrollBar_time.valueChanged['int'].connect(self.setRowWidgetText)
        self.scrollBar_time.valueChanged['int'].connect(self.rewatchAnimation)
        QtCore.QMetaObject.connectSlotsByName(self)

    def __resetDefaultUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainProgram", "TEAM 4 Simulation program"))
        self.btn_add.setText(_translate("MainProgram", "Add"))
        self.btn_prt.setText(_translate("MainProgram", "PrtBall"))
        self.btn_del.setText(_translate("MainProgram", "Del"))
        self.btn_graph.setText(_translate("MainProgram", "Graph"))
        self.btn_start.setText(_translate("MainProgram", "Start"))
        self.btn_reset.setText(_translate("MainProgram", "Reset"))

        self.setStyleSheet("QMainWindow{\n"
                           "background-image: url(:/bg/MainWinBG.png);\n"
                           "}\n"
                           )
        self.displayView.setStyleSheet("font: 24pt \"Eras Demi ITC\";\n"
                                             "background:transparent;\n"
                                             # "background-image: url(:/bg/Add_ball_Setting_purebackground.png);\n"
                                             # "background-image: url(:/bg/trajectory_window.png);\n"
                                             "background-color: #7fc8f3;\n"
                                             "border-width: 5px;\n"
                                             "border-color: rgb(255, 0, 0);\n"
                                             "border-radius: 10px;\n"
                                             "padding: 6px;")

        self.lineEdit_time.setStyleSheet("font: 24pt \"Eras Demi ITC\";\n"
                                             "background:transparent;\n"
                                             "background-color: #121824;\n"
                                             "color: #85e1d3;\n"
                                             "border-style: solid;\n"
                                             "border-width: 5px;\n"
                                             "border-color: rgb(255, 0, 0);\n"
                                             "border-radius: 10px;\n"
                                             "padding: 6px;")

        self.btn_add.setStyleSheet("QPushButton{\n"
                                         "font: 18pt \"Eras Demi ITC\";\n"
                                         "background:transparent;\n"
                                         "background-color: #121824;\n"
                                         "color: #85e1d3;\n"
                                         "    border-style: solid;\n"
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
                                         "}"
                                         "QPushButton:disabled{\n"
                                         "border-style: double;\n"
                                         "background-color: #121824;\n"
                                         "color: #ff0000;\n"
                                         "}"
                                   )
        self.btn_del.setStyleSheet("QPushButton{\n"
                                         "font: 18pt \"Eras Demi ITC\";\n"
                                         "background:transparent;\n"
                                         "background-color: #121824;\n"
                                         "color: #85e1d3;\n"
                                         "    border-style: solid;\n"
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
                                         "}"
                                         "QPushButton:disabled{\n"
                                         "border-style: double;\n"
                                         "background-color: #121824;\n"
                                         "color: #ff0000;\n"
                                         "}"
                                   )
        self.btn_prt.setStyleSheet("QPushButton{\n"
                                         "font: 18pt \"Eras Demi ITC\";\n"
                                         "background:transparent;\n"
                                         "background-color: #121824;\n"
                                         "color: #85e1d3;\n"
                                         "    border-style: solid;\n"
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
                                         "}"
                                         "QPushButton:disabled{\n"
                                         "border-style: double;\n"
                                         "background-color: #121824;\n"
                                         "color: #ff0000;\n"
                                         "}"
                                   )
        self.btn_graph.setStyleSheet("QPushButton{\n"
                                         "font: 18pt \"Eras Demi ITC\";\n"
                                         "background:transparent;\n"
                                         "background-color: #121824;\n"
                                         "color: #85e1d3;\n"
                                         "    border-style: solid;\n"
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
                                         "}"
                                         "QPushButton:disabled{\n"
                                         "border-style: double;\n"
                                         "background-color: #121824;\n"
                                         "color: #ff0000;\n"
                                         "}"
                                   )

        self.btn_start.setStyleSheet("QPushButton{\n"
                                         "font: 18pt \"Eras Demi ITC\";\n"
                                         "background:transparent;\n"
                                         "background-color: #55ff7f;\n"
                                         "color: #000000;\n"
                                         "    border-style: solid;\n"
                                         "    border-width: 5px;\n"
                                         "    border-radius: 10px;\n"
                                         "    border-color: #00bd5b;\n"
                                         "    font: bold 20px;\n"
                                         "    padding: 6px;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "background-color: #00bd5b;\n"   
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "border-style: ridge;\n"
                                         "background-color: #55ff7f;\n"       
                                         "}"
                                   )

        self.btn_reset.setStyleSheet("QPushButton{\n"
                                         "font: 18pt \"Eras Demi ITC\";\n"
                                         "background:transparent;\n"
                                         "background-color: #ff0000;\n"
                                         "color: #000000;\n"
                                         "    border-style: solid;\n"
                                         "    border-width: 5px;\n"
                                         "    border-radius: 10px;\n"
                                         "    border-color: #aa0000;\n"
                                         "    font: bold 20px;\n"
                                         "    padding: 6px;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "background-color: #aa0000;\n"   
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "border-style: ridge;\n"
                                         "background-color: #ff0000;\n"       
                                         "}"
                                   )


        self.msg_prtBall.setStyleSheet("QMessageBox{\n"
                                         "background-color: #121824;\n"
                                         "}\n"
                                       "QMessageBox QLabel{\n"
                                         "font: 16pt \"Eras Demi ITC\";\n"
                                         "color: #85e1d3;\n"
                                         "background-color: #121824;\n"
                                         "border-style: solid;\n"
                                         "border-width: 2px;\n"
                                         "border-radius: 10px;\n"
                                         "border-color: rgb(255, 0, 0);\n"
                                         "font: bold 16px;\n"
                                         "padding: 6px;\n"
                                         "}\n"
                                       "QPushButton{\n"
                                       "font: 18pt \"Eras Demi ITC\";\n"
                                       "background:transparent;\n"
                                       "background-color: #121824;\n"
                                       "color: #85e1d3;\n"
                                       "border-style: solid;\n"
                                       "border-width: 5px;\n"
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
                                       "}"
                                       "QMessageBox QTextEdit { background-color: #121824; color: #85e1d3 }"
                                       )

    def addRow(self):
        self.ballTable.createRowObj()

    def delRow(self):
        self.ballTable.delRow()

    def prtBall(self):
        headderText = '==================Ball_Information==================\n\n'
        headderText += "All Ball in this simulation : {} ".format(str(len(self.rows)))
        self.msg_prtBall.setText(headderText)
        # infotext = self.ballTable.rowBallBucket.printAllBall
        # self.msg_prtBall.setInformativeText(infotext)
        self.msg_prtBall.setStandardButtons(QMessageBox.Save | QMessageBox.Close)
        self.msg_prtBall.setDefaultButton(QMessageBox.Close)
        detialText = ''
        for i, rowObj in enumerate(self.ballTable.rowBallBucket.bucket):
            detialText += "Ball Number : {} \n".format(i+1)
            detialText += str(rowObj.ball.getAttr())
            detialText += '=============================================\n'
        self.msg_prtBall.setDetailedText(detialText)
        returnValue = self.msg_prtBall.exec_()
        if returnValue == QMessageBox.Save:
            self.csvBall()

    def csvBall(self):
        timemax = -999
        ballmax = None
        data = dict()
        for rowObj in self.ballTable.rowBallBucket.bucket:
            if rowObj.ball.time_period > timemax:
                timemax = rowObj.ball.time_period
                ballmax = rowObj.ball
        data['time'] = ballmax.time_step
        max_len = len(ballmax.time_step)
        for idx,rowObj in enumerate(self.ballTable.rowBallBucket.bucket):
            data['ball {} X pos'.format(idx)] = rowObj.ball.trajectory_x
            data['ball {} Y pos'.format(idx)] = rowObj.ball.trajectory_y
        for key in data:
            if len(data[key])<max_len:
                data[key] = np.hstack((data[key],np.full(max_len-len(data[key]), np.nan)))
        df = pd.DataFrame(data)
        sf = SaveFileDailog(df)

    def plotGraph(self):
        self.plotWindow = PlotGraphWindow()
        balls = []
        for rowObj in self.rows:
            balls.append(rowObj.ball)
        self.plotWindow.balls = balls
        self.plotWindow.plotGraph()

    def startAnimation(self):
        self.displayScreen.playAnimation()
        self.btn_add.setEnabled(False)
        self.btn_del.setEnabled(False)
        for rowObj in self.rows:
            rowObj.ColorBox.setEnabled(False)
            rowObj.CheckBox.setEnabled(False)

    def resetAnimation(self):
        self.displayScreen.resetAnimation()
        self.btn_add.setEnabled(True)
        self.btn_del.setEnabled(True)
        self.scrollBar_time.setEnabled(False)
        self.scrollBar_time.setValue(0)
        for rowObj in self.rows:
            rowObj.PositionBox.setText("({:.2f},{:.2f})".format(rowObj.ball.positionX, abs(rowObj.ball.positionY)))
            rowObj.VelocityBox.setText("{:.2f}".format(0))
            rowObj.ColorBox.setEnabled(True)
            rowObj.CheckBox.setEnabled(True)

    def setAnimationTimeText(self):
        timeMax = 0
        self.scrollBar_time.setValue(0)
        self.timeMaxBall = None
        self.timeMaxBallIndex = 0
        for rowObj in self.rows:
            ball = rowObj.ball
            if ball.time_period > timeMax:
                timeMax = ball.time_period
                self.timeMaxBall = ball
                self.timeMaxBallIndex = ball.max_index
                self.lineEdit_time.setText('{:.2f}'.format(self.timeMaxBall.time_step[self.scrollBar_time.value()]))
                self.scrollBar_time.setMaximum(self.timeMaxBall.max_index)
                self.scrollBar_time.setValue(self.timeMaxBall.max_index)
        self.ellipseAll = self.displayScreen.ellipseAll

    def rewatchAnimation(self):
        curIndex = self.scrollBar_time.value()
        for ellipse in self.ellipseAll:
            for index in range(self.timeMaxBallIndex+1):
                if index <= curIndex and index < len(ellipse[0]) and ellipse[1].visible == True:
                    ellipse[0][index].setVisible(True)
                elif index < len(ellipse[0]) and ellipse[1].visible == True:
                    ellipse[0][index].setVisible(False)
                elif index < len(ellipse[0]) and ellipse[1].visible == False:
                    ellipse[0][index].setVisible(False)

    def setRowWidgetText(self):
        curIndex = self.scrollBar_time.value()
        self.lineEdit_time.setText('{:.2f}'.format(self.timeMaxBall.time_step[curIndex]))
        for rowObj in self.rows:
            if curIndex <= rowObj.ball.max_index:
                rowObj.PositionBox.setText("({:.2f},{:.2f})".format(rowObj.ball.trajectory_x[curIndex], abs(rowObj.ball.trajectory_y[curIndex])))
                rowObj.VelocityBox.setText("{:.2f}".format(rowObj.ball.speedLst[curIndex]))
