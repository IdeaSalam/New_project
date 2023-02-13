
from windows.window import MyWindow
from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication
import sys
if __name__=='__main__':
    app = QApplication(sys.argv)
    win = MyWindow(600,600, "My_project")
    win.show()
    app.exec()