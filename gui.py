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
		self.label_1 = NewLabel(self.frame)
		self.label_2 = NewLabel(self.frame)
		self.label_3 = NewLabel(self.frame)
		self.label_4 = NewLabel(self.frame)
		self.label_5 = NewLabel(self.frame)
		self.horizontalLayout_3.addWidget(self.label_1)
		self.horizontalLayout_3.addWidget(self.label_2)
		self.horizontalLayout_3.addWidget(self.label_3)
		self.horizontalLayout_3.addWidget(self.label_4)
		self.horizontalLayout_3.addWidget(self.label_5)
		self.suggestions = [""] * 5
		QtCore.QObject.connect(self.label_1, QtCore.SIGNAL('clicked()'), lambda foo = 0: self.suggestionSearch(foo))
		QtCore.QObject.connect(self.label_2, QtCore.SIGNAL('clicked()'), lambda foo = 1: self.suggestionSearch(foo))	
		QtCore.QObject.connect(self.label_3, QtCore.SIGNAL('clicked()'), lambda foo = 2: self.suggestionSearch(foo))	
		QtCore.QObject.connect(self.label_4, QtCore.SIGNAL('clicked()'), lambda foo = 3: self.suggestionSearch(foo))	
		QtCore.QObject.connect(self.label_5, QtCore.SIGNAL('clicked()'), lambda foo = 4: self.suggestionSearch(foo))	
		
	def suggestionComp(self, event):
		text = self.lineEdit.text()
		suggestions = Complete.main(text)
		self.label_1.setText(suggestions[0])
		self.label_2.setText(suggestions[1])
		self.label_3.setText(suggestions[2])
		self.label_4.setText(suggestions[3])	
		self.label_5.setText(suggestions[4])
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
		DictionaryApp.history.insert(DictionaryApp.historyindex, text)
		DictionaryApp.historyindex += 1	
	
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
