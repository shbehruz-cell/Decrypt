from PyQt5.QtWidgets import *
import json
class alphabetwin(QWidget):
    def __init__(self,obj):
        super().__init__()
        self.mainwindow = obj
        self.v_main = QVBoxLayout()
        self.lbl = QLabel("   Key                 Value")
        self.lst = QListWidget()
        f = open("data.json")
        data = json.load(f)
        for key ,value in data.items():
            self.lst.addItem(f"   {key}                     {value}")
        self.btn_back = QPushButton("Back")
        self.btn_back.clicked.connect(self.back)

        self.v_main.addWidget(self.lbl)
        self.v_main.addWidget(self.lst)
        self.v_main.addWidget(self.btn_back)
        self.setLayout(self.v_main)


    def back(self):
        self.hide()
        self.mainwindow.show()