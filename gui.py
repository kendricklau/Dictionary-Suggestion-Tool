from PyQt4 import QtGui #sudo apt-get install python3-pyqt4
from PyQt4.QtCore import SIGNAL
import sys
import gui_designer #Includes all widgets of GUI
import gui_history_designer #New Window
import hash

#Designer class with all GUI functions
class DictionaryApp(QtGui.QMainWindow, gui_designer.Ui_MainWindow):
	history = []
	historyindex = 0
		
	def __init__(self, parent = None):
		super(DictionaryApp, self).__init__(parent)
		self.setupUi(self)
		self.connect(self.searchBtn, SIGNAL("clicked()"), self.getSearch)	
		self.pushButton.clicked.connect(self.showHistory)
		self.window2 = None
		self.setWindowTitle("ECE368 Dictionary")
		self.hashtable = hash.add_words('dict.html')
			
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
			deftext = '\n'.join(deflist)
			deffull = text.title() + '\n\n' + deftext
		
		self.window2 = None	
		self.textBrowser.setText(deffull)
	
	def storeHistory(self, text):
		DictionaryApp.history.insert(DictionaryApp.historyindex, text)
		DictionaryApp.historyindex += 1	
		print(DictionaryApp.history)
		
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

def main():
	app = QtGui.QApplication(sys.argv)
	form = DictionaryApp() 
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()
