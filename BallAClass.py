
from PyQt5.QtWidgets import QWidget,QApplication ,QGraphicsScene
from PyQt5.QtCore import QObject, pyqtSignal, QTimer , QRect, Qt ,QRectF ,QPropertyAnimation, QPointF
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
import numpy as np
import math

class BallA(QWidget):

    sigDataChange = pyqtSignal()

    sigEllipse = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.springK = 100
        self.springX = 0.2
        self.positionX = 0.00
        self.positionY = 0.00
        self.goalX = 0.00
        self.goalY = 0.00
        self.positionX_text = 0.00
        self.positionY_text = 0.00
        self.angle = math.pi/4
        self.mass = 0.1
        self.drag = 0
        self.gConst = 9.81
        self.color = "#000000"
        self.speed = 0
        self.visible = False
        self.finish = False
        self.screen = QGraphicsScene()
        self.fps = 60
        self.ratio = 250
        self.ellipseBox = []
        self.u_x = None
        self.u_y = None
        self.time_period = None
        self.time_step = None
        self.v_x = None
        self.v_y = None
        self.speedLst = None
        self.trajectory = None
        self.cur_idx = 0
        self.max_index = None
        self.finish = False

    def calculation(self):
        # compute initial velocity
        try:
            u =  math.sqrt(((self.springK*(self.springX**2))/self.mass) - 2*self.gConst*self.springX*(math.sin(self.angle)+self.drag*math.cos(self.angle)))
        except ValueError:
            u = 0
        self.u_x = u*math.cos(self.angle)
        self.u_y = u*math.sin(self.angle)
        # compute time step
        self.time_period = ((-(-200*self.u_y))+np.sqrt((-200*self.u_y)**2-4*self.gConst*100*200*self.positionY*-1))/(2*self.gConst*100)
        self.time_step = np.arange(0, self.time_period+(1/self.fps), 1/self.fps)
        if len(self.time_step)==0:
            self.time_step.append(self.time_period)
        else:
            self.time_step[-1] = self.time_period
        # compute trajectory
        self.v_x = self.u_x
        self.v_y = self.u_y - self.gConst * self.time_step
        self.speedLst = np.sqrt(self.v_x**2 + self.v_y**2)
        self.trajectory_x = (self.u_x*self.time_step)
        if self.angle<math.pi/2+0.001 and self.angle>math.pi/2-0.001:
            self.trajectory_x[:] = 0
        self.trajectory_x += self.positionX
        self.trajectory_y = (self.u_y*self.time_step-0.5*self.gConst*self.time_step**2) + self.positionY
        self.trajectory = np.column_stack((self.trajectory_x, self.trajectory_y))*self.ratio
        # self.trajectory[:, 0] += self.positionX * self.ratio
        self.trajectory[:, 1] = self.positionY + self.trajectory[:, 1]
        self.cur_idx = 0
        self.max_index = len(self.time_step)-1
        self.speed = self.speedLst[0]
        self.finish = False

    def show(self):
        pen = QPen(QColor(self.color), 5, Qt.SolidLine)
        brush = QBrush(QColor(self.color), Qt.SolidPattern)
        self.sigDataChange.emit()

        if self.cur_idx<self.max_index:
            ellipse = self.screen.addEllipse(self.trajectory[self.cur_idx, 0], -self.trajectory[self.cur_idx, 1], 10, 10, pen, brush)
            self.ellipseBox.append(ellipse)
            self.positionX_text = self.trajectory_x[self.cur_idx]
            self.positionY_text = self.trajectory_y[self.cur_idx]
            self.speed = self.speedLst[self.cur_idx]
            self.cur_idx += 1

        else:
            if not self.finish:
                ellipse = self.screen.addEllipse(self.trajectory[-1, 0], -self.trajectory[-1, 1], 10, 10, pen, brush)
                self.ellipseBox.append(ellipse)
                self.positionX_text = self.trajectory_x[-1]
                self.positionY_text = 0
                self.speed = self.speedLst[self.cur_idx]
                self.finish = True
                self.screen.ellipseAll.append([self.ellipseBox, self])

        for ellipse in self.ellipseBox:
            ellipse.setBrush(brush)
            ellipse.setPen(pen)
            ellipse.setVisible(self.visible)

    def getAttr(self):
        outputText = ''
        for index in range(self.max_index):
            outputText += 'time : {:.2f}, X : {:.2f}, Y : {:.2f}, Speed : {:.2f} '.format(self.time_step[index], self.trajectory_x[index], self.trajectory_y[index], self.speedLst[index])
            outputText += '\n'
        return  outputText

    def reset(self):
        self.ellipseBox.clear()
        self.cur_idx = 0
        self.finish = False
        self.positionX_text = int(self.trajectory_x[self.cur_idx])
        self.positionY_text = int(self.trajectory_y[self.cur_idx])

    def outputText(self):
        outputtext = ''
        outputdict = {
            'Spring constant        ': self.springK,
            'Spring displacement    ': self.springX,
            'Start position(X)      ': self.positionX,
            'Start position(Y)      ': self.positionY,
            'Angle                  ': self.angle,
            'Mass                   ': self.mass,
            'Gravitational Constant ': self.gConst,
            'Color                  ': self.color
            }
        for key in outputdict:
            outputtext += "{} : {}".format(key, outputdict[key])
            outputtext += '\n'
        return outputtext

    # def __repr__(self):
    #     bAttrs = (
    #     "springK", "springX", "positionX", "positionY", "angle", "mass", "drag", "gConst", "color", "speed", "visible",
    #     'fps', 'time_period', 'max_index', 'finish')
    #     bText = ["{:10} : {}".format(at, getattr(self, at))for at in bAttrs]
    #     send = "\n".join(bText) + "\n"
    #     return send



