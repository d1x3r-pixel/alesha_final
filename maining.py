
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