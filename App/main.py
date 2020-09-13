import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, 
                             QPushButton, QLabel, QLineEdit, QFileDialog)

from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.style_sheet = """

                QWidget {
                        background-color: #222222;
                }

                QLineEdit {
                        background: transparent;
                        color: #708AF2;
                        font-style: italic;
                        font-weight: bold;
                        border-radius: 5px;
                        border-bottom: 1px solid #708AF2;  
                }

                QPushButton {
                        background-color: transparent;
                        color: #ffffff;
                        font-style: italic;
                        border-radius: 5px;
                        border-bottom: 1px solid #708AF2;
                        height: 25px;

                } 
                        
                QPushButton:hover {
                            background: #708AF2;
                } 

                    """
        self.setUi()

    def setUi(self):
        
        self.setGeometry(300, 300, 600, 370)
        self.setMaximumSize(600, 370)
        self.setMinimumSize(600, 370)
        self.setStyleSheet(self.style_sheet) 
        self.setWindowFlags(Qt.CustomizeWindowHint)
        
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('background.png'))
        self.image.resize(600, 400)
        self.line_1 = QLineEdit(self)
        self.line_1.resize(170, 25)
        self.line_1.move(220, 130)
        self.line_1.setPlaceholderText('Path')
        self.line_2 = QLineEdit(self)
        self.line_2.resize(170, 25)
        self.line_2.move(220, 160)
        self.line_2.setPlaceholderText('Register')


        self.btn_search = QPushButton('search', self)
        self.btn_search.resize(70, 30)
        self.btn_search.move(232, 200)
        self.btn_search.clicked.connect(lambda : print('OK'))
        
        self.btn_exit = QPushButton('exit', self)
        self.btn_exit.resize(70, 30)
        self.btn_exit.move(310, 200)
        self.btn_exit.clicked.connect(lambda : self.close())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())