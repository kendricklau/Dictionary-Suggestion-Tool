from PyQt4 import QtGui, QtCore #sudo apt-get install python3-pyqt4
from PyQt4.QtGui import QKeyEvent
import sys
import gui_designer #Includes all widgets of GUI
import gui_history_designer #Opens new history window
import Complete_old
import Complete
import hash

#Designer class with all GUI functions
class DictionaryApp(QtGui.QMainWindow, gui_designer.Ui_MainWindow):
	history = []
	historyindex = 0
	
	def __init__(self, parent = None):
		super(DictionaryApp, self).__init__(parent)
		self.setupUi(self)	
		self.searchBtn.clicked.connect(self.getSearch)
		self.pushButton.clicked.connect(self.showHistory)
		self.lineEdit.textChanged.connect(self.suggestionComp)	
		self.window2 = None
		self.setWindowTitle("ECE368 Dictionary")
		self.hashtable = hash.add_words('dict.html')		
		self.suggestions = [""] * 5
		self.label_1 =NewLabel(self.frame)
		self.label_2 =NewLabel(self.frame)
		self.label_3 =NewLabel(self.frame)
		self.label_4 =NewLabel(self.frame)
		self.label_5 =NewLabel(self.frame)
		self.label_6 =NewLabel(self.frame)
		self.label_7 =NewLabel(self.frame)
		self.label_8 =NewLabel(self.frame)
		self.label_9 =NewLabel(self.frame)
		self.label_10 =NewLabel(self.frame)
		QtCore.QObject.connect(self.label_1, QtCore.SIGNAL('clicked()'), lambda foo = 0: self.suggestionSearch(foo))
		QtCore.QObject.connect(self.label_2, QtCore.SIGNAL('clicked()'), lambda foo = 1: self.suggestionSearch(foo))	
		QtCore.QObject.connect(self.label_3, QtCore.SIGNAL('clicked()'), lambda foo = 2: self.suggestionSearch(foo))	
		QtCore.QObject.connect(self.label_4, QtCore.SIGNAL('clicked()'), lambda foo = 3: self.suggestionSearch(foo))	
		QtCore.QObject.connect(self.label_5, QtCore.SIGNAL('clicked()'), lambda foo = 4: self.suggestionSearch(foo))	
		QtCore.QObject.connect(self.label_6, QtCore.SIGNAL('clicked()'), lambda foo = 5: self.suggestionSearch(foo))
		QtCore.QObject.connect(self.label_7, QtCore.SIGNAL('clicked()'), lambda foo = 6: self.suggestionSearch(foo))	
		QtCore.QObject.connect(self.label_8, QtCore.SIGNAL('clicked()'), lambda foo = 7: self.suggestionSearch(foo))	
		QtCore.QObject.connect(self.label_9, QtCore.SIGNAL('clicked()'), lambda foo = 8: self.suggestionSearch(foo))	
		QtCore.QObject.connect(self.label_10, QtCore.SIGNAL('clicked()'), lambda foo = 9: self.suggestionSearch(foo))	
		self.gridLayout.addWidget(self.label_5, 0, 5, 1, 1)
		self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
		self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
		self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
		self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
		self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
		self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)
		self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)
		self.gridLayout.addWidget(self.label_9, 1, 3, 1, 1)
		self.gridLayout.addWidget(self.label_10, 1, 5, 1, 1)
		
	def suggestionComp(self, event):
		text = self.lineEdit.text()
		com = Complete.main()
		suggestions = com.out(text)
		self.label_1.setText(suggestions[0])
		self.label_2.setText(suggestions[1])
		self.label_3.setText(suggestions[2])
		self.label_4.setText(suggestions[3])	
		self.label_5.setText(suggestions[4])
		self.label_6.setText(suggestions[5])
		self.label_7.setText(suggestions[6])
		self.label_8.setText(suggestions[7])
		self.label_9.setText(suggestions[8])	
		self.label_10.setText(suggestions[9])
		self.suggestions = suggestions
				
	def suggestionSearch(self, val):
		self.lineEdit.setText(self.suggestions[val])
		self.getSearch()

	def showHistory(self):
		if self.window2 is None:
			self.window2 = HistoryApp()
		self.window2.show()

	def getSearch(self):	
		text = self.lineEdit.text()
		self.storeHistory(text)
		self.textBrowser.setText("")
		deflist = self.hashtable.lookup(text.lower())
		
		if len(deflist) == 0:
			deffull = "Could not find entry!\n"
		else:
			deftext = '\n\n'.join(deflist)
			deffull = text.title() + '\n\n' + deftext
		
		self.window2 = None	
		self.textBrowser.setText(deffull)
	
	def storeHistory(self, text):
		if text is not '':
			if self.historyindex is 0:
				self.history.insert(self.historyindex, text)
				self.historyindex += 1
			elif text is self.history[self.historyindex - 1]:
				print("here1")
			else:
				print(self.history[self.historyindex - 1])
				print(text)
				self.history.insert(self.historyindex, text)
				self.historyindex += 1	
				
	def keyPressEvent(self, event):			
		if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_Return:
			self.getSearch()

				
class HistoryApp(QtGui.QDialog, gui_history_designer.Ui_Dialog):

	def __init__(self, parent = None):
		super(HistoryApp, self).__init__(parent)
		self.setupUi(self)
		self.setWindowTitle("Search History")
		self.displayHistory()
		self.pushButton.clicked.connect(self.close)	

	def displayHistory(self):
		histfull = '\n'.join(DictionaryApp.history) + '\n'
		self.textBrowser.setText(histfull)

class NewLabel(QtGui.QLabel):
	def __init__(self, parent = None):
		QtGui.QLabel.__init__(self, parent)
		
	def mouseReleaseEvent(self, event):
		self.emit(QtCore.SIGNAL('clicked()'))
def main():
	app = QtGui.QApplication(sys.argv)
	form = DictionaryApp() 
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()
