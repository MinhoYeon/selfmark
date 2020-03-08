import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class1 = uic.loadUiType("main_window.ui")[0]
form_class2 = uic.loadUiType("new_window.ui")[0]

class NewWindow(QMainWindow, form_class2):
    def __init__(self, parent=None):
        super(NewWindow, self).__init__(parent)
        self.setupUi(self)


class MyWindow(QMainWindow, form_class1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_clicked)

    # 버튼이 클릭될 때 새로운 창 생성
    def button_clicked(self):
        self.newWindow = NewWindow(self)
        self.newWindow.show()


app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
