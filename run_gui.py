import ui
import sys
import netease_api
from PyQt5 import QtWidgets, QtGui, QtCore
from functools import partial

class Main(QtWidgets.QWidget):

	def __init__(self):
		super().__init__()
		self.ui = ui.Ui_Form()
		self.ui.setupUi(self)

		self.ui.pushButton_Search.clicked.connect(self.search_clicked)
		self.ui.radioButton_Track.setChecked(True)

		#dialog button
		self.ui.dialog = QtWidgets.QDialogButtonBox(QtCore.Qt.Horizontal)
		self.ui.dialog.resize(120, 80)
		# self.ui.dialog.show()

	def search_clicked(self):
		if (self.ui.radioButton_Track.isChecked()):

			name = self.ui.lineEdit_Search.text()
			result = netease_api.search(name.encode('utf-8'), stype = 1, limit = 100)['songs']
			if (result == 'Search Failed!'):
				print (result + 'Are you connected to the Internet?')
			else:
				temp = []
				try:
					for song, i in zip(result, range(0, 50)):
						song = [
							QtWidgets.QPushButton("猛击下载！", self.ui.tableWidget),
							song['name'],
							song['artists'][0]['name'],
							song['album']['name'],
							song['duration'],
							song['id']]
						# song_temp =
						# print (str(i) + ". {name:<18} {album:<18} {artists:<18}".format(**song))
						# print ("{name}\t\t{album}\t\t{artists}".format(**song))
						temp += [song]
				except e:
					e.print_tb()

				list_length = len(temp)
				# print (list_length)
				# self.sid = []
				self.ui.tableWidget.setRowCount(list_length);
				self.ui.tableWidget.setColumnCount(5);

				# self.ui.tableWidget.setItem(1, 4, QtWidgets.QTableWidgetItem("fuck"))
				for i in range(0, list_length):
					self.ui.tableWidget.setCellWidget(i, 0, temp[i][0])
					temp[i][0].clicked.connect(partial(self.list_button_on_click, song = temp[i]))
					# self.sid += [temp[i][5]]
					for j in range(1, 5):
						self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(temp[i][j]))

				# myButton = QtWidgets.QPushButton("fuck", self.ui.tableWidget)
				# self.ui.tableWidget.setItem(51, 1, QtWidgets.QPushButton("fuck"))
				# print (myButton)
				# self.ui.tableWidget.setCellWidget(50, 1, myButton)
				# netease_api.download(song_id)

		if (self.ui.radioButton_Artist.isChecked()):
			temp = self.ui.lineEdit_Search.text()

			print (temp)
		if (self.ui.radioButton_Album.isChecked()):
			print ("mother!")

	def list_button_on_click(self, song):
		song[0].setText("Downloading")
		# print (sid)
		netease_api.download(song[5])
		song[0].setText("Finished!")

if __name__ == "__main__":
	args = []
	if sys.platform == 'linux' :
		args = ['','-style','Cleanlooks']

	app = QtWidgets.QApplication(args)
	main = Main()
	main.show()
	sys.exit(app.exec_())
