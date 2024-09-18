#python -m PyQt6.uic.pyuic -x OPU2.ui -o OPU2.py
from ComPortClient import  ComPort
from UI import Ui
from PyQt6 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt

global DATA

def proverka():
      ui.UI.label_10.setText('Статус: Подключен')

def connect_STM():
        client = ComPort()
        client.Connect(ui.COM, ui.boundRate)                          #Connect to STM32
        ui.UI.label_10.setText('Статус: Подключен')
        # if client.Connected():
        #       ui.UI.label_10.setText('Статус: Подключен') 
        # Command = '*IDN?'
        # DATA = client.Query(Command)
    
def DN():
        fi = [1,2,3,4,5,6,7,8,9]
        E_f = [1,2,3,4,5,6,7,8,9]
        fig, ax = plt.subplots()             # Create a figure containing a single Axes.
        ax.plot(fi, E_f)  # Plot some data on the Axes.   
        ax.set_title(ui.User.FIO + ' ' + ui.User.group)                      # Show the figure.
        plt.savefig('DN.png')
        ui.UI.label_6.setPixmap(QtGui.QPixmap("DN.png"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui(MainWindow)                                    #Set UI
    MainWindow.show()
    ui.UI.savefio.clicked.connect(ui.GetDatafromLineEdit)
    ui.UI.mesuar.clicked.connect(ui.COMInd)
    ui.UI.Connect.clicked.connect(connect_STM)
    ui.UI.DN.clicked.connect(DN)



    # while Command != 'exit':
    #         Command = input('Input your command ')
    #         Command+=' \n'



    
    sys.exit(app.exec())