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
	lenPrev = 0
	text = ''

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
		lenPrev = len(self.text)
		self.text = self.lineEdit.text()	
		if lenPrev is 0 and len(self.text) is 1:
			self.com2 = Complete.main()
		elif lenPrev > len(self.text):
			self.com2 = Complete.main()
		#Use Complete_old.py to generate history->suggestions
		newHistory = list(reversed(self.history))
		newHistory += [''] * (3 - len(newHistory))
		com1 = Complete_old.Complete(newHistory)	
		histSuggestions = com1.fin(self.text.lower())
		histSuggestions = ['(' + s + ')' for s in histSuggestions]
		histSuggestions = [n for n in histSuggestions if n != '()']
		#Use Complete.py to generate suggestions->suggestions
		suggSuggestions = self.com2.out(self.text.lower())
		#Add the lists together
		if self.text is '':	
			newHistory = ['(' + s + ')' for s in newHistory]
			newHistory = [n for n in newHistory if n != '()']
			newHistory += [''] * (3 - len(newHistory))	
			suggestions = newHistory[0:3] + [''] * 7	
		else:
			suggestions = histSuggestions + suggSuggestions
			suggestions = [i for i in suggestions if i != '']
			suggestions += [''] * (10-len(suggestions))
			
		#Sets the suggestions
		self.label_1.setText(suggestions[0])
		if suggestions[0] == "":
			self.label_1.setEnabled(False)
		else:
			self.label_1.setEnabled(True)
		self.label_2.setText(suggestions[1])
		if suggestions[1] == "":
			self.label_2.setEnabled(False)
		else:
			self.label_2.setEnabled(True)
		self.label_3.setText(suggestions[2])
		if suggestions[2] == "":
			self.label_3.setEnabled(False)
		else:
			self.label_3.setEnabled(True)
		self.label_4.setText(suggestions[3])	
		if suggestions[3] == "":
			self.label_4.setEnabled(False)
		else:
			self.label_4.setEnabled(True)
		self.label_5.setText(suggestions[4])
		if suggestions[4] == "":
			self.label_5.setEnabled(False)
		else:
			self.label_5.setEnabled(True)
		self.label_6.setText(suggestions[5])
		if suggestions[5] == "":
			self.label_6.setEnabled(False)
		else:
			self.label_6.setEnabled(True)
		self.label_7.setText(suggestions[6])
		if suggestions[6] == "":
			self.label_7.setEnabled(False)
		else:
			self.label_7.setEnabled(True)
		self.label_8.setText(suggestions[7])
		if suggestions[7] == "":
			self.label_8.setEnabled(False)
		else:
			self.label_8.setEnabled(True)
		self.label_9.setText(suggestions[8])	
		if suggestions[8] == "":
			self.label_9.setEnabled(False)
		else:
			self.label_9.setEnabled(True)
		self.label_10.setText(suggestions[9])
		if suggestions[9] == "":
			self.label_10.setEnabled(False)
		else:
			self.label_10.setEnabled(True)
		self.suggestions = suggestions
				
	def suggestionSearch(self, val): # fix here
		historyword = self.suggestions[val]
		if '(' in historyword:
			historyword = historyword.replace('(', '').replace(')', '')
		self.lineEdit.setText(historyword)
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
		text = text.rstrip()
		if text is not '':
			if self.historyindex is 0:
				self.history.insert(self.historyindex, text)
				self.historyindex += 1
			elif text == self.history[self.historyindex - 1]:
				return	
			else:
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
		dispHistory = list(reversed(DictionaryApp.history))
		dispHistory = filter(None, dispHistory)
		histfull = '\n'.join(dispHistory) + '\n'
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
