from PyQt5.QtWidgets import *
import json
class dewin(QWidget):
    def __init__(self,obj):
        super().__init__()

        self.mainwindow = obj

        self.v_main = QVBoxLayout()
        self.h_btn_lay = QHBoxLayout()

        self.edit = QLineEdit()
        self.edit.setPlaceholderText("Text to decrypt")

        self.lst = QListWidget()

        self.btn_back = QPushButton("Back")
        self.btn_back.clicked.connect(self.back)
        self.btn_ok = QPushButton("Ok")
        self.btn_ok.clicked.connect(self.ok)
        self.h_btn_lay.addWidget(self.btn_back)
        self.h_btn_lay.addWidget(self.btn_ok)
        
        self.v_main.addWidget(self.edit)
        self.v_main.addWidget(self.lst)
        self.v_main.addLayout(self.h_btn_lay)
        self.setLayout(self.v_main)

    def back(self):
        self.hide()
        self.mainwindow.show()    

    def ok(self):
        self.lst.clear()
        f = open("data.json")
        data = json.load(f)
        matn = self.edit.text()
        natija = str()

        for i in matn:
            for key, value in data.items():
                if value == i:
                    natija += key
        self.lst.addItem(natija)            