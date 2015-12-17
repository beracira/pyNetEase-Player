#! /usr/bin/python3

import ui
import sys
import netease_api
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtWidgets, QtGui, QtCore
from functools import partial

global_sid = 0

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
					for song, i in zip(result, range(0, 100)):
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

				# set header
				self.ui.tableWidget.clearContents();
				self.ui.tableWidget.setRowCount(list_length);
				self.ui.tableWidget.setColumnCount(5);
				item = self.ui.tableWidget.horizontalHeaderItem(0)
				item.setText("Download")
				item = self.ui.tableWidget.horizontalHeaderItem(1)
				item.setText("Track")
				item = self.ui.tableWidget.horizontalHeaderItem(2)
				item.setText("Artist")
				item = self.ui.tableWidget.horizontalHeaderItem(3)
				item.setText("Album")
				item = self.ui.tableWidget.horizontalHeaderItem(4)
				item.setText("Length")



				# self.ui.tableWidget.setItem(1, 4, QtWidgets.QTableWidgetItem("fuck"))
				for i in range(0, list_length):
					self.ui.tableWidget.setCellWidget(i, 0, temp[i][0])
					temp[i][0].clicked.connect(partial(self.song_list_button_on_click, song = temp[i]))
					# self.sid += [temp[i][5]]
					for j in range(1, 5):
						self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(temp[i][j]))

				# myButton = QtWidgets.QPushButton("fuck", self.ui.tableWidget)
				# self.ui.tableWidget.setItem(51, 1, QtWidgets.QPushButton("fuck"))
				# print (myButton)
				# self.ui.tableWidget.setCellWidget(50, 1, myButton)
				# netease_api.download(song_id)

		if (self.ui.radioButton_Artist.isChecked()):
			name = self.ui.lineEdit_Search.text()
			result = netease_api.search(name.encode('utf-8'), stype = 1, limit = 100)['songs']
			if (result == 'Search Failed!'):
				print (result + 'Are you connected to the Internet?')
			else:
				temp = []
				try:
					for song, i in zip(result, range(0, 100)):
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

				# set header
				self.ui.tableWidget.clearContents();
				self.ui.tableWidget.setRowCount(list_length);
				self.ui.tableWidget.setColumnCount(5);
				item = self.ui.tableWidget.horizontalHeaderItem(0)
				item.setText("Download")
				item = self.ui.tableWidget.horizontalHeaderItem(1)
				item.setText("Track")
				item = self.ui.tableWidget.horizontalHeaderItem(2)
				item.setText("Artist")
				item = self.ui.tableWidget.horizontalHeaderItem(3)
				item.setText("Album")
				item = self.ui.tableWidget.horizontalHeaderItem(4)
				item.setText("Length")



				# self.ui.tableWidget.setItem(1, 4, QtWidgets.QTableWidgetItem("fuck"))
				for i in range(0, list_length):
					self.ui.tableWidget.setCellWidget(i, 0, temp[i][0])
					temp[i][0].clicked.connect(partial(self.song_list_button_on_click, song = temp[i]))
					# self.sid += [temp[i][5]]
					for j in range(1, 5):
						self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(temp[i][j]))


		if (self.ui.radioButton_Album.isChecked()):
			name = self.ui.lineEdit_Search.text()
			result = netease_api.search(name.encode('utf-8'), stype = 10, limit = 100)['albums']
			if (result == 'Search Failed!'):
				print (result + 'Are you connected to the Internet?')
			else:
				temp = []
				# print ("   {:<24} {:<24} {:>6}".format("Name","Artists","Size"))
				try:
					for (album, i) in zip(result, range(0, 100)):
						album = [
							QtWidgets.QPushButton("猛击下载！", self.ui.tableWidget),
							album['name'],
							album['artist']['name'],
							str(album['size']),
							album['id']]
						# print (str(i) + ". {name:<24} {artist:<24} {size:>6}".format(**album))
						temp += [album]
				except e:
					e.print_tb()

				item = self.ui.tableWidget.horizontalHeaderItem(0)
				item.setText("Download")
				item = self.ui.tableWidget.horizontalHeaderItem(1)
				item.setText("Album")
				item = self.ui.tableWidget.horizontalHeaderItem(2)
				item.setText("Artist")
				item = self.ui.tableWidget.horizontalHeaderItem(3)
				item.setText("Size")
				# item = self.ui.tableWidget.horizontalHeaderItem(4)
				# item.setText(_translate("Form", "Length"))

				list_length = len(temp)
				self.ui.tableWidget.clearContents();
				self.ui.tableWidget.setRowCount(list_length);
				self.ui.tableWidget.setColumnCount(4);

				for i in range(0, list_length):
					self.ui.tableWidget.setCellWidget(i, 0, temp[i][0])
					temp[i][0].clicked.connect(partial(self.album_song_list_button_on_click, album = temp[i]))
					print (temp[i][3])
					for j in range(1, 4):
						self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(temp[i][j]))


	def song_list_button_on_click(self, song):
		# song[0].setText("Downloading")
		# print (sid)
		song[0].setText("Downloading")
		self.workThread = WorkThread()
		self.workThread.downloadSingle.connect(netease_api.download)
		self.workThread.take(song[0], song[5])
	
		self.workThread.start()

		# netease_api.download(song[5])
		# song[0].setText("Finished!")

	def album_song_list_button_on_click(self, album):
		album[0].setText("Downloading")
		netease_api.download_by_album(album[4], album[0])
		album[0].setText("Finished")

class WorkThread(QtCore.QThread):
	#define signal here
	downloadSingle = pyqtSignal(int, object)
	downloadAlbum = pyqtSignal()

	def __init__(self):
		QtCore.QThread.__init__(self)

	def take(self, button, sid):
		self.button = button
		self.sid = sid

	def run(self):
		print (self.sid)
		# self.downloadSingle.emit(self.sid, self.button)
		netease_api.download(self.sid, self.button)
		return


if __name__ == "__main__":
	args = []
	if sys.platform == 'linux' :
		args = ['','-style','Cleanlooks']

	app = QtWidgets.QApplication(args)
	main = Main()
	# mainThread = MainThread()
	# mainThread.start()
	main.show()
	sys.exit(app.exec_())
