import sys
import datetime
import requests
from PyQt5 import QtCore, uic, QtWidgets
 
qtCreatorFile = "your_ui_file_created_with_Qt_Designer.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
	
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)

		# self.label.setText("text0")

		# self.prev_button.clicked.connect(self.GoPrev)
		# self.next_button.clicked.connect(self.GoNext)

	def GoNext(self):
		# self.label.setText("text1")


	def GoPrev(self):
		# self.label.setText("text2")

 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    daynumber = 0
    window = MyApp()
    window.show()
    sys.exit(app.exec_())