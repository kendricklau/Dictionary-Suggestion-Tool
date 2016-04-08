#!/usr/bin/python3

import sys
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QDialog, QApplication, QPushButton, QLineEdit, QFormLayout
 
class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
 
        self.lineEdit = QLineEdit()
        self.lineEdit.setObjectName("host")
        self.lineEdit.setText("")
		
		

        self.pushButton = QPushButton()
        self.pushButton.setObjectName("btn")
        self.pushButton.setText("Submit") 

		 
        layout = QFormLayout()
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.pushButton)
 
        self.setLayout(layout)
        self.connect(self.pushButton, SIGNAL("clicked()"),self.button_click)
        self.setWindowTitle("ECE368 Dictionary Project")
		

    def button_click(self):
        qstr = self.lineEdit.text()
        print qstr
	self.lineEdit.setText("")
 
 
app = QApplication(sys.argv)
form = Form()
form.resize(500, 300)
form.show()
app.exec_()
