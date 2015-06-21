import ui
import sys
from PyQt5 import QtWidgets, QtGui

class Main(QtWidgets.QWidget):

	def __init__(self):
		super().__init__()
		self.ui = ui.Ui_Form()
		self.ui.setupUi(self)



app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
sys.exit(app.exec_())
