from PyQt5.QtWidgets import *
from text import textwin
from decrypt import dewin
from alphabet import alphabetwin
class mainwin(QWidget):
    def __init__(self):
        super().__init__()

        self.v_main = QVBoxLayout()

        self.btn_text = QPushButton("Text to decrypt")
        self.btn_text.clicked.connect(self.text)
        self.btn_decrypt = QPushButton("Decrypt to Text")
        self.btn_decrypt.clicked.connect(self.decrypt)
        self.btn_alphabet = QPushButton("Alphabet")
        self.btn_alphabet.clicked.connect(self.alphabet)
        self.btn_exit = QPushButton("Exit")
        self.btn_exit.clicked.connect(exit)

        self.v_main.addWidget(self.btn_text)
        self.v_main.addWidget(self.btn_decrypt)
        self.v_main.addWidget(self.btn_alphabet)
        self.v_main.addWidget(self.btn_exit)

        self.setLayout(self.v_main)


    def text(self):
        self.hide()
        self.wint = textwin(self)
        self.wint.show()
    def decrypt(self):
        self.hide()
        self.decwin = dewin(self)
        self.decwin.show()
    def alphabet(self):
        self.hide()
        self.alph = alphabetwin(self)
        self.alph.show()

app = QApplication([])
win = mainwin()
win.show()
app.exec_()


