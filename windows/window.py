from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit
from PyQt6 import QtCore

class MyWindow(QMainWindow):
    def __init__(self, width=500, height = 500, title = "Qt") -> None:
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(250,250,width,height)
        self.main_btn = QPushButton("button1",self)
        self.main_lbl = QLabel("<b>this is lable</b>",self)
        self.main_btn.setGeometry(width//2,height//2, 100, 45)
        self.main_btn.adjustSize()
        self.main_lbl.setGeometry(width//2,height//2-50, 100, 100)
        self.main_lbl.adjustSize()
        self.main_btn.clicked.connect(self.change_lable_txt)
    def change_lable_txt(self):
        self.main_lbl.setText("<b> Change </b>")