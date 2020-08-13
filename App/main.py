from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QLineEdit, QLabel


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setUi()

    def setUi(self):
        self.setGeometry(100,100,300,300)
        self.setWindowTitle("Hello")
        
        # Line Edit
        self.line_1 = QLineEdit(self)
        self.line_1.move(100,100)
        self.line_2 = QLineEdit(self)
        self.line_2.move(100,120)

        # Label
        self.label_1 = QLabel("username", self)
        self.label_1.move(20, 100)
        self.label_2 = QLabel("password", self)
        self.label_2.move(20, 120)

        self.button = QPushButton("submit", self)
        self.button.move(100,150)
        self.button.clicked.connect(self.submit)
        self.show()
        
    def submit(self):
        self.username = self.line_1.text()
        self.password = self.line_2.text()
        try:
            import redis
            r = redis.Redis()
            r.set(self.password, self.username)
            r.get(self.password)
            print('successfully :)')
        except ModuleNotFoundError:
            print('you most install redis your system !')


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
    
    