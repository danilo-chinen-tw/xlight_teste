# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inform.ui'
#
# Created: Thu Jul 26 19:51:24 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

try:
	from PyQt4 import QtCore, QtGui
	from PyQt4.QtGui import QPushButton, QLabel, QApplication
except:
	from PyQt5 import QtCore, QtGui, QtWidgets
	from PyQt5.QtWidgets import QPushButton, QLabel, QApplication

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s
	

class Ui_FInform(object):
	def setupUi(self, FInform, infoString):
		FInform.setObjectName(_fromUtf8("FInform"))
		FInform.resize(500, 112)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("imgs/window.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		FInform.setWindowIcon(icon)
		self.PbOk = QPushButton(FInform)
		self.PbOk.setGeometry(QtCore.QRect(20, 72, 460, 31))
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8("imgs/ok.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.PbOk.setIcon(icon1)
		self.PbOk.setObjectName(_fromUtf8("PbOk"))
		self.LbInform = QLabel(FInform)
		self.LbInform.setGeometry(QtCore.QRect(70, 20, 401, 41))
		self.LbInform.setText(_fromUtf8(infoString))
		self.LbInform.setScaledContents(False)
		self.LbInform.setAlignment(QtCore.Qt.AlignCenter)
		self.LbInform.setObjectName(_fromUtf8("LbInform"))
		self.label = QLabel(FInform)
		self.label.setGeometry(QtCore.QRect(10, 20, 41, 41))
		self.label.setPixmap(QtGui.QPixmap(_fromUtf8("imgs/exclamation.ico")))
		self.label.setScaledContents(True)
		self.label.setObjectName(_fromUtf8("label"))

		self.retranslateUi(FInform)
		QtCore.QMetaObject.connectSlotsByName(FInform)
		try:
			QtCore.QObject.connect(self.PbOk, QtCore.SIGNAL(_fromUtf8("clicked()")), FInform.close)
		except:
			self.PbOk.clicked.connect(FInform.close)


	def retranslateUi(self, FInform):
		try:
			FInform.setWindowTitle(QApplication.translate("FInform", "XLightData", None, QApplication.UnicodeUTF8))
			self.PbOk.setText(QApplication.translate("FInform", "OK", None, QApplication.UnicodeUTF8))
		except:
			FInform.setWindowTitle(QApplication.translate("FInform", "XLightData", None, 0))
			self.PbOk.setText(QApplication.translate("FInform", "OK", None, 0))

class Ui_FErro(object):
	def setupUi(self, FInform, infoString):
		FInform.setObjectName(_fromUtf8("FInform"))
		FInform.resize(500, 112)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("imgs/window.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		FInform.setWindowIcon(icon)
		self.PbOk = QPushButton(FInform)
		self.PbOk.setGeometry(QtCore.QRect(20, 72, 460, 31))
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8("imgs/ok.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.PbOk.setIcon(icon1)
		self.PbOk.setObjectName(_fromUtf8("PbOk"))
		self.LbInform = QLabel(FInform)
		self.LbInform.setGeometry(QtCore.QRect(70, 20, 401, 41))
		self.LbInform.setText(_fromUtf8(infoString))
		self.LbInform.setScaledContents(False)
		self.LbInform.setAlignment(QtCore.Qt.AlignCenter)
		self.LbInform.setObjectName(_fromUtf8("LbInform"))
		self.label = QLabel(FInform)
		self.label.setGeometry(QtCore.QRect(10, 20, 41, 41))
		self.label.setPixmap(QtGui.QPixmap(_fromUtf8("imgs/erro.ico")))
		self.label.setScaledContents(True)
		self.label.setObjectName(_fromUtf8("label"))

		self.retranslateUi(FInform)
		QtCore.QMetaObject.connectSlotsByName(FInform)
		try:
			QtCore.QObject.connect(self.PbOk, QtCore.SIGNAL(_fromUtf8("clicked()")), FInform.close)
		except:
			self.PbOk.clicked.connect(FInform.close)


	def retranslateUi(self, FInform):
		try:
			FInform.setWindowTitle(QApplication.translate("FInform", "XLightData", None, QApplication.UnicodeUTF8))
			self.PbOk.setText(QApplication.translate("FInform", "OK", None, QApplication.UnicodeUTF8))
		except:
			FInform.setWindowTitle(QApplication.translate("FInform", "XLightData", None, 0))
			self.PbOk.setText(QApplication.translate("FInform", "OK", None, 0))

class Ui_FAccept(object):
	def setupUi(self, FInform, infoString):
		FInform.setObjectName(_fromUtf8("FInform"))
		FInform.resize(500, 112)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("imgs/window.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		FInform.setWindowIcon(icon)
		self.PbOk = QPushButton(FInform)
		self.PbOk.setGeometry(QtCore.QRect(20, 72, 460, 31))
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8("imgs/ok.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.PbOk.setIcon(icon1)
		self.PbOk.setObjectName(_fromUtf8("PbOk"))
		self.LbInform = QLabel(FInform)
		self.LbInform.setGeometry(QtCore.QRect(70, 20, 401, 41))
		self.LbInform.setText(_fromUtf8(infoString))
		self.LbInform.setScaledContents(False)
		self.LbInform.setAlignment(QtCore.Qt.AlignCenter)
		self.LbInform.setObjectName(_fromUtf8("LbInform"))
		self.label = QLabel(FInform)
		self.label.setGeometry(QtCore.QRect(10, 20, 41, 41))
		self.label.setPixmap(QtGui.QPixmap(_fromUtf8("imgs/accept.ico")))
		self.label.setScaledContents(True)
		self.label.setObjectName(_fromUtf8("label"))

		self.retranslateUi(FInform)
		QtCore.QMetaObject.connectSlotsByName(FInform)
		try:
			QtCore.QObject.connect(self.PbOk, QtCore.SIGNAL(_fromUtf8("clicked()")), FInform.close)
		except:
			self.PbOk.clicked.connect(FInform.close)


	def retranslateUi(self, FInform):
		try:
			FInform.setWindowTitle(QApplication.translate("FInform", "XLightData", None, QApplication.UnicodeUTF8))
			self.PbOk.setText(QApplication.translate("FInform", "OK", None, QApplication.UnicodeUTF8))
		except:
			FInform.setWindowTitle(QApplication.translate("FInform", "XLightData", None, 0))
			self.PbOk.setText(QApplication.translate("FInform", "OK", None, 0))
