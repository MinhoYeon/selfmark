import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("MainWindow.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)


    def btn_clicked (self):
        QMessageBox.about(self, "message", "Clicked")
        for i in range(5):
            self.label = "label_" + str(i)
            self.label = QLabel()
            self.label.setText(str(i))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()