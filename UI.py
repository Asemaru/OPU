
from PyQt6 import QtCore, QtGui, QtWidgets
global line1, line2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(843, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.FIO = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.FIO.setGeometry(QtCore.QRect(590, 40, 191, 31))
        self.FIO.setObjectName("FIO")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("GOST type A")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.group = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.group.setGeometry(QtCore.QRect(594, 80, 191, 31))
        self.group.setText("")
        self.group.setObjectName("group")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 80, 91, 31))
        font = QtGui.QFont()
        font.setFamily("GOST type A")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 160, 161, 61))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 843, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ФИО"))
        self.label_2.setText(_translate("MainWindow", "Группа"))
        self.pushButton.setText(_translate("MainWindow", "ok"))
    
    def GetDatafromLineEdit(self):
        self.line1 = str(self.FIO.displayText())
        self.line2 = str(self.group.displayText())
        print(self.line1,' ',self.line2)

    def hello_world():
        print("fdhgdsh")





