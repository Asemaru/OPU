from PyQt6 import uic
import PyQt6.QtWidgets 

# эта функция срабатывает при нажатии кнопки
def hello_world():
    print(str(fio.text()))

# подключаем файл, полученный в QtDesigner
Form, Window = uic.loadUiType("OPU.ui")
app = PyQt6.QtWidgets.QApplication([])
window, form = Window(), Form()
form.setupUi(window)
window.show()

# настраиваем сценарий для элемента pushButton

fio = PyQt6.QtWidgets.QLineEdit
form.pushButton.clicked.connect(hello_world) #UART 
# запускаем окно программы
app.exec()