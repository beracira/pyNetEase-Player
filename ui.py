# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(844, 570)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_Top = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Top.setObjectName("horizontalLayout_Top")
        self.widget_Left = QtWidgets.QWidget(Form)
        self.widget_Left.setSizeIncrement(QtCore.QSize(30, 0))
        self.widget_Left.setObjectName("widget_Left")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_Left)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lable_Local_Dire = QtWidgets.QLabel(self.widget_Left)
        self.lable_Local_Dire.setObjectName("lable_Local_Dire")
        self.verticalLayout_4.addWidget(self.lable_Local_Dire)
        self.listWidget_Local = QtWidgets.QListWidget(self.widget_Left)
        self.listWidget_Local.setObjectName("listWidget_Local")
        self.verticalLayout_4.addWidget(self.listWidget_Local)
        self.line = QtWidgets.QFrame(self.widget_Left)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.lable_Cloud_Playlist = QtWidgets.QLabel(self.widget_Left)
        self.lable_Cloud_Playlist.setObjectName("lable_Cloud_Playlist")
        self.verticalLayout_4.addWidget(self.lable_Cloud_Playlist)
        self.listWidget_Cloud = QtWidgets.QListWidget(self.widget_Left)
        self.listWidget_Cloud.setObjectName("listWidget_Cloud")
        self.verticalLayout_4.addWidget(self.listWidget_Cloud)
        self.horizontalLayout_Top.addWidget(self.widget_Left)
        self.verticalLayout_Right = QtWidgets.QVBoxLayout()
        self.verticalLayout_Right.setObjectName("verticalLayout_Right")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_Search = QtWidgets.QLineEdit(Form)
        self.lineEdit_Search.setObjectName("lineEdit_Search")
        self.horizontalLayout_2.addWidget(self.lineEdit_Search)
        self.pushButton_Search = QtWidgets.QPushButton(Form)
        self.pushButton_Search.setObjectName("pushButton_Search")
        self.horizontalLayout_2.addWidget(self.pushButton_Search)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_Track = QtWidgets.QRadioButton(Form)
        self.radioButton_Track.setObjectName("radioButton_Track")
        self.horizontalLayout.addWidget(self.radioButton_Track)
        self.radioButton_Artist = QtWidgets.QRadioButton(Form)
        self.radioButton_Artist.setObjectName("radioButton_Artist")
        self.horizontalLayout.addWidget(self.radioButton_Artist)
        self.radioButton_Album = QtWidgets.QRadioButton(Form)
        self.radioButton_Album.setObjectName("radioButton_Album")
        self.horizontalLayout.addWidget(self.radioButton_Album)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_Right.addLayout(self.verticalLayout)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout_Right.addWidget(self.tableWidget)
        self.horizontalLayout_Top.addLayout(self.verticalLayout_Right)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_Top)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "pyNetEase Player"))
        self.lable_Local_Dire.setText(_translate("Form", "Local Directory"))
        self.lable_Cloud_Playlist.setText(_translate("Form", "Cloud Playlist"))
        self.pushButton_Search.setText(_translate("Form", "Search"))
        self.radioButton_Track.setText(_translate("Form", "Track"))
        self.radioButton_Artist.setText(_translate("Form", "Artist"))
        self.radioButton_Album.setText(_translate("Form", "Album"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Download"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Track"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Artist"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Album"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Length"))

