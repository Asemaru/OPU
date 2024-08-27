#python -m PyQt6.uic.pyuic -x OPU2.ui -o OPU2.py
from ComPortClient import  ComPort
from UI import Ui
from PyQt6 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt

# fi = [1,2,3,4,5,6,7,8,9]
# E = [1,2,3,4,5,6,7,8,9]

def proverka():
      ui.UI.label_10.setText('Статус: Подключен')

def conect():
        client = ComPort()
        client.Connect(ui.COM, ui.boundRate)                          #Connect to STM32
        # if client.Connected():
        #       ui.UI.label_10.setText('Статус: Подключен') 
        Command = '*IDN?'
        client.Query(Command)
    
def DN():
        # fig, ax = plt.subplots()             # Create a figure containing a single Axes.
        # ax.plot(fi, E)  # Plot some data on the Axes.
        # plt.savefig('DN.png')
        # plt.show()
        fig, ax = plt.subplots()             # Create a figure containing a single Axes.
        ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.                         # Show the figure.
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
    ui.UI.Connect.clicked.connect(conect)
    ui.UI.DN.clicked.connect(DN)



    # while Command != 'exit':
    #         Command = input('Input your command ')
    #         Command+=' \n'



    
    sys.exit(app.exec())