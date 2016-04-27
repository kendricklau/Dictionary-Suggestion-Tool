# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_designer.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(482, 449)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        #self.label_5 = QtGui.QLabel(self.frame)
        #self.label_5.setObjectName(_fromUtf8("label_5"))
        #self.gridLayout.addWidget(self.label_5, 0, 5, 1, 1)
        #self.label_3 = QtGui.QLabel(self.frame)
        #self.label_3.setObjectName(_fromUtf8("label_3"))
        #self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        #self.label_4 = QtGui.QLabel(self.frame)
        #self.label_4.setObjectName(_fromUtf8("label_4"))
        #self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        #self.label_1 = QtGui.QLabel(self.frame)
        #self.label_1.setObjectName(_fromUtf8("label_1"))
        #self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        #self.label_2 = QtGui.QLabel(self.frame)
        #self.label_2.setObjectName(_fromUtf8("label_2"))
        #self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        #self.label_6 = QtGui.QLabel(self.frame)
        #self.label_6.setObjectName(_fromUtf8("label_6"))
        #self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        #self.label_7 = QtGui.QLabel(self.frame)
        #self.label_7.setObjectName(_fromUtf8("label_7"))
        #self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)
        #self.label_8 = QtGui.QLabel(self.frame)
        #self.label_8.setObjectName(_fromUtf8("label_8"))
        #self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)
        #self.label_9 = QtGui.QLabel(self.frame)
        #self.label_9.setObjectName(_fromUtf8("label_9"))
        #self.gridLayout.addWidget(self.label_9, 1, 3, 1, 1)
        #self.label_10 = QtGui.QLabel(self.frame)
        #self.label_10.setObjectName(_fromUtf8("label_10"))
        #self.gridLayout.addWidget(self.label_10, 1, 5, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.searchBtn = QtGui.QPushButton(self.frame_3)
        self.searchBtn.setObjectName(_fromUtf8("searchBtn"))
        self.horizontalLayout_5.addWidget(self.searchBtn)
        self.pushButton = QtGui.QPushButton(self.frame_3)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.frame_3)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 462, 277))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.textBrowser = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.horizontalLayout_2.addWidget(self.textBrowser)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        #self.label_5.setText(_translate("MainWindow", "-", None))
        #self.label_3.setText(_translate("MainWindow", "-", None))
        #self.label_4.setText(_translate("MainWindow", "-", None))
        #self.label_1.setText(_translate("MainWindow", "-", None))
        #self.label_2.setText(_translate("MainWindow", "-", None))
        #self.label_6.setText(_translate("MainWindow", "-", None))
        #self.label_7.setText(_translate("MainWindow", "-", None))
        #self.label_8.setText(_translate("MainWindow", "-", None))
        #self.label_9.setText(_translate("MainWindow", "-", None))
        #self.label_10.setText(_translate("MainWindow", "-", None))
        self.searchBtn.setText(_translate("MainWindow", "Search", None))
        self.pushButton.setText(_translate("MainWindow", "View History", None))

