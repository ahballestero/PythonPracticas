from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("La misteriosa ventana sin nombre")
        boton = QPushButton("Aprieta aqui!")
        self.setCentralWidget(boton)

        self.setFixedSize(QSize(640, 480))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
