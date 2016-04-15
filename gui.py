from PyQt4 import QtGui #sudo apt-get install python3-pyqt4
from PyQt4.QtCore import SIGNAL
import sys
import gui_designer #Includes all widgets of GUI
import hash

#Designer class with all GUI functions
class DictionaryApp(QtGui.QMainWindow, gui_designer.Ui_MainWindow):
	def __init__(self, parent = None):
		super(DictionaryApp, self).__init__(parent)
		self.setupUi(self)
		self.connect(self.searchBtn, SIGNAL("clicked()"), self.getSearch)
		self.setWindowTitle("ECE368 Dictionary")
		
		self.hashtable = hash.add_words('dict.html')
	
	def getSearch(self):
		text = self.lineEdit.text()
		self.textBrowser.setText("")
		deflist = self.hashtable.lookup(text.lower())
		

		if deflist is []:
			deftext = "Could not find entry!\n"
		else:
			deftext = '\n'.join(deflist)
			deffull = text.title() + '\n\n' + deftext
		
		self.textBrowser.setText(deffull)
		self.lineEdit.setText("")



def main():
	app = QtGui.QApplication(sys.argv)
	form = DictionaryApp()
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()
