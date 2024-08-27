from ComPortClient import  ComPort
from UI import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()                                    #Set UI
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(ui.GetDatafromLineEdit)

    # client = ComPort()
    # client.Connect("COM3", 115200)                          #Connect to STM32
    # Command = ''

    # while Command != 'exit':
    #         Command = input('Input your command ')
    #         Command+=' \n'



    
    sys.exit(app.exec())