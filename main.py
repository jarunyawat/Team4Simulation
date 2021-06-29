from MainWindowclass import *
import sys

if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        ui = Team4SIM()
        ui.show()
        sys.exit(app.exec_())