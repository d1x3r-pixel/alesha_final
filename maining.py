# import sys  # sys нужен для передачи argv в QApplication
# from PyQt5 import QtWidgets
# import design
#
#
# class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
#     def __init__(self):
#         # Это здесь нужно для доступа к переменным, методам
#         # и т.д. в файле design.py
#         super().__init__()
#         self.setupUi(self)
#
#
# def on_click():
#     exec(open('main.py').read())
#
#     form.pushButton.clicked.connect(on_click)
#
#
# def maining():
#     app = QtWidgets.QApplication(sys.argv)  # овый экземпляр QApplication
#     window = ExampleApp()  # Создаём объект класса ExampleApp
#     window.show()  # Показываем окно
#     app.exec_()
#
#
#
# if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
#     maining()


    #
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import os
import webbrowser

Form, Window = uic.loadUiType("design.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


def on_click():
    os.system("python app.py")



def github():
    webbrowser.open('https://github.com/d1x3r-pixel/alesha_final', new=2)

form.pushButton.clicked.connect(on_click)

form.commandLinkButton.clicked.connect(github)
# form.pushButton


app.exec_()