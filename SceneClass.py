from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtCore import QTimer, Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor

class DisplayScreen(QGraphicsScene):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.drawGraph = True
        self.balls = []
        self.rowBucket = []
        self.globalMaxIndex = 0
        self.globalMaxX = 0
        self.globalMaxY = 0
        self.drawBase()
        self.ellipseAll = []

        self.fps = 60
        self.clock = QTimer(self)
        self.clock.setInterval((1/self.fps)*1000)
        self.clock.timeout.connect(self.setAnimationTimeText)
        self.clock.timeout.connect(self.endAnimation)

    def ballUpdate(self):
        self.globalMaxIndex = 0
        self.globalMaxX = 0
        self.globalMaxY = 0
        self.balls.clear()
        for rowObj in self.rowBucket:
            self.balls.append(rowObj.ball)
        for ball in self.balls:
            ball.fps = self.fps
            ball.screen = self
            ball.calculation()
        if len(self.balls) != 0:
            self.globalMaxIndex = max([ball.max_index for ball in self.balls])
            self.globalMaxX = max([max(ball.trajectory[:, 0]) for ball in self.balls])
            self.globalMaxY = max([max(ball.trajectory[:, 1]) for ball in self.balls])

    def playAnimation(self):
        self.ellipseAll.clear()
        self.drawGraph = True
        self.ballUpdate()
        for ball in self.balls:
            ball.reset()
            self.clear()
            self.clock.start()
        self.drawBase()

    def endAnimation(self):
        if all([ball.finish for ball in self.balls]):
            self.window.scrollBar_time.setEnabled(True)
            self.clock.stop()
        self.drawOrigin()

    def resetAnimation(self):
        for ball in self.balls:
            ball.reset()
            ball.ellipseBox.clear()
        self.ellipseAll.clear()
        self.clear()
        self.clock.stop()

    def setAnimationTimeText(self):
        timemax = -999
        ballmax = None
        for ball in self.balls:
            if ball.time_period > timemax:
                timemax = ball.time_period
                ballmax = ball
        self.window.lineEdit_time.setText('{:.2f}'.format(ballmax.time_step[ballmax.cur_idx]))

    def drawBase(self):
        if self.drawGraph:
            self.drawOrigin()
            pen = QPen(QColor(Qt.black), 5, Qt.SolidLine)
            self.addLine(-10, 10, self.globalMaxX, 10, pen)
            self.addLine(-10, 10, -10, -self.globalMaxY, pen)
            self.drawGraph = False
        else:
            pass

    def drawOrigin(self):
        pen = QPen(QColor(Qt.black), 5, Qt.SolidLine)
        brush = QBrush(QColor(Qt.red), Qt.SolidPattern)
        self.addEllipse(-5, -5, 20, 20, pen, brush)



