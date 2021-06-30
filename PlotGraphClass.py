import sys
sys.path.insert(1, 'D:/Team4UI/simulation/picture')
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtGui, QtWidgets

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    
    def __init__(self, parent=None, width=10, height=8, dpi=100): #inch
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class PlotGraphWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(PlotGraphWindow, self).__init__(*args, **kwargs)
        self.sc = MplCanvas(self, width=10, height=8, dpi=100)
        self.sc.axes.set_xlabel("Positon X (m)")
        self.sc.axes.set_ylabel("Positon Y (m)")
        self.sc.axes.set_aspect('equal')
        self.balls = None

    def plotGraph(self):
        for index,ball in enumerate(self.balls):
            self.sc.axes.plot(ball.trajectory_x, ball.trajectory_y, label="Ball number {}".format(index+1), color=ball.color)
        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        self.sc.axes.legend()
        toolbar = NavigationToolbar(self.sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()