import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import pandas as pd

class SaveFileDailog(QWidget):

    def __init__(self,data):
        super().__init__()
        self.title = 'Save data'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.data = data
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.saveFileDialog()
        self.show()
    
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);; Excel File (*.xlsx *.xls)", options=options)
        if fileName:
            print(fileName)
        self.data.to_excel(fileName+".xlsx", engine='xlsxwriter')
