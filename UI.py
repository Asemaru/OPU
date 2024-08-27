
from PyQt6 import QtCore, QtGui, QtWidgets
from OPU2 import Ui_MainWindow
from User import User
global line1, line2

class Ui(object):
    def __init__ (self, MainWindow):
        self.UI = Ui_MainWindow()
        self.UI.setupUi(MainWindow)
        self.User = User()
        self.boundRate = 000

    def GetDatafromLineEdit(self):
        self.User.FIO = str(self.UI.FIO.displayText())
        self.User.group = str(self.UI.group.displayText())
        print(self.User.FIO,' ',self.User.group)

    def hello_world():
        print("fdhgdsh")
    
    def COMInd(self):
        self.COM = str(self.UI.comboBox.currentText())
        self.boundRate = int(self.UI.comboBox_2.currentText())

        #отработчик ошибок поставить

        print(self.COM, ' ', self.boundRate)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())