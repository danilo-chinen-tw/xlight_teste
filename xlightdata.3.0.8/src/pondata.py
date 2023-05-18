# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pondata.ui'
#
# Created: Fri Jul 27 13:53:16 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

try:
	from PyQt4 import QtCore, QtGui
	from PyQt4.QtGui import QWidget, QTabWidget, QLineEdit, QGroupBox, QLabel
	from PyQt4.QtGui import QComboBox, QPushButton, QApplication, QDialog
except:
	from PyQt5 import QtCore, QtGui, QtWidgets
	from PyQt5.QtWidgets import QWidget, QTabWidget, QLineEdit, QGroupBox, QLabel 
	from PyQt5.QtWidgets import QComboBox, QPushButton, QApplication, QDialog

import binascii
import struct
import subprocess
from os import path
import signal
import re
import sys
from inform import * 
from formso import *
from asgamac import *
from invfile import *
from invSend import *
from threading import Thread
from unicodedata import normalize 

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = path.relpath("../orders/")
orders_path = os.path.join(script_dir, rel_path) + "/"
	
			
							

class Ui_PDMainWindow(object):
	def setupUi(self, PDMainWindow):
		PDMainWindow.setObjectName(_fromUtf8("PDMainWindow"))
		PDMainWindow.resize(715, 590)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("imgs/window.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		PDMainWindow.setWindowIcon(icon)
		
		self.PDcentralwidget = QWidget(PDMainWindow)
			
		self.PDcentralwidget.setObjectName(_fromUtf8("PDcentralwidget"))
		
		
		self.PDtabWidget = QTabWidget(self.PDcentralwidget)			
		self.PDtabWidget.setGeometry(QtCore.QRect(0, 150, 720, 441))
		self.PDtabWidget.setObjectName(_fromUtf8("PDtabWidget"))
		
		self.TabOlt = QWidget()			
		self.TabOlt.setObjectName(_fromUtf8("TabOlt"))
		
		self.LeOltMac = QLineEdit(self.TabOlt)
		self.LeOltMac.setEnabled(False)
		self.LeOltMac.setGeometry(QtCore.QRect(210, 10, 151, 31))
		self.LeOltMac.setMaxLength(18)
		self.LeOltMac.setObjectName(_fromUtf8("LeOltMac"))
		
		self.LeOltCprod = QLineEdit(self.TabOlt)
		self.LeOltCprod.setEnabled(False)
		self.LeOltCprod.setGeometry(QtCore.QRect(210, 45, 101, 31))
		self.LeOltCprod.setMaxLength(8)
		self.LeOltCprod.setObjectName(_fromUtf8("LeOltCprod"))
		
		self.LeOltNserie = QLineEdit(self.TabOlt)
		self.LeOltNserie.setEnabled(False)
		self.LeOltNserie.setGeometry(QtCore.QRect(210, 80, 161, 31))
		self.LeOltNserie.setMaxLength(6)
		self.LeOltNserie.setObjectName(_fromUtf8("LeOltNserie"))
		
		self.LeOltData = QLineEdit(self.TabOlt)
		self.LeOltData.setEnabled(False)
		self.LeOltData.setGeometry(QtCore.QRect(210, 115, 161, 31))
		self.LeOltData.setMaxLength(11)
		self.LeOltData.setObjectName(_fromUtf8("LeOltData"))
		
		self.LeOltDproduto = QLineEdit(self.TabOlt)
		self.LeOltDproduto.setGeometry(QtCore.QRect(210, 185, 301, 31))
		self.LeOltDproduto.setMaxLength(30)
		self.LeOltDproduto.setObjectName(_fromUtf8("LeOltDproduto"))
		
		self.LeOltTec = QLineEdit(self.TabOlt)
		self.LeOltTec.setGeometry(QtCore.QRect(210, 220, 301, 31))
		self.LeOltTec.setMaxLength(100)
		self.LeOltTec.setObjectName(_fromUtf8("LeOltTec"))
		
		self.LeOltNpedido = QLineEdit(self.TabOlt)
		self.LeOltNpedido.setGeometry(QtCore.QRect(210, 150, 151, 31))
		self.LeOltNpedido.setObjectName(_fromUtf8("LeOltNpedido"))
		
		self.GbOltVersoes = QGroupBox(self.TabOlt)
		self.GbOltVersoes.setGeometry(QtCore.QRect(20, 330, 220, 80))
		self.GbOltVersoes.setObjectName(_fromUtf8("GbOltVersoes"))
		
		self.LeOltVhw = QLineEdit(self.GbOltVersoes)
		self.LeOltVhw.setEnabled(False)
		self.LeOltVhw.setGeometry(QtCore.QRect(10, 40, 81, 31))
		self.LeOltVhw.setObjectName(_fromUtf8("LeOltVhw"))
		
		self.LeOltVfw = QLineEdit(self.GbOltVersoes)
		self.LeOltVfw.setEnabled(False)
		self.LeOltVfw.setGeometry(QtCore.QRect(120, 40, 81, 31))
		self.LeOltVfw.setObjectName(_fromUtf8("LeOltVfw"))
		
		self.LaOltVhw = QLabel(self.GbOltVersoes)
		self.LaOltVhw.setGeometry(QtCore.QRect(10, 20, 80, 16))
		self.LaOltVhw.setObjectName(_fromUtf8("LaOltVhw"))
		
		self.LaOltVfw = QLabel(self.GbOltVersoes)
		self.LaOltVfw.setGeometry(QtCore.QRect(120, 20, 80, 14))
		self.LaOltVfw.setObjectName(_fromUtf8("LaOltVfw"))
	
		self.GbOltSoftware = QGroupBox(self.TabOlt)
		self.GbOltSoftware.setGeometry(QtCore.QRect(280, 330, 280, 80))
		self.GbOltSoftware.setObjectName(_fromUtf8("GbOltSoftware"))
		
		self.LeOltStartup = QLineEdit(self.GbOltSoftware)
		self.LeOltStartup.setEnabled(False)
		self.LeOltStartup.setGeometry(QtCore.QRect(10, 40, 80, 30))
		self.LeOltStartup.setObjectName(_fromUtf8("LeOltStartup"))
		
		self.LeOltSystem = QLineEdit(self.GbOltSoftware)
		self.LeOltSystem.setEnabled(False)
		self.LeOltSystem.setGeometry(QtCore.QRect(100, 40, 80, 30))
		self.LeOltSystem.setObjectName(_fromUtf8("LeOltSystem"))
		
		self.LaOltStartup = QLabel(self.GbOltSoftware)
		self.LaOltStartup.setGeometry(QtCore.QRect(10, 20, 57, 14))
		self.LaOltStartup.setObjectName(_fromUtf8("LaOltStartup"))
		
		self.LaOltSystem = QLabel(self.GbOltSoftware)
		self.LaOltSystem.setGeometry(QtCore.QRect(100, 20, 57, 14))
		self.LaOltSystem.setObjectName(_fromUtf8("LaOltSystem"))
		
		self.LaOltAsgos = QLabel(self.GbOltSoftware)
		self.LaOltAsgos.setGeometry(QtCore.QRect(190, 20, 57, 14))
		self.LaOltAsgos.setObjectName(_fromUtf8("LaOltAsgos"))
		
		self.LeOltAsgos = QLineEdit(self.GbOltSoftware)
		self.LeOltAsgos.setEnabled(False)
		self.LeOltAsgos.setGeometry(QtCore.QRect(190, 40, 80, 30))
		self.LeOltAsgos.setObjectName(_fromUtf8("LeOltAsgos"))
		
		self.LaOltMac = QLabel(self.TabOlt)
		self.LaOltMac.setGeometry(QtCore.QRect(20, 20, 181, 21))
		self.LaOltMac.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOltMac.setObjectName(_fromUtf8("LaOltMac"))
		
		self.LaOltCprod = QLabel(self.TabOlt)
		self.LaOltCprod.setGeometry(QtCore.QRect(20, 55, 180, 21))
		self.LaOltCprod.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOltCprod.setObjectName(_fromUtf8("LaOltCprod"))
		
		self.LaOltNserie = QLabel(self.TabOlt)
		self.LaOltNserie.setGeometry(QtCore.QRect(20, 90, 180, 21))
		self.LaOltNserie.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOltNserie.setObjectName(_fromUtf8("LaOltNserie"))
		
		self.LaOltData = QLabel(self.TabOlt)
		self.LaOltData.setGeometry(QtCore.QRect(20, 125, 180, 21))
		self.LaOltData.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOltData.setObjectName(_fromUtf8("LaOltData"))
		
		self.LaOltNpedido = QLabel(self.TabOlt)
		self.LaOltNpedido.setGeometry(QtCore.QRect(20, 160, 180, 21))
		self.LaOltNpedido.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOltNpedido.setObjectName(_fromUtf8("LaOltNpedido"))
		
		self.LaOltDproduto = QLabel(self.TabOlt)
		self.LaOltDproduto.setGeometry(QtCore.QRect(20, 195, 180, 21))
		self.LaOltDproduto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOltDproduto.setObjectName(_fromUtf8("LaOltDproduto"))
		
		self.LaOltTec = QLabel(self.TabOlt)
		self.LaOltTec.setGeometry(QtCore.QRect(20, 230, 180, 21))
		self.LaOltTec.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOltTec.setObjectName(_fromUtf8("LaOltTec"))
		
		self.LaOltResets = QLabel(self.TabOlt)
		self.LaOltResets.setGeometry(QtCore.QRect(20, 265, 180, 20))
		self.LaOltResets.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOltResets.setObjectName(_fromUtf8("LaOltResets"))
		
		self.LeOltResets = QLineEdit(self.TabOlt)
		self.LeOltResets.setGeometry(QtCore.QRect(210, 255, 81, 31))
		self.LeOltResets.setObjectName(_fromUtf8("LeOltResets"))
		self.LeOltResets.setEnabled(False)
		self.PDtabWidget.addTab(self.TabOlt, _fromUtf8(""))
		
		#ONU Inventory fields
		self.TabOnu = QWidget()
		self.TabOnu.setObjectName(_fromUtf8("TabOnu"))
		self.LaOnuData = QLabel(self.TabOnu)
		self.LaOnuData.setGeometry(QtCore.QRect(20, 160, 181, 21))
		self.LaOnuData.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOnuData.setObjectName(_fromUtf8("LaOnuData"))
		self.LeOnuMac = QLineEdit(self.TabOnu)
		self.LeOnuMac.setEnabled(False)
		self.LeOnuMac.setGeometry(QtCore.QRect(210, 10, 161, 31))
		self.LeOnuMac.setMaxLength(18)
		self.LeOnuMac.setObjectName(_fromUtf8("LeOnuMac"))
		self.LeOnuDproduto = QLineEdit(self.TabOnu)
		self.LeOnuDproduto.setGeometry(QtCore.QRect(210, 220, 341, 31))
		self.LeOnuDproduto.setMaxLength(30)
		self.LeOnuDproduto.setObjectName(_fromUtf8("LeOnuDproduto"))
		self.LeOnuResets = QLineEdit(self.TabOnu)
		self.LeOnuResets.setGeometry(QtCore.QRect(210, 290, 81, 31))
		self.LeOnuResets.setObjectName(_fromUtf8("LeOnuResets"))
		self.LeOnuResets.setEnabled(False)
		self.LeOnuNpedido = QLineEdit(self.TabOnu)
		self.LeOnuNpedido.setGeometry(QtCore.QRect(210, 185, 161, 31))
		self.LeOnuNpedido.setObjectName(_fromUtf8("LeOnuNpedido"))
		self.LaOnuMac = QLabel(self.TabOnu)
		self.LaOnuMac.setGeometry(QtCore.QRect(20, 20, 181, 21))
		self.LaOnuMac.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOnuMac.setObjectName(_fromUtf8("LaOnuMac"))
		self.LeOnuNserie = QLineEdit(self.TabOnu)
		self.LeOnuNserie.setEnabled(False)
		self.LeOnuNserie.setGeometry(QtCore.QRect(210, 80, 161, 31))
		self.LeOnuNserie.setMaxLength(6)
		self.LeOnuNserie.setObjectName(_fromUtf8("LeOnuNserie"))
		self.GbOnuSoftware = QGroupBox(self.TabOnu)
		self.GbOnuSoftware.setGeometry(QtCore.QRect(310, 330, 160, 80))
		self.GbOnuSoftware.setObjectName(_fromUtf8("GbOnuSoftware"))
		self.LeOnuSystem = QLineEdit(self.GbOnuSoftware)
		self.LeOnuSystem.setEnabled(False)
		self.LeOnuSystem.setGeometry(QtCore.QRect(40, 40, 81, 31))
		self.LeOnuSystem.setObjectName(_fromUtf8("LeOnuSystem"))
		self.LaOnuSystem = QLabel(self.GbOnuSoftware)
		self.LaOnuSystem.setGeometry(QtCore.QRect(40, 20, 80, 14))
		self.LaOnuSystem.setObjectName(_fromUtf8("LaOnuSystem"))
		
		self.GbOnuGtin = QGroupBox(self.TabOnu)
		self.GbOnuGtin.setGeometry(QtCore.QRect(500, 330, 160, 80))
		self.GbOnuGtin.setObjectName(_fromUtf8("GbOnuGtin"))
		self.LeOnuGtin = QLineEdit(self.GbOnuGtin)
		self.LeOnuGtin.setEnabled(False)
		self.LeOnuGtin.setGeometry(QtCore.QRect(20, 40, 120, 31))
		self.LeOnuGtin.setObjectName(_fromUtf8("LeGtin"))
		self.LaOnuGtin = QLabel(self.GbOnuGtin)
		self.LaOnuGtin.setGeometry(QtCore.QRect(20, 20, 80, 14))
		self.LaOnuGtin.setObjectName(_fromUtf8("LaGtin"))
		
		self.GbOnuVersoes = QGroupBox(self.TabOnu)
		self.GbOnuVersoes.setGeometry(QtCore.QRect(70, 330, 220, 80))
		self.GbOnuVersoes.setObjectName(_fromUtf8("GbOnuVersoes"))
		self.LeOnuVhw = QLineEdit(self.GbOnuVersoes)
		self.LeOnuVhw.setEnabled(False)
		self.LeOnuVhw.setGeometry(QtCore.QRect(10, 40, 81, 31))
		self.LeOnuVhw.setObjectName(_fromUtf8("LeOnuVhw"))
		self.LeOnuVfw = QLineEdit(self.GbOnuVersoes)
		self.LeOnuVfw.setEnabled(False)
		self.LeOnuVfw.setGeometry(QtCore.QRect(120, 40, 81, 31))
		self.LeOnuVfw.setObjectName(_fromUtf8("LeOnuVfw"))
		self.LaOnuVhw = QLabel(self.GbOnuVersoes)
		self.LaOnuVhw.setGeometry(QtCore.QRect(10, 20, 80, 16))
		self.LaOnuVhw.setObjectName(_fromUtf8("LaOnuVhw"))
		self.LaOnuVfw = QLabel(self.GbOnuVersoes)
		self.LaOnuVfw.setGeometry(QtCore.QRect(120, 20, 80, 14))
		self.LaOnuVfw.setObjectName(_fromUtf8("LaOnuVfw"))
		self.LeOnuCprod = QLineEdit(self.TabOnu)
		self.LeOnuCprod.setEnabled(False)
		self.LeOnuCprod.setGeometry(QtCore.QRect(210, 45, 81, 31))
		self.LeOnuCprod.setMaxLength(8)
		self.LeOnuCprod.setObjectName(_fromUtf8("LeOnuCprod"))
		self.LaOnuDproduto = QLabel(self.TabOnu)
		self.LaOnuDproduto.setGeometry(QtCore.QRect(20, 230, 181, 21))
		self.LaOnuDproduto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOnuDproduto.setObjectName(_fromUtf8("LaOnuDproduto"))
		self.LaOnuTec = QLabel(self.TabOnu)
		self.LaOnuTec.setGeometry(QtCore.QRect(20, 265, 181, 21))
		self.LaOnuTec.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOnuTec.setObjectName(_fromUtf8("LaOnuTec"))
		self.LaOnuNserie = QLabel(self.TabOnu)
		self.LaOnuNserie.setGeometry(QtCore.QRect(20, 90, 181, 21))
		self.LaOnuNserie.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOnuNserie.setObjectName(_fromUtf8("LaOnuNserie"))
		self.LaOnuNpedido = QLabel(self.TabOnu)
		self.LaOnuNpedido.setGeometry(QtCore.QRect(20, 195, 181, 21))
		self.LaOnuNpedido.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOnuNpedido.setObjectName(_fromUtf8("LaOnuNpedido"))
		palette = QtGui.QPalette()
		palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.black)
		self.LaOnuStatusPVL2 = QLabel(self.TabOnu)
		self.LaOnuStatusPVL2.setGeometry(QtCore.QRect(355, 167, 181, 21))
		self.LaOnuStatusPVL2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOnuStatusPVL2.setObjectName(_fromUtf8("LaOnuStatusPVL2"))
		self.LaOnuStatusPVL2.setPalette(palette)
		self.LaOnuStatusPVL2.setHidden(True)
		self.LbOnuStatusPVL2 = QLabel(self.TabOnu)
		self.LbOnuStatusPVL2.setGeometry(QtCore.QRect(540, 167, 183, 21))
		self.LbOnuStatusPVL2.setAlignment(QtCore.Qt.AlignLeft)#|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LbOnuStatusPVL2.setObjectName(_fromUtf8("LbOnuStatusPVL2"))
		self.LbOnuStatusPVL2.setPalette(palette)
		self.LbOnuStatusPVL2.setHidden(True)
		self.LaOnuStatusPVL3Lite = QLabel(self.TabOnu)
		self.LaOnuStatusPVL3Lite.setGeometry(QtCore.QRect(355, 182, 181, 21))
		self.LaOnuStatusPVL3Lite.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOnuStatusPVL3Lite.setObjectName(_fromUtf8("LaOnuStatusPVL3Lite"))
		self.LaOnuStatusPVL3Lite.setPalette(palette)
		self.LaOnuStatusPVL3Lite.setHidden(True)
		self.LbOnuStatusPVL3Lite = QLabel(self.TabOnu)
		self.LbOnuStatusPVL3Lite.setGeometry(QtCore.QRect(540, 182, 183, 21))
		self.LbOnuStatusPVL3Lite.setAlignment(QtCore.Qt.AlignLeft) #|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter
		self.LbOnuStatusPVL3Lite.setObjectName(_fromUtf8("LbOnuStatusPVL3Lite"))
		self.LbOnuStatusPVL3Lite.setPalette(palette)
		self.LbOnuStatusPVL3Lite.setHidden(True)
		self.LaOnuStatusPVL3Full = QLabel(self.TabOnu)
		self.LaOnuStatusPVL3Full.setGeometry(QtCore.QRect(355, 197, 181, 21))
		self.LaOnuStatusPVL3Full.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOnuStatusPVL3Full.setObjectName(_fromUtf8("LaOnuStatusPVL3Full"))
		self.LaOnuStatusPVL3Full.setPalette(palette)
		self.LaOnuStatusPVL3Full.setHidden(True)
		self.LbOnuStatusPVL3Full = QLabel(self.TabOnu)
		self.LbOnuStatusPVL3Full.setGeometry(QtCore.QRect(540, 197, 183, 21))
		self.LbOnuStatusPVL3Full.setAlignment(QtCore.Qt.AlignLeft) #|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter
		self.LbOnuStatusPVL3Full.setObjectName(_fromUtf8("LbOnuStatusPVL3Full"))
		self.LbOnuStatusPVL3Full.setPalette(palette)
		self.LbOnuStatusPVL3Full.setHidden(True)
		self.LeOnuTec = QLineEdit(self.TabOnu)
		self.LeOnuTec.setGeometry(QtCore.QRect(210, 255, 341, 31))
		self.LeOnuTec.setMaxLength(100)
		self.LeOnuTec.setObjectName(_fromUtf8("LeOnuTec"))
		self.LeOnuData = QLineEdit(self.TabOnu)
		self.LeOnuData.setEnabled(False)
		self.LeOnuData.setGeometry(QtCore.QRect(210, 150, 161, 31))
		self.LeOnuData.setMaxLength(11)
		self.LeOnuData.setObjectName(_fromUtf8("LeOnuData"))
		self.LaOnuResets = QLabel(self.TabOnu)
		self.LaOnuResets.setGeometry(QtCore.QRect(20, 300, 181, 21))
		self.LaOnuResets.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOnuResets.setObjectName(_fromUtf8("LaOnuResets"))
		self.LaOnuCprod = QLabel(self.TabOnu)
		self.LaOnuCprod.setGeometry(QtCore.QRect(20, 55, 181, 21))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Sans Serif"))
		self.LaOnuCprod.setFont(font)
		self.LaOnuCprod.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOnuCprod.setObjectName(_fromUtf8("LaOnuCprod"))
		self.LeOnuNspon = QLineEdit(self.TabOnu)
		self.LeOnuNspon.setEnabled(False)
		self.LeOnuNspon.setGeometry(QtCore.QRect(210, 115, 161, 31))
		self.LeOnuNspon.setMaxLength(25)
		self.LeOnuNspon.setObjectName(_fromUtf8("LeOnuNspon"))
		self.LaOnuNspon = QLabel(self.TabOnu)
		self.LaOnuNspon.setGeometry(QtCore.QRect(20, 125, 181, 21))
		self.LaOnuNspon.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOnuNspon.setObjectName(_fromUtf8("LaOnuNspon"))
		self.LaOnuLayer = QComboBox(self.TabOnu)
		self.LaOnuLayer.setGeometry(QtCore.QRect(380,45,190,31))
		LayerList = ['Escolha o produto..','ONU-HQ2*** (L2)','ONU-JQ2*** (L3 Lite)', 'ONU-KQ2*** (L3 Full)']
		self.LaOnuLayer.addItems(LayerList)
		self.LaOnuLayer.setCurrentIndex(0)
		self.LaOnuLayer.setHidden(True)

		
		self.PDtabWidget.addTab(self.TabOnu, _fromUtf8(""))
		
		#STM1-GW Inventory fields
		self.TabSTM1GW = QWidget()
		self.TabSTM1GW.setObjectName(_fromUtf8("TabSTM1GW"))
		self.LeSTM1Tec = QLineEdit(self.TabSTM1GW)
		self.LeSTM1Tec.setGeometry(QtCore.QRect(260, 195, 301, 31))
		self.LeSTM1Tec.setMaxLength(100)
		self.LeSTM1Tec.setObjectName(_fromUtf8("LeSTM1Tec"))
		self.LeSTM1Dproduto = QLineEdit(self.TabSTM1GW)
		self.LeSTM1Dproduto.setGeometry(QtCore.QRect(260, 160, 301, 31))
		self.LeSTM1Dproduto.setMaxLength(30)
		self.LeSTM1Dproduto.setObjectName(_fromUtf8("LeSTM1Dproduto"))
		self.LeSTM1Nserie = QLineEdit(self.TabSTM1GW)
		self.LeSTM1Nserie.setEnabled(False)
		self.LeSTM1Nserie.setGeometry(QtCore.QRect(260, 60, 161, 31))
		self.LeSTM1Nserie.setMaxLength(6)
		self.LeSTM1Nserie.setObjectName(_fromUtf8("LeSTM1Nserie"))
		self.LeSTM1Cprod = QLineEdit(self.TabSTM1GW)
		self.LeSTM1Cprod.setEnabled(False)
		self.LeSTM1Cprod.setGeometry(QtCore.QRect(260, 25, 81, 31))
		self.LeSTM1Cprod.setMaxLength(8)
		self.LeSTM1Cprod.setObjectName(_fromUtf8("LeSTM1Cprod"))
		self.LaSTM1Tec = QLabel(self.TabSTM1GW)
		self.LaSTM1Tec.setGeometry(QtCore.QRect(70, 205, 181, 21))
		self.LaSTM1Tec.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaSTM1Tec.setObjectName(_fromUtf8("LaSTM1Tec"))
		self.LaSTM1Nserie = QLabel(self.TabSTM1GW)
		self.LaSTM1Nserie.setGeometry(QtCore.QRect(70, 70, 181, 21))
		self.LaSTM1Nserie.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaSTM1Nserie.setObjectName(_fromUtf8("LaSTM1Nserie"))
		self.LeSTM1Data = QLineEdit(self.TabSTM1GW)
		self.LeSTM1Data.setEnabled(False)
		self.LeSTM1Data.setGeometry(QtCore.QRect(260, 90, 161, 31))
		self.LeSTM1Data.setMaxLength(11)
		self.LeSTM1Data.setObjectName(_fromUtf8("LeSTM1Data"))
		self.LeSTM1Resets = QLineEdit(self.TabSTM1GW)
		self.LeSTM1Resets.setEnabled(False)
		self.LeSTM1Resets.setGeometry(QtCore.QRect(260, 230, 81, 31))
		self.LeSTM1Resets.setObjectName(_fromUtf8("LeSTM1Resets"))
		self.LaSTM1Cprod = QLabel(self.TabSTM1GW)
		self.LaSTM1Cprod.setGeometry(QtCore.QRect(70, 35, 181, 21))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Sans Serif"))
		self.LaSTM1Cprod.setFont(font)
		self.LaSTM1Cprod.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaSTM1Cprod.setObjectName(_fromUtf8("LaSTM1Cprod"))
		self.GbSTM1Versoes = QGroupBox(self.TabSTM1GW)
		self.GbSTM1Versoes.setGeometry(QtCore.QRect(180, 290, 220, 80))
		self.GbSTM1Versoes.setObjectName(_fromUtf8("GbSTM1Versoes"))
		self.LeSTM1Vhw = QLineEdit(self.GbSTM1Versoes)
		self.LeSTM1Vhw.setEnabled(False)
		self.LeSTM1Vhw.setGeometry(QtCore.QRect(10, 40, 81, 31))
		self.LeSTM1Vhw.setObjectName(_fromUtf8("LeSTM1Vhw"))
		self.LeSTM1Vfw = QLineEdit(self.GbSTM1Versoes)
		self.LeSTM1Vfw.setEnabled(False)
		self.LeSTM1Vfw.setGeometry(QtCore.QRect(120, 40, 81, 31))
		self.LeSTM1Vfw.setObjectName(_fromUtf8("LeSTM1Vfw"))
		self.LaSTM1Vhw = QLabel(self.GbSTM1Versoes)
		self.LaSTM1Vhw.setGeometry(QtCore.QRect(10, 20, 80, 16))
		self.LaSTM1Vhw.setObjectName(_fromUtf8("LaSTM1Vhw"))
		self.LaSTM1Vfw = QLabel(self.GbSTM1Versoes)
		self.LaSTM1Vfw.setGeometry(QtCore.QRect(120, 20, 80, 14))
		self.LaSTM1Vfw.setObjectName(_fromUtf8("LaSTM1Vfw"))
		self.LaSTM1Data = QLabel(self.TabSTM1GW)
		self.LaSTM1Data.setGeometry(QtCore.QRect(70, 100, 181, 21))
		self.LaSTM1Data.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaSTM1Data.setObjectName(_fromUtf8("LaSTM1Data"))
		self.LaSTM1Npedido = QLabel(self.TabSTM1GW)
		self.LaSTM1Npedido.setGeometry(QtCore.QRect(70, 135, 181, 21))
		self.LaSTM1Npedido.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaSTM1Npedido.setObjectName(_fromUtf8("LaSTM1Npedido"))
		self.LeSTM1Npedido = QLineEdit(self.TabSTM1GW)
		self.LeSTM1Npedido.setGeometry(QtCore.QRect(260, 125, 161, 31))
		self.LeSTM1Npedido.setObjectName(_fromUtf8("LeSTM1Npedido"))
		self.LaSTM1Resets = QLabel(self.TabSTM1GW)
		self.LaSTM1Resets.setGeometry(QtCore.QRect(70, 240, 181, 21))
		self.LaSTM1Resets.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaSTM1Resets.setObjectName(_fromUtf8("LaSTM1Resets"))
		self.LaSTM1Dproduto = QLabel(self.TabSTM1GW)
		self.LaSTM1Dproduto.setGeometry(QtCore.QRect(70, 170, 181, 21))
		self.LaSTM1Dproduto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaSTM1Dproduto.setObjectName(_fromUtf8("LaSTM1Dproduto"))
		self.PDtabWidget.addTab(self.TabSTM1GW, _fromUtf8(""))
		
		#OLT Blade Inventory fields
		self.TabOltBlade = QWidget()
		self.TabOltBlade.setObjectName(_fromUtf8("TabOltBlade"))
		self.LeOltBladeMac = QLineEdit(self.TabOltBlade)
		self.LeOltBladeMac.setEnabled(False)
		self.LeOltBladeMac.setGeometry(QtCore.QRect(210, 10, 151, 31))
		self.LeOltBladeMac.setMaxLength(18)
		self.LeOltBladeMac.setObjectName(_fromUtf8("LeOltBladeMac"))
		self.LeOltBladeCprod = QLineEdit(self.TabOltBlade)
		self.LeOltBladeCprod.setEnabled(False)
		self.LeOltBladeCprod.setGeometry(QtCore.QRect(210, 45, 101, 31))
		self.LeOltBladeCprod.setMaxLength(8)
		self.LeOltBladeCprod.setObjectName(_fromUtf8("LeOltBladeCprod"))
		self.LeOltBladeNserie = QLineEdit(self.TabOltBlade)
		self.LeOltBladeNserie.setEnabled(False)
		self.LeOltBladeNserie.setGeometry(QtCore.QRect(210, 80, 161, 31))
		self.LeOltBladeNserie.setMaxLength(6)
		self.LeOltBladeNserie.setObjectName(_fromUtf8("LeOltBladeNserie"))
		self.LeOltBladeData = QLineEdit(self.TabOltBlade)
		self.LeOltBladeData.setEnabled(False)
		self.LeOltBladeData.setGeometry(QtCore.QRect(210, 115, 161, 31))
		self.LeOltBladeData.setMaxLength(11)
		self.LeOltBladeData.setObjectName(_fromUtf8("LeOltBladeData"))
		self.LeOltBladeDproduto = QLineEdit(self.TabOltBlade)
		self.LeOltBladeDproduto.setGeometry(QtCore.QRect(210, 185, 301, 31))
		self.LeOltBladeDproduto.setMaxLength(30)
		self.LeOltBladeDproduto.setObjectName(_fromUtf8("LeOltBladeDproduto"))
		self.LeOltBladeTec = QLineEdit(self.TabOltBlade)
		self.LeOltBladeTec.setGeometry(QtCore.QRect(210, 220, 301, 31))
		self.LeOltBladeTec.setMaxLength(100)
		self.LeOltBladeTec.setObjectName(_fromUtf8("LeOltBladeTec"))
		self.LeOltBladeNpedido = QLineEdit(self.TabOltBlade)
		self.LeOltBladeNpedido.setGeometry(QtCore.QRect(210, 150, 151, 31))
		self.LeOltBladeNpedido.setObjectName(_fromUtf8("LeOltBladeNpedido"))
		self.GbOltBladeVersoes = QGroupBox(self.TabOltBlade)
		self.GbOltBladeVersoes.setGeometry(QtCore.QRect(20, 330, 220, 80))
		self.GbOltBladeVersoes.setObjectName(_fromUtf8("GbOltBladeVersoes"))
		self.LeOltBladeVhw = QLineEdit(self.GbOltBladeVersoes)
		self.LeOltBladeVhw.setEnabled(False)
		self.LeOltBladeVhw.setGeometry(QtCore.QRect(10, 40, 81, 31))
		self.LeOltBladeVhw.setObjectName(_fromUtf8("LeOltBladeVhw"))
		self.LeOltBladeVfw = QLineEdit(self.GbOltBladeVersoes)
		self.LeOltBladeVfw.setEnabled(False)
		self.LeOltBladeVfw.setGeometry(QtCore.QRect(120, 40, 81, 31))
		self.LeOltBladeVfw.setObjectName(_fromUtf8("LeOltBladeVfw"))
		self.LaOltBladeVhw = QLabel(self.GbOltBladeVersoes)
		self.LaOltBladeVhw.setGeometry(QtCore.QRect(10, 20, 80, 16))
		self.LaOltBladeVhw.setObjectName(_fromUtf8("LaOltBladeVhw"))
		self.LaOltBladeVfw = QLabel(self.GbOltBladeVersoes)
		self.LaOltBladeVfw.setGeometry(QtCore.QRect(120, 20, 80, 14))
		self.LaOltBladeVfw.setObjectName(_fromUtf8("LaOltBladeVfw"))
		self.GbOltBladeSoftware = QGroupBox(self.TabOltBlade)
		self.GbOltBladeSoftware.setGeometry(QtCore.QRect(280, 330, 280, 80))
		self.GbOltBladeSoftware.setObjectName(_fromUtf8("GbOltBladeSoftware"))
		self.LeOltBladeStartup = QLineEdit(self.GbOltBladeSoftware)
		self.LeOltBladeStartup.setEnabled(False)
		self.LeOltBladeStartup.setGeometry(QtCore.QRect(10, 40, 80, 30))
		self.LeOltBladeStartup.setObjectName(_fromUtf8("LeOltBladeStartup"))
		self.LeOltBladeSystem = QLineEdit(self.GbOltBladeSoftware)
		self.LeOltBladeSystem.setEnabled(False)
		self.LeOltBladeSystem.setGeometry(QtCore.QRect(100, 40, 80, 30))
		self.LeOltBladeSystem.setObjectName(_fromUtf8("LeOltBladeSystem"))
		self.LaOltBladeStartup = QLabel(self.GbOltBladeSoftware)
		self.LaOltBladeStartup.setGeometry(QtCore.QRect(10, 20, 57, 14))
		self.LaOltBladeStartup.setObjectName(_fromUtf8("LaOltBladeStartup"))
		self.LaOltBladeSystem = QLabel(self.GbOltBladeSoftware)
		self.LaOltBladeSystem.setGeometry(QtCore.QRect(100, 20, 57, 14))
		self.LaOltBladeSystem.setObjectName(_fromUtf8("LaOltBladeSystem"))
		self.LaOltBladeAsgos = QLabel(self.GbOltBladeSoftware)
		self.LaOltBladeAsgos.setGeometry(QtCore.QRect(190, 20, 57, 14))
		self.LaOltBladeAsgos.setObjectName(_fromUtf8("LaOltBladeAsgos"))
		self.LeOltBladeAsgos = QLineEdit(self.GbOltBladeSoftware)
		self.LeOltBladeAsgos.setEnabled(False)
		self.LeOltBladeAsgos.setGeometry(QtCore.QRect(190, 40, 80, 30))
		self.LeOltBladeAsgos.setObjectName(_fromUtf8("LeOltBladeAsgos"))
		self.LaOltBladeMac = QLabel(self.TabOltBlade)
		self.LaOltBladeMac.setGeometry(QtCore.QRect(20, 20, 181, 21))
		self.LaOltBladeMac.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOltBladeMac.setObjectName(_fromUtf8("LaOltMac"))
		self.LaOltBladeCprod = QLabel(self.TabOltBlade)
		self.LaOltBladeCprod.setGeometry(QtCore.QRect(20, 55, 180, 21))
		self.LaOltBladeCprod.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOltBladeCprod.setObjectName(_fromUtf8("LaOltBladeCprod"))
		self.LaOltBladeNserie = QLabel(self.TabOltBlade)
		self.LaOltBladeNserie.setGeometry(QtCore.QRect(20, 90, 180, 21))
		self.LaOltBladeNserie.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOltBladeNserie.setObjectName(_fromUtf8("LaOltBladeNserie"))
		self.LaOltBladeData = QLabel(self.TabOltBlade)
		self.LaOltBladeData.setGeometry(QtCore.QRect(20, 125, 180, 21))
		self.LaOltBladeData.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOltBladeData.setObjectName(_fromUtf8("LaOltBladeData"))
		self.LaOltBladeNpedido = QLabel(self.TabOltBlade)
		self.LaOltBladeNpedido.setGeometry(QtCore.QRect(20, 160, 180, 21))
		self.LaOltBladeNpedido.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOltBladeNpedido.setObjectName(_fromUtf8("LaOltBladeNpedido"))
		self.LaOltBladeDproduto = QLabel(self.TabOltBlade)
		self.LaOltBladeDproduto.setGeometry(QtCore.QRect(20, 195, 180, 21))
		self.LaOltBladeDproduto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOltBladeDproduto.setObjectName(_fromUtf8("LaOltBladeDproduto"))
		self.LaOltBladeTec = QLabel(self.TabOltBlade)
		self.LaOltBladeTec.setGeometry(QtCore.QRect(20, 230, 180, 21))
		self.LaOltBladeTec.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOltBladeTec.setObjectName(_fromUtf8("LaOltBladeTec"))
		self.LaOltBladeResets = QLabel(self.TabOltBlade)
		self.LaOltBladeResets.setGeometry(QtCore.QRect(20, 265, 180, 20))
		self.LaOltBladeResets.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOltBladeResets.setObjectName(_fromUtf8("LaOltBladeResets"))
		self.LeOltBladeResets = QLineEdit(self.TabOltBlade)
		self.LeOltBladeResets.setGeometry(QtCore.QRect(210, 255, 81, 31))
		self.LeOltBladeResets.setObjectName(_fromUtf8("LeOltBladeResets"))
		self.LeOltBladeResets.setEnabled(False)
		self.PDtabWidget.addTab(self.TabOltBlade, _fromUtf8(""))
		
		#MSDD Inventory fields
		self.TabMSDD = QWidget()
		self.TabMSDD.setObjectName(_fromUtf8("TabMSDD"))
		self.LaMSDDData = QLabel(self.TabMSDD)
		self.LaMSDDData.setGeometry(QtCore.QRect(20, 160, 181, 21))
		self.LaMSDDData.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaMSDDData.setObjectName(_fromUtf8("LaMSDDData"))
		self.LeMSDDMac = QLineEdit(self.TabMSDD)
		self.LeMSDDMac.setEnabled(False)
		self.LeMSDDMac.setGeometry(QtCore.QRect(210, 10, 161, 31))
		self.LeMSDDMac.setMaxLength(18)
		self.LeMSDDMac.setObjectName(_fromUtf8("LeMSDDMac"))
		self.LeMSDDDproduto = QLineEdit(self.TabMSDD)
		self.LeMSDDDproduto.setGeometry(QtCore.QRect(210, 220, 301, 31))
		self.LeMSDDDproduto.setMaxLength(30)
		self.LeMSDDDproduto.setObjectName(_fromUtf8("LeMSDDDproduto"))
		self.LeMSDDResets = QLineEdit(self.TabMSDD)
		self.LeMSDDResets.setGeometry(QtCore.QRect(210, 290, 81, 31))
		self.LeMSDDResets.setObjectName(_fromUtf8("LeMSDDResets"))
		self.LeMSDDResets.setEnabled(False)
		self.LeMSDDNpedido = QLineEdit(self.TabMSDD)
		self.LeMSDDNpedido.setGeometry(QtCore.QRect(210, 185, 161, 31))
		self.LeMSDDNpedido.setObjectName(_fromUtf8("LeMSDDNpedido"))
		self.LaMSDDMac = QLabel(self.TabMSDD)
		self.LaMSDDMac.setGeometry(QtCore.QRect(20, 20, 181, 21))
		self.LaMSDDMac.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaMSDDMac.setObjectName(_fromUtf8("LaMSDDMac"))
		self.LeMSDDNserie = QLineEdit(self.TabMSDD)
		self.LeMSDDNserie.setEnabled(False)
		self.LeMSDDNserie.setGeometry(QtCore.QRect(210, 80, 161, 31))
		self.LeMSDDNserie.setMaxLength(6)
		self.LeMSDDNserie.setObjectName(_fromUtf8("LeMSDDNserie"))
		self.GbMSDDSoftware = QGroupBox(self.TabMSDD)
		self.GbMSDDSoftware.setGeometry(QtCore.QRect(310, 330, 160, 80))
		self.GbMSDDSoftware.setObjectName(_fromUtf8("GbMSDDSoftware"))
		self.LeMSDDSystem = QLineEdit(self.GbMSDDSoftware)
		self.LeMSDDSystem.setEnabled(False)
		self.LeMSDDSystem.setGeometry(QtCore.QRect(40, 40, 81, 31))
		self.LeMSDDSystem.setObjectName(_fromUtf8("LeMSDDSystem"))
		self.LaMSDDSystem = QLabel(self.GbMSDDSoftware)
		self.LaMSDDSystem.setGeometry(QtCore.QRect(40, 20, 80, 14))
		self.LaMSDDSystem.setObjectName(_fromUtf8("LaMSDDSystem"))
		self.GbMSDDVersoes = QGroupBox(self.TabMSDD)
		self.GbMSDDVersoes.setGeometry(QtCore.QRect(70, 330, 220, 80))
		self.GbMSDDVersoes.setObjectName(_fromUtf8("GbMSDDVersoes"))
		self.LeMSDDVhw = QLineEdit(self.GbMSDDVersoes)
		self.LeMSDDVhw.setEnabled(False)
		self.LeMSDDVhw.setGeometry(QtCore.QRect(10, 40, 81, 31))
		self.LeMSDDVhw.setObjectName(_fromUtf8("LeMSDDVhw"))
		self.LeMSDDVfw = QLineEdit(self.GbMSDDVersoes)
		self.LeMSDDVfw.setEnabled(False)
		self.LeMSDDVfw.setGeometry(QtCore.QRect(120, 40, 81, 31))
		self.LeMSDDVfw.setObjectName(_fromUtf8("LeMSDDVfw"))
		self.LaMSDDVhw = QLabel(self.GbMSDDVersoes)
		self.LaMSDDVhw.setGeometry(QtCore.QRect(10, 20, 80, 16))
		self.LaMSDDVhw.setObjectName(_fromUtf8("LaMSDDVhw"))
		self.LaMSDDVfw = QLabel(self.GbMSDDVersoes)
		self.LaMSDDVfw.setGeometry(QtCore.QRect(120, 20, 80, 14))
		self.LaMSDDVfw.setObjectName(_fromUtf8("LaMSDDVfw"))
		self.LeMSDDCprod = QLineEdit(self.TabMSDD)
		self.LeMSDDCprod.setEnabled(False)
		self.LeMSDDCprod.setGeometry(QtCore.QRect(210, 45, 81, 31))
		self.LeMSDDCprod.setMaxLength(8)
		self.LeMSDDCprod.setObjectName(_fromUtf8("LeMSDDCprod"))
		self.LaMSDDDproduto = QLabel(self.TabMSDD)
		self.LaMSDDDproduto.setGeometry(QtCore.QRect(20, 230, 181, 21))
		self.LaMSDDDproduto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaMSDDDproduto.setObjectName(_fromUtf8("LaMSDDDproduto"))
		self.LaMSDDTec = QLabel(self.TabMSDD)
		self.LaMSDDTec.setGeometry(QtCore.QRect(20, 265, 181, 21))
		self.LaMSDDTec.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaMSDDTec.setObjectName(_fromUtf8("LaMSDDTec"))
		self.LaMSDDNserie = QLabel(self.TabMSDD)
		self.LaMSDDNserie.setGeometry(QtCore.QRect(20, 90, 181, 21))
		self.LaMSDDNserie.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaMSDDNserie.setObjectName(_fromUtf8("LaMSDDNserie"))
		self.LaMSDDNpedido = QLabel(self.TabMSDD)
		self.LaMSDDNpedido.setGeometry(QtCore.QRect(20, 195, 181, 21))
		self.LaMSDDNpedido.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaMSDDNpedido.setObjectName(_fromUtf8("LaMSDDNpedido"))
		self.LeMSDDTec = QLineEdit(self.TabMSDD)
		self.LeMSDDTec.setGeometry(QtCore.QRect(210, 255, 301, 31))
		self.LeMSDDTec.setMaxLength(100)
		self.LeMSDDTec.setObjectName(_fromUtf8("LeMSDDTec"))
		self.LeMSDDData = QLineEdit(self.TabMSDD)
		self.LeMSDDData.setEnabled(False)
		self.LeMSDDData.setGeometry(QtCore.QRect(210, 150, 161, 31))
		self.LeMSDDData.setMaxLength(11)
		self.LeMSDDData.setObjectName(_fromUtf8("LeMSDDData"))
		self.LaMSDDResets = QLabel(self.TabMSDD)
		self.LaMSDDResets.setGeometry(QtCore.QRect(20, 300, 181, 21))
		self.LaMSDDResets.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaMSDDResets.setObjectName(_fromUtf8("LaMSDDResets"))
		self.LaMSDDCprod = QLabel(self.TabMSDD)
		self.LaMSDDCprod.setGeometry(QtCore.QRect(20, 55, 181, 21))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Sans Serif"))
		self.LaMSDDCprod.setFont(font)
		self.LaMSDDCprod.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaMSDDCprod.setObjectName(_fromUtf8("LaMSDDCprod"))
		self.LeMSDDNspon = QLineEdit(self.TabMSDD)
		self.LeMSDDNspon.setEnabled(False)
		self.LeMSDDNspon.setGeometry(QtCore.QRect(210, 115, 161, 31))
		self.LeMSDDNspon.setMaxLength(25)
		self.LeMSDDNspon.setObjectName(_fromUtf8("LeMSDDNspon"))
		self.LaMSDDNspon = QLabel(self.TabMSDD)
		self.LaMSDDNspon.setGeometry(QtCore.QRect(20, 125, 181, 21))
		self.LaMSDDNspon.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaMSDDNspon.setObjectName(_fromUtf8("LaMSDDNspon"))
		self.PDtabWidget.addTab(self.TabMSDD, _fromUtf8(""))

		#OLT Maple Inventory fields
		self.TabOltMaple = QWidget()
		self.TabOltMaple.setObjectName(_fromUtf8("TabOltMaple"))
		self.LeOltMapleModel = QLineEdit(self.TabOltMaple)
		self.LeOltMapleModel.setEnabled(False)
		self.LeOltMapleModel.setGeometry(QtCore.QRect(210, 10, 151, 31))
		self.LeOltMapleModel.setMaxLength(18)
		self.LeOltMapleModel.setObjectName(_fromUtf8("LeOltMapleModel"))
		self.LeOltMapleMac = QLineEdit(self.TabOltMaple)
		self.LeOltMapleMac.setEnabled(False)
		self.LeOltMapleMac.setGeometry(QtCore.QRect(210, 45, 151, 31))
		self.LeOltMapleMac.setMaxLength(18)
		self.LeOltMapleMac.setObjectName(_fromUtf8("LeOltMapleMac"))
		self.LeOltMapleCprod = QLineEdit(self.TabOltMaple)
		self.LeOltMapleCprod.setEnabled(False)
		self.LeOltMapleCprod.setGeometry(QtCore.QRect(210, 80, 150, 31))
		self.LeOltMapleCprod.setMaxLength(13)
		self.LeOltMapleCprod.setObjectName(_fromUtf8("LeOltMapleCprod"))
		self.LeOltMapleNserie = QLineEdit(self.TabOltMaple)
		self.LeOltMapleNserie.setEnabled(False)
		self.LeOltMapleNserie.setGeometry(QtCore.QRect(210, 115, 161, 31))
		self.LeOltMapleNserie.setMaxLength(6)
		self.LeOltMapleNserie.setObjectName(_fromUtf8("LeOltMapleNserie"))
		self.LeOltMapleData = QLineEdit(self.TabOltMaple)
		self.LeOltMapleData.setEnabled(False)
		self.LeOltMapleData.setGeometry(QtCore.QRect(210, 150, 161, 31))
		self.LeOltMapleData.setMaxLength(11)
		self.LeOltMapleData.setObjectName(_fromUtf8("LeOltMapleData"))
		self.LaOltMapleModel = QLabel(self.TabOltMaple)
		self.LaOltMapleModel.setGeometry(QtCore.QRect(20, 20, 181, 21))
		self.LaOltMapleModel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOltMapleModel.setObjectName(_fromUtf8("LaOltMapleModel"))
		self.LaOltMapleMac = QLabel(self.TabOltMaple)
		self.LaOltMapleMac.setGeometry(QtCore.QRect(20, 55, 181, 21))
		self.LaOltMapleMac.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOltMapleMac.setObjectName(_fromUtf8("LaOltMapleMac"))
		self.LaOltMapleCprod = QLabel(self.TabOltMaple)
		self.LaOltMapleCprod.setGeometry(QtCore.QRect(20, 90, 180, 21))
		self.LaOltMapleCprod.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOltMapleCprod.setObjectName(_fromUtf8("LaOltMapleCprod"))
		self.LaOltMapleNserie = QLabel(self.TabOltMaple)
		self.LaOltMapleNserie.setGeometry(QtCore.QRect(20, 125, 180, 21))
		self.LaOltMapleNserie.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOltMapleNserie.setObjectName(_fromUtf8("LaOltMapleNserie"))
		self.LaOltMapleData = QLabel(self.TabOltMaple)
		self.LaOltMapleData.setGeometry(QtCore.QRect(20, 160, 180, 21))
		self.LaOltMapleData.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.LaOltMapleData.setObjectName(_fromUtf8("LaOltMapleData"))
		self.PDtabWidget.addTab(self.TabOltMaple, _fromUtf8(""))
		

		self.LeCodbar = QLineEdit(self.PDcentralwidget)
		self.LeCodbar.setGeometry(QtCore.QRect(10, 40, 311, 31))
		self.LeCodbar.setMaxLength(32)
		self.LeCodbar.setObjectName(_fromUtf8("LeCodbar"))
		self.LaCodBar = QLabel(self.PDcentralwidget)
		self.LaCodBar.setGeometry(QtCore.QRect(10, 20, 180, 16))
		self.LaCodBar.setObjectName(_fromUtf8("LaCodBar"))
		self.PbWrite = QPushButton(self.PDcentralwidget)
		self.PbWrite.setGeometry(QtCore.QRect(430, 10, 160, 31))
		self.PbSend = QPushButton(self.PDcentralwidget)
		self.PbSend.setGeometry(QtCore.QRect(430, 45, 160, 31))
		icon0 = QtGui.QIcon()
		icon0.addPixmap(QtGui.QPixmap(_fromUtf8("imgs/send.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.PbSend.setIcon(icon0)
		self.PbSend.setObjectName(_fromUtf8("PbSend"))
		self.PbSend.setAutoDefault(True)
		self.PbSend.setEnabled(False)
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8("imgs/write.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.PbWrite.setIcon(icon1)
		self.PbWrite.setObjectName(_fromUtf8("PbWrite"))
		self.PbWrite.setAutoDefault(True)
		self.PbRead = QPushButton(self.PDcentralwidget)
		self.PbRead.setGeometry(QtCore.QRect(430, 80, 160, 31))
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(_fromUtf8("imgs/read.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.PbRead.setIcon(icon2)
		self.PbRead.setObjectName(_fromUtf8("PbRead"))
		self.PbClean = QPushButton(self.PDcentralwidget)
		self.PbClean.setGeometry(QtCore.QRect(430, 115, 160, 31))
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap(_fromUtf8("imgs/erase.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.PbClean.setIcon(icon3)
		self.PbClean.setObjectName(_fromUtf8("PbClean"))
		self.PbQuit = QPushButton(self.PDcentralwidget)
		self.PbQuit.setGeometry(QtCore.QRect(600, 10, 81, 101))
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap(_fromUtf8("imgs/quit.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.PbQuit.setIcon(icon4)
		self.PbQuit.setObjectName(_fromUtf8("PbQuit"))
		PDMainWindow.setCentralWidget(self.PDcentralwidget)

		self.retranslateUi(PDMainWindow)
		self.PDtabWidget.setCurrentIndex(0)
		
		try:
			#Field callbcaks
			QtCore.QObject.connect(self.LeOnuDproduto, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.LeOnuDataCheckWithOutAccent)
			QtCore.QObject.connect(self.LeOltDproduto, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.LeOltDataCheckWithOutAccent)
			QtCore.QObject.connect(self.LeSTM1Dproduto, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.LeSTM1DataCheckWithOutAccent)
			QtCore.QObject.connect(self.LeMSDDDproduto, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.LeMSDDDataCheckWithOutAccent)
			QtCore.QObject.connect(self.LeOltBladeDproduto, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.LeOltBladeDataCheckWithOutAccent)
			
			QtCore.QObject.connect(self.LeOnuTec, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.LeOnuTecCheckWithOutAccent)
			QtCore.QObject.connect(self.LeOltTec, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.LeOltTecCheckWithOutAccent)
			QtCore.QObject.connect(self.LeSTM1Tec, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.LeSTM1TecCheckWithOutAccent)
			QtCore.QObject.connect(self.LeMSDDTec, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.LeMSDDTecCheckWithOutAccent)
			QtCore.QObject.connect(self.LeOltBladeTec, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.LeOltBladeTecCheckWithOutAccent)
			
			QtCore.QObject.connect(self.LeOnuNpedido, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.LeOnuNpedidoCheckIfDigit)
			QtCore.QObject.connect(self.LeOnuNpedido, QtCore.SIGNAL(_fromUtf8("clicked()")), self.LeOnuNpedidoCheckEmptyness )
			QtCore.QObject.connect(self.LeOnuNpedido, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.LeOnuNpedidoCheckOrder)
			self.LeOnuNpedido.mousePressEvent = lambda _ : self.LeOnuNpedidoCheckEmptyness()
			
			QtCore.QObject.connect(self.LeOltNpedido, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.LeOltNpedidoCheckIfDigit)
			QtCore.QObject.connect(self.LeSTM1Npedido, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.LeSTM1NpedidoCheckIfDigit)
			QtCore.QObject.connect(self.LeMSDDNpedido, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.LeMSDDNpedidoCheckIfDigit)
			QtCore.QObject.connect(self.LeOltBladeNpedido, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.LeOltBladeNpedidoCheckIfDigit)
			
			#ComboBox Callback
			QtCore.QObject.connect(self.LaOnuLayer, QtCore.SIGNAL('activated(QString)'), self.checkIfL3)

			#Top Button/Field Callbacks
			QtCore.QObject.connect(self.LeCodbar, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.leCodeBarCheckIfDigit)
			QtCore.QObject.connect(self.LeCodbar, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.calculateBarCode)
			QtCore.QObject.connect(self.PbWrite, QtCore.SIGNAL(_fromUtf8("clicked()")), self.invGenerate)
			QtCore.QObject.connect(self.PbSend, QtCore.SIGNAL(_fromUtf8("clicked()")), self.invGenerateToSend)
			QtCore.QObject.connect(self.PbClean, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clearButton)
			QtCore.QObject.connect(self.PbRead, QtCore.SIGNAL(_fromUtf8("clicked()")), self.invRead)
			QtCore.QObject.connect(self.PbQuit, QtCore.SIGNAL(_fromUtf8("clicked()")), self.exitApp)
		except:
			self.LeOnuDproduto.textEdited.connect(self.LeOnuDataCheckWithOutAccent)
			self.LeOltDproduto.textEdited.connect(self.LeOltDataCheckWithOutAccent)
			self.LeSTM1Dproduto.textEdited.connect(self.LeSTM1DataCheckWithOutAccent)
			self.LeMSDDDproduto.textEdited.connect(self.LeMSDDDataCheckWithOutAccent)
			self.LeOltBladeDproduto.textEdited.connect(self.LeOltBladeDataCheckWithOutAccent)
			
			self.LeOnuTec.textEdited.connect(self.LeOnuTecCheckWithOutAccent)
			self.LeOltTec.textEdited.connect(self.LeOltTecCheckWithOutAccent)
			self.LeSTM1Tec.textEdited.connect(self.LeSTM1TecCheckWithOutAccent)
			self.LeMSDDTec.textEdited.connect(self.LeMSDDTecCheckWithOutAccent)
			self.LeOltBladeTec.textEdited.connect(self.LeOltBladeTecCheckWithOutAccent)
			
			self.LeOnuNpedido.textEdited.connect(self.LeOnuNpedidoCheckIfDigit)
			self.LeOnuNpedido.returnPressed.connect(self.LeOnuNpedidoCheckOrder)
			self.LeOnuNpedido.mousePressEvent = lambda _ : self.LeOnuNpedidoCheckEmptyness()
			
			self.LeOltNpedido.textEdited.connect(self.LeOltNpedidoCheckIfDigit)
			self.LeSTM1Npedido.textEdited.connect(self.LeSTM1NpedidoCheckIfDigit)
			self.LeMSDDNpedido.textEdited.connect(self.LeMSDDNpedidoCheckIfDigit)
			self.LeOltBladeNpedido.textEdited.connect(self.LeOltBladeNpedidoCheckIfDigit)
			
			self.LaOnuLayer.activated.connect(self.checkIfL3)
			
			self.LeCodbar.textEdited.connect(self.leCodeBarCheckIfDigit)
			self.LeCodbar.returnPressed.connect(self.calculateBarCode)
			self.PbWrite.clicked.connect(self.invGenerate)
			self.PbSend.clicked.connect(self.invGenerateToSend)
			self.PbClean.clicked.connect(self.clearButton)
			self.PbRead.clicked.connect(self.invRead)
			self.PbQuit.clicked.connect(self.exitApp)
		
		
		'activated(QString)'
		QtCore.QMetaObject.connectSlotsByName(PDMainWindow)
		
		PDMainWindow.setTabOrder(self.LeCodbar, 		self.LeOltNpedido)
		PDMainWindow.setTabOrder(self.LeOltNpedido, 	self.LeOltDproduto)
		PDMainWindow.setTabOrder(self.LeOltDproduto,	self.LeOltTec)
		PDMainWindow.setTabOrder(self.LeOltTec, 		self.LeOltVhw)
		PDMainWindow.setTabOrder(self.LeOltVhw, 		self.LeOltVfw)
		PDMainWindow.setTabOrder(self.LeOltVfw,			self.LeOltStartup)
		PDMainWindow.setTabOrder(self.LeOltStartup, 	self.LeOltSystem)
		PDMainWindow.setTabOrder(self.LeOltSystem, 		self.LeOltAsgos)
		PDMainWindow.setTabOrder(self.LeOltAsgos, 		self.LeOltResets)
		PDMainWindow.setTabOrder(self.LeOltResets, 		self.LaOnuLayer)
		PDMainWindow.setTabOrder(self.LeOnuNspon, 		self.LeOltData)
		PDMainWindow.setTabOrder(self.LeOltData, 		self.LeOltCprod)
		PDMainWindow.setTabOrder(self.LeOltCprod, 		self.LeOltNserie)
		PDMainWindow.setTabOrder(self.LeOltNserie, 		self.LeOltMac)
		PDMainWindow.setTabOrder(self.LeOltMac, 		self.LeSTM1Npedido)
		PDMainWindow.setTabOrder(self.LeSTM1Npedido,	self.LeSTM1Dproduto)
		PDMainWindow.setTabOrder(self.LeSTM1Dproduto,	self.LeSTM1Tec)
		PDMainWindow.setTabOrder(self.LeSTM1Tec, 		self.LeOltBladeNpedido)
		PDMainWindow.setTabOrder(self.LeOltBladeNpedido,self.LeOltBladeDproduto)
		PDMainWindow.setTabOrder(self.LeOltBladeDproduto,self.LeOltBladeTec)
		PDMainWindow.setTabOrder(self.LeOltBladeTec,	self.LeMSDDNpedido)
		PDMainWindow.setTabOrder(self.LeMSDDNpedido,	self.LeMSDDDproduto)
		PDMainWindow.setTabOrder(self.LeMSDDDproduto,	self.LeMSDDTec)
		PDMainWindow.setTabOrder(self.LeMSDDTec, 		self.LaOnuLayer)
		PDMainWindow.setTabOrder(self.LaOnuLayer, 		self.PbWrite)
		PDMainWindow.setTabOrder(self.PbWrite,			self.LeOnuMac)
		PDMainWindow.setTabOrder(self.LeOnuMac, 		self.LeOnuNpedido)
		PDMainWindow.setTabOrder(self.LeOnuNpedido, 	self.LeOnuResets)
		PDMainWindow.setTabOrder(self.LeOnuResets, 		self.LeOnuDproduto)
		PDMainWindow.setTabOrder(self.LeOnuDproduto,	self.LeOnuNserie)
		PDMainWindow.setTabOrder(self.LeOnuNserie, 		self.LeOnuSystem)
		PDMainWindow.setTabOrder(self.LeOnuSystem, 		self.LeOnuVhw)
		PDMainWindow.setTabOrder(self.LeOnuVhw, 		self.LeOnuVfw)
		PDMainWindow.setTabOrder(self.LeOnuVfw, 		self.LeOnuGtin)
		PDMainWindow.setTabOrder(self.LeOnuGtin, 		self.LeOnuCprod)
		PDMainWindow.setTabOrder(self.LeOnuCprod, 		self.LeOnuTec)
		PDMainWindow.setTabOrder(self.LeOnuTec, 		self.LeOnuData)
		PDMainWindow.setTabOrder(self.LeOnuData, 		self.LeOnuNspon)
		PDMainWindow.setTabOrder(self.LeOnuNspon, 		self.LeOltData)
		PDMainWindow.setTabOrder(self.LeOltData, 		self.PbRead)
		PDMainWindow.setTabOrder(self.PbRead, 			self.PbClean)
		PDMainWindow.setTabOrder(self.PbClean, 			self.PbQuit)
		
		#Starting tftp server
		self.PDMainWindow = PDMainWindow
		
	def retranslateUi(self, PDMainWindow):
		try:
			PDMainWindow.setWindowTitle(QApplication.translate("PDMainWindow", "XLightData 3.0.8", None, QApplication.UnicodeUTF8))
			self.GbOltVersoes.setTitle(QApplication.translate("PDMainWindow", "Versões", None, QApplication.UnicodeUTF8))
			self.LaOltVhw.setText(QApplication.translate("PDMainWindow", "Hardware:", None, QApplication.UnicodeUTF8))
			self.LaOltVfw.setText(QApplication.translate("PDMainWindow", "Firmware:", None, QApplication.UnicodeUTF8))
			self.GbOltSoftware.setTitle(QApplication.translate("PDMainWindow", "Pacotes de Software", None, QApplication.UnicodeUTF8))
			self.LaOltStartup.setText(QApplication.translate("PDMainWindow", "Startup:", None, QApplication.UnicodeUTF8))
			self.LaOltSystem.setText(QApplication.translate("PDMainWindow", "System:", None, QApplication.UnicodeUTF8))
			self.LaOltAsgos.setText(QApplication.translate("PDMainWindow", "AsGOS:", None, QApplication.UnicodeUTF8))
			self.LaOltMac.setText(QApplication.translate("PDMainWindow", "MAC:", None, QApplication.UnicodeUTF8))
			self.LaOltCprod.setText(QApplication.translate("PDMainWindow", "Código do produto:", None, QApplication.UnicodeUTF8))
			self.LaOltNserie.setText(QApplication.translate("PDMainWindow", "Número de Série:", None, QApplication.UnicodeUTF8))
			self.LaOltData.setText(QApplication.translate("PDMainWindow", "Data de Fabricação:", None, QApplication.UnicodeUTF8))
			self.LaOltNpedido.setText(QApplication.translate("PDMainWindow", "Numero do pedido:", None, QApplication.UnicodeUTF8))
			self.LaOltDproduto.setText(QApplication.translate("PDMainWindow", "Descrição do Produto:", None, QApplication.UnicodeUTF8))
			self.LaOltTec.setText(QApplication.translate("PDMainWindow", "Anotações Assist. Tec.:", None, QApplication.UnicodeUTF8))
			self.LaOltResets.setText(QApplication.translate("PDMainWindow", "Número de Resets:", None, QApplication.UnicodeUTF8))
			self.PDtabWidget.setTabText(self.PDtabWidget.indexOf(self.TabOlt), QApplication.translate("PDMainWindow", "OLT Inventory", None, QApplication.UnicodeUTF8))
			self.LaOnuData.setText(QApplication.translate("PDMainWindow", "Data de Fabricação:", None, QApplication.UnicodeUTF8))
			self.LaOnuMac.setText(QApplication.translate("PDMainWindow", "MAC:", None, QApplication.UnicodeUTF8))
			self.GbOnuSoftware.setTitle(QApplication.translate("PDMainWindow", "Pacotes de Software", None, QApplication.UnicodeUTF8))
			self.LaOnuSystem.setText(QApplication.translate("PDMainWindow", "System:", None, QApplication.UnicodeUTF8))
			self.GbOnuGtin.setTitle(QApplication.translate("PDMainWindow", "GTIN Cod Bar", None, QApplication.UnicodeUTF8))
			self.LaOnuGtin.setText(QApplication.translate("PDMainWindow", "GTIN:", None, QApplication.UnicodeUTF8))
			self.GbOnuVersoes.setTitle(QApplication.translate("PDMainWindow", "Versões", None, QApplication.UnicodeUTF8))
			self.LaOnuVhw.setText(QApplication.translate("PDMainWindow", "Hardware:", None, QApplication.UnicodeUTF8))
			self.LaOnuVfw.setText(QApplication.translate("PDMainWindow", "Firmware:", None, QApplication.UnicodeUTF8))
			self.LaOnuDproduto.setText(QApplication.translate("PDMainWindow", "Descrição do Produto:", None, QApplication.UnicodeUTF8))
			self.LaOnuTec.setText(QApplication.translate("PDMainWindow", "Anotações Assist. Tec.:", None, QApplication.UnicodeUTF8))
			self.LaOnuNserie.setText(QApplication.translate("PDMainWindow", "Número de Série:", None, QApplication.UnicodeUTF8))
			self.LaOnuNpedido.setText(QApplication.translate("PDMainWindow", "Numero do pedido:", None, QApplication.UnicodeUTF8))
			
			self.LaOnuStatusPVL2.setText(QApplication.translate("PDMainWindow", "ONU-HQ2*** (L2):", None, QApplication.UnicodeUTF8))
			self.LaOnuStatusPVL3Lite.setText(QApplication.translate("PDMainWindow", "ONU-JQ2*** (L3 Lite):", None, QApplication.UnicodeUTF8))
			self.LaOnuStatusPVL3Full.setText(QApplication.translate("PDMainWindow", "ONU-KQ2*** (L3 Full):", None, QApplication.UnicodeUTF8))
			
			self.LaOnuResets.setText(QApplication.translate("PDMainWindow", "Número de Resets:", None, QApplication.UnicodeUTF8))
			self.LaOnuCprod.setText(QApplication.translate("PDMainWindow", "Código do produto:", None, QApplication.UnicodeUTF8))
			self.LaOnuNspon.setText(QApplication.translate("PDMainWindow", "Número de Série PON:", None, QApplication.UnicodeUTF8))
			self.PDtabWidget.setTabText(self.PDtabWidget.indexOf(self.TabOnu), QApplication.translate("PDMainWindow", "ONU inventory", None, QApplication.UnicodeUTF8))
			self.LaSTM1Tec.setText(QApplication.translate("PDMainWindow", "Anotações Assist. Tec.:", None,QApplication.UnicodeUTF8))
			self.LaSTM1Nserie.setText(QApplication.translate("PDMainWindow", "Número de Série:", None,QApplication.UnicodeUTF8))
			self.LaSTM1Cprod.setText(QApplication.translate("PDMainWindow", "Código do produto:", None, QApplication.UnicodeUTF8))
			self.GbSTM1Versoes.setTitle(QApplication.translate("PDMainWindow", "Versões", None, QApplication.UnicodeUTF8))
			self.LaSTM1Vhw.setText(QApplication.translate("PDMainWindow", "Hardware:", None, QApplication.UnicodeUTF8))
			self.LaSTM1Vfw.setText(QApplication.translate("PDMainWindow", "Firmware:", None, QApplication.UnicodeUTF8))
			self.LaSTM1Data.setText(QApplication.translate("PDMainWindow", "Data de Fabricação:", None, QApplication.UnicodeUTF8))
			self.LaSTM1Npedido.setText(QApplication.translate("PDMainWindow", "Numero do pedido:", None, QApplication.UnicodeUTF8))
			self.LaSTM1Resets.setText(QApplication.translate("PDMainWindow", "Número de Resets:", None, QApplication.UnicodeUTF8))
			self.LaSTM1Dproduto.setText(QApplication.translate("PDMainWindow", "Descrição do Produto:", None, QApplication.UnicodeUTF8))
			self.PDtabWidget.setTabText(self.PDtabWidget.indexOf(self.TabSTM1GW), QApplication.translate("PDMainWindow", "STM1-GW", None, QApplication.UnicodeUTF8))
			self.GbOltBladeVersoes.setTitle(QApplication.translate("PDMainWindow", "Versões", None, QApplication.UnicodeUTF8))
			self.LaOltBladeVhw.setText(QApplication.translate("PDMainWindow", "Hardware:", None, QApplication.UnicodeUTF8))
			self.LaOltBladeVfw.setText(QApplication.translate("PDMainWindow", "Firmware:", None, QApplication.UnicodeUTF8))
			self.GbOltBladeSoftware.setTitle(QApplication.translate("PDMainWindow", "Pacotes de Software", None, QApplication.UnicodeUTF8))
			self.LaOltBladeStartup.setText(QApplication.translate("PDMainWindow", "Startup:", None, QApplication.UnicodeUTF8))
			self.LaOltBladeSystem.setText(QApplication.translate("PDMainWindow", "System:", None, QApplication.UnicodeUTF8))
			self.LaOltBladeAsgos.setText(QApplication.translate("PDMainWindow", "AsGOS:", None, QApplication.UnicodeUTF8))
			self.LaOltBladeMac.setText(QApplication.translate("PDMainWindow", "MAC:", None, QApplication.UnicodeUTF8))
			self.LaOltBladeCprod.setText(QApplication.translate("PDMainWindow", "Código do produto:", None, QApplication.UnicodeUTF8))
			self.LaOltBladeNserie.setText(QApplication.translate("PDMainWindow", "Número de Série:", None, QApplication.UnicodeUTF8))
			self.LaOltBladeData.setText(QApplication.translate("PDMainWindow", "Data de Fabricação:", None, QApplication.UnicodeUTF8))
			self.LaOltBladeNpedido.setText(QApplication.translate("PDMainWindow", "Numero do pedido:", None, QApplication.UnicodeUTF8))
			self.LaOltBladeDproduto.setText(QApplication.translate("PDMainWindow", "Descrição do Produto:", None, QApplication.UnicodeUTF8))
			self.LaOltBladeTec.setText(QApplication.translate("PDMainWindow", "Anotações Assist. Tec.:", None, QApplication.UnicodeUTF8))
			self.LaOltBladeResets.setText(QApplication.translate("PDMainWindow", "Número de Resets:", None, QApplication.UnicodeUTF8))
			self.PDtabWidget.setTabText(self.PDtabWidget.indexOf(self.TabOltBlade), QApplication.translate("PDMainWindow", "OLT Blade inventory", None, QApplication.UnicodeUTF8))
			self.LaMSDDData.setText(QApplication.translate("PDMainWindow", "Data de Fabricação:", None, QApplication.UnicodeUTF8))
			self.LaMSDDMac.setText(QApplication.translate("PDMainWindow", "MAC:", None, QApplication.UnicodeUTF8))
			self.GbMSDDSoftware.setTitle(QApplication.translate("PDMainWindow", "Pacotes de Software", None, QApplication.UnicodeUTF8))
			self.LaMSDDSystem.setText(QApplication.translate("PDMainWindow", "System:", None, QApplication.UnicodeUTF8))
			self.GbMSDDVersoes.setTitle(QApplication.translate("PDMainWindow", "Versões", None, QApplication.UnicodeUTF8))
			self.LaMSDDVhw.setText(QApplication.translate("PDMainWindow", "Hardware:", None, QApplication.UnicodeUTF8))
			self.LaMSDDVfw.setText(QApplication.translate("PDMainWindow", "Firmware:", None, QApplication.UnicodeUTF8))
			self.LaMSDDDproduto.setText(QApplication.translate("PDMainWindow", "Descrição do Produto:", None, QApplication.UnicodeUTF8))
			self.LaMSDDTec.setText(QApplication.translate("PDMainWindow", "Anotações Assist. Tec.:", None, QApplication.UnicodeUTF8))
			self.LaMSDDNserie.setText(QApplication.translate("PDMainWindow", "Número de Série:", None, QApplication.UnicodeUTF8))
			self.LaMSDDNpedido.setText(QApplication.translate("PDMainWindow", "Numero do pedido:", None, QApplication.UnicodeUTF8))
			self.LaMSDDResets.setText(QApplication.translate("PDMainWindow", "Número de Resets:", None, QApplication.UnicodeUTF8))
			self.LaMSDDCprod.setText(QApplication.translate("PDMainWindow", "Código do produto:", None, QApplication.UnicodeUTF8))
			self.LaMSDDNspon.setText(QApplication.translate("PDMainWindow", "Número de Série PON:", None, QApplication.UnicodeUTF8))
			self.PDtabWidget.setTabText(self.PDtabWidget.indexOf(self.TabMSDD), QApplication.translate("PDMainWindow", "MSDD inventory", None, QApplication.UnicodeUTF8))
			self.LaOltMapleModel.setText(QApplication.translate("PDMainWindow", "OLT Model:", None, QApplication.UnicodeUTF8))
			self.LaOltMapleMac.setText(QApplication.translate("PDMainWindow", "MAC:", None, QApplication.UnicodeUTF8))
			self.LaOltMapleCprod.setText(QApplication.translate("PDMainWindow", "Código do produto:", None, QApplication.UnicodeUTF8))
			self.LaOltMapleNserie.setText(QApplication.translate("PDMainWindow", "Número de Série:", None, QApplication.UnicodeUTF8))
			self.LaOltMapleData.setText(QApplication.translate("PDMainWindow", "Data de Fabricação:", None, QApplication.UnicodeUTF8))
			self.PDtabWidget.setTabText(self.PDtabWidget.indexOf(self.TabOltMaple), QApplication.translate("PDMainWindow", "OLT Maple Inventory", None, QApplication.UnicodeUTF8))
			self.LaCodBar.setText(QApplication.translate("PDMainWindow", "Código de Barras:", None, QApplication.UnicodeUTF8))
			self.PbWrite.setText(QApplication.translate("PDMainWindow", "Gerar Inventário", None, QApplication.UnicodeUTF8))
			self.PbSend.setText(QApplication.translate("PDMainWindow", "Enviar Inventário", None, QApplication.UnicodeUTF8))
			self.PbRead.setText(QApplication.translate("PDMainWindow", "Ler Inventário", None, QApplication.UnicodeUTF8))
			self.PbClean.setText(QApplication.translate("PDMainWindow", "Resetar Campos", None, QApplication.UnicodeUTF8))
			self.PbQuit.setText(QApplication.translate("PDMainWindow", "Sair", None, QApplication.UnicodeUTF8))
		except:
			PDMainWindow.setWindowTitle(QApplication.translate("PDMainWindow", "XLightData 3.0.8", None, 0))
			self.GbOltVersoes.setTitle(QApplication.translate("PDMainWindow", "Versões", None, 0))
			self.LaOltVhw.setText(QApplication.translate("PDMainWindow", "Hardware:", None, 0))
			self.LaOltVfw.setText(QApplication.translate("PDMainWindow", "Firmware:", None, 0))
			self.GbOltSoftware.setTitle(QApplication.translate("PDMainWindow", "Pacotes de Software", None, 0))
			self.LaOltStartup.setText(QApplication.translate("PDMainWindow", "Startup:", None, 0))
			self.LaOltSystem.setText(QApplication.translate("PDMainWindow", "System:", None, 0))
			self.LaOltAsgos.setText(QApplication.translate("PDMainWindow", "AsGOS:", None, 0))
			self.LaOltMac.setText(QApplication.translate("PDMainWindow", "MAC:", None, 0))
			self.LaOltCprod.setText(QApplication.translate("PDMainWindow", "Código do produto:", None, 0))
			self.LaOltNserie.setText(QApplication.translate("PDMainWindow", "Número de Série:", None, 0))
			self.LaOltData.setText(QApplication.translate("PDMainWindow", "Data de Fabricação:", None, 0))
			self.LaOltNpedido.setText(QApplication.translate("PDMainWindow", "Numero do pedido:", None, 0))
			self.LaOltDproduto.setText(QApplication.translate("PDMainWindow", "Descrição do Produto:", None, 0))
			self.LaOltTec.setText(QApplication.translate("PDMainWindow", "Anotações Assist. Tec.:", None, 0))
			self.LaOltResets.setText(QApplication.translate("PDMainWindow", "Número de Resets:", None, 0))
			self.PDtabWidget.setTabText(self.PDtabWidget.indexOf(self.TabOlt), QApplication.translate("PDMainWindow", "OLT Inventory", None, 0))
			self.LaOnuData.setText(QApplication.translate("PDMainWindow", "Data de Fabricação:", None, 0))
			self.LaOnuMac.setText(QApplication.translate("PDMainWindow", "MAC:", None, 0))
			self.GbOnuSoftware.setTitle(QApplication.translate("PDMainWindow", "Pacotes de Software", None, 0))
			self.LaOnuSystem.setText(QApplication.translate("PDMainWindow", "System:", None, 0))
			self.GbOnuGtin.setTitle(QApplication.translate("PDMainWindow", "GTIN Cod Bar", None, 0))
			self.LaOnuGtin.setText(QApplication.translate("PDMainWindow", "GTIN:", None, 0))
			self.GbOnuVersoes.setTitle(QApplication.translate("PDMainWindow", "Versões", None, 0))
			self.LaOnuVhw.setText(QApplication.translate("PDMainWindow", "Hardware:", None, 0))
			self.LaOnuVfw.setText(QApplication.translate("PDMainWindow", "Firmware:", None, 0))
			self.LaOnuDproduto.setText(QApplication.translate("PDMainWindow", "Descrição do Produto:", None, 0))
			self.LaOnuTec.setText(QApplication.translate("PDMainWindow", "Anotações Assist. Tec.:", None, 0))
			self.LaOnuNserie.setText(QApplication.translate("PDMainWindow", "Número de Série:", None, 0))
			self.LaOnuNpedido.setText(QApplication.translate("PDMainWindow", "Numero do pedido:", None, 0))
			
			self.LaOnuStatusPVL2.setText(QApplication.translate("PDMainWindow", "ONU-HQ2*** (L2):", None, 0))
			self.LaOnuStatusPVL3Lite.setText(QApplication.translate("PDMainWindow", "ONU-JQ2*** (L3 Lite):", None, 0))
			self.LaOnuStatusPVL3Full.setText(QApplication.translate("PDMainWindow", "ONU-KQ2*** (L3 Full):", None, 0))
			
			self.LaOnuResets.setText(QApplication.translate("PDMainWindow", "Número de Resets:", None, 0))
			self.LaOnuCprod.setText(QApplication.translate("PDMainWindow", "Código do produto:", None, 0))
			self.LaOnuNspon.setText(QApplication.translate("PDMainWindow", "Número de Série PON:", None, 0))
			self.PDtabWidget.setTabText(self.PDtabWidget.indexOf(self.TabOnu), QApplication.translate("PDMainWindow", "ONU inventory", None, 0))
			self.LaSTM1Tec.setText(QApplication.translate("PDMainWindow", "Anotações Assist. Tec.:", None,0))
			self.LaSTM1Nserie.setText(QApplication.translate("PDMainWindow", "Número de Série:", None,0))
			self.LaSTM1Cprod.setText(QApplication.translate("PDMainWindow", "Código do produto:", None, 0))
			self.GbSTM1Versoes.setTitle(QApplication.translate("PDMainWindow", "Versões", None, 0))
			self.LaSTM1Vhw.setText(QApplication.translate("PDMainWindow", "Hardware:", None, 0))
			self.LaSTM1Vfw.setText(QApplication.translate("PDMainWindow", "Firmware:", None, 0))
			self.LaSTM1Data.setText(QApplication.translate("PDMainWindow", "Data de Fabricação:", None, 0))
			self.LaSTM1Npedido.setText(QApplication.translate("PDMainWindow", "Numero do pedido:", None, 0))
			self.LaSTM1Resets.setText(QApplication.translate("PDMainWindow", "Número de Resets:", None, 0))
			self.LaSTM1Dproduto.setText(QApplication.translate("PDMainWindow", "Descrição do Produto:", None, 0))
			self.PDtabWidget.setTabText(self.PDtabWidget.indexOf(self.TabSTM1GW), QApplication.translate("PDMainWindow", "STM1-GW", None, 0))
			self.GbOltBladeVersoes.setTitle(QApplication.translate("PDMainWindow", "Versões", None, 0))
			self.LaOltBladeVhw.setText(QApplication.translate("PDMainWindow", "Hardware:", None, 0))
			self.LaOltBladeVfw.setText(QApplication.translate("PDMainWindow", "Firmware:", None, 0))
			self.GbOltBladeSoftware.setTitle(QApplication.translate("PDMainWindow", "Pacotes de Software", None, 0))
			self.LaOltBladeStartup.setText(QApplication.translate("PDMainWindow", "Startup:", None, 0))
			self.LaOltBladeSystem.setText(QApplication.translate("PDMainWindow", "System:", None, 0))
			self.LaOltBladeAsgos.setText(QApplication.translate("PDMainWindow", "AsGOS:", None, 0))
			self.LaOltBladeMac.setText(QApplication.translate("PDMainWindow", "MAC:", None, 0))
			self.LaOltBladeCprod.setText(QApplication.translate("PDMainWindow", "Código do produto:", None, 0))
			self.LaOltBladeNserie.setText(QApplication.translate("PDMainWindow", "Número de Série:", None, 0))
			self.LaOltBladeData.setText(QApplication.translate("PDMainWindow", "Data de Fabricação:", None, 0))
			self.LaOltBladeNpedido.setText(QApplication.translate("PDMainWindow", "Numero do pedido:", None, 0))
			self.LaOltBladeDproduto.setText(QApplication.translate("PDMainWindow", "Descrição do Produto:", None, 0))
			self.LaOltBladeTec.setText(QApplication.translate("PDMainWindow", "Anotações Assist. Tec.:", None, 0))
			self.LaOltBladeResets.setText(QApplication.translate("PDMainWindow", "Número de Resets:", None, 0))
			self.PDtabWidget.setTabText(self.PDtabWidget.indexOf(self.TabOltBlade), QApplication.translate("PDMainWindow", "OLT Blade inventory", None, 0))
			self.LaMSDDData.setText(QApplication.translate("PDMainWindow", "Data de Fabricação:", None, 0))
			self.LaMSDDMac.setText(QApplication.translate("PDMainWindow", "MAC:", None, 0))
			self.GbMSDDSoftware.setTitle(QApplication.translate("PDMainWindow", "Pacotes de Software", None, 0))
			self.LaMSDDSystem.setText(QApplication.translate("PDMainWindow", "System:", None, 0))
			self.GbMSDDVersoes.setTitle(QApplication.translate("PDMainWindow", "Versões", None, 0))
			self.LaMSDDVhw.setText(QApplication.translate("PDMainWindow", "Hardware:", None, 0))
			self.LaMSDDVfw.setText(QApplication.translate("PDMainWindow", "Firmware:", None, 0))
			self.LaMSDDDproduto.setText(QApplication.translate("PDMainWindow", "Descrição do Produto:", None, 0))
			self.LaMSDDTec.setText(QApplication.translate("PDMainWindow", "Anotações Assist. Tec.:", None, 0))
			self.LaMSDDNserie.setText(QApplication.translate("PDMainWindow", "Número de Série:", None, 0))
			self.LaMSDDNpedido.setText(QApplication.translate("PDMainWindow", "Numero do pedido:", None, 0))
			self.LaMSDDResets.setText(QApplication.translate("PDMainWindow", "Número de Resets:", None, 0))
			self.LaMSDDCprod.setText(QApplication.translate("PDMainWindow", "Código do produto:", None, 0))
			self.LaMSDDNspon.setText(QApplication.translate("PDMainWindow", "Número de Série PON:", None, 0))
			self.PDtabWidget.setTabText(self.PDtabWidget.indexOf(self.TabMSDD), QApplication.translate("PDMainWindow", "MSDD inventory", None, 0))
			self.LaOltMapleModel.setText(QApplication.translate("PDMainWindow", "OLT Model:", None, 0))
			self.LaOltMapleMac.setText(QApplication.translate("PDMainWindow", "MAC:", None, 0))
			self.LaOltMapleCprod.setText(QApplication.translate("PDMainWindow", "Código do produto:", None, 0))
			self.LaOltMapleNserie.setText(QApplication.translate("PDMainWindow", "Número de Série:", None, 0))
			self.LaOltMapleData.setText(QApplication.translate("PDMainWindow", "Data de Fabricação:", None, 0))
			self.PDtabWidget.setTabText(self.PDtabWidget.indexOf(self.TabOltMaple), QApplication.translate("PDMainWindow", "OLT Maple Inventory", None, 0))
			self.LaCodBar.setText(QApplication.translate("PDMainWindow", "Código de Barras:", None, 0))
			self.PbWrite.setText(QApplication.translate("PDMainWindow", "Gerar Inventário", None, 0))
			self.PbSend.setText(QApplication.translate("PDMainWindow", "Enviar Inventário", None, 0))
			self.PbRead.setText(QApplication.translate("PDMainWindow", "Ler Inventário", None, 0))
			self.PbClean.setText(QApplication.translate("PDMainWindow", "Resetar Campos", None, 0))
			self.PbQuit.setText(QApplication.translate("PDMainWindow", "Sair", None, 0))
	

	def removeInvFile(self):
		try:
			os.remove("tftpboot/oltinv.cpt")
		except:
			pass

		try:
			os.remove("tftpboot/oltinv")
		except:
			pass
			
		try:
			os.remove("tftpboot/onuinv.cpt")
		except:
			pass

		try:
			os.remove("tftpboot/onuinv")
		except:
			pass

		try:
			os.remove("tftpboot/stm1inv.cpt")
		except:
			pass

		try:
			os.remove("tftpboot/stm1inv")
		except:
			pass

		try:
			os.remove("tftpboot/oltbladeinv.cpt")
		except:
			pass

		try:
			os.remove("tftpboot/oltbladeinv")
		except:
			pass

		try:
			os.remove("tftpboot/msddinv.cpt")
		except:
			pass

		try:
			os.remove("tftpboot/msddinv")
		except:
			pass


	def exitApp(self):
		self.removeInvFile()
		self.PDMainWindow.close()

	def showInformDialog(self, InfoString):
		Dialog =  QDialog()
		u = Ui_FInform()
		u.setupUi(Dialog, InfoString)
		Dialog.exec_()

	def showErroDialog(self, InfoString):
		Dialog =  QDialog()
		u = Ui_FErro()
		u.setupUi(Dialog, InfoString)
		Dialog.exec_()

	def showAcceptDialog(self, InfoString):
		Dialog =  QDialog()
		u = Ui_FAccept()
		u.setupUi(Dialog, InfoString)
		Dialog.exec_()
		
	def formSalesOrder(self, sOrder):
		form = SalesOrder(sOrder)
		form.exec_()
	
	def clearButton(self):
		self.clearFields('all')
		self.removeInvFile()

	def clearFields(self, typeClean):
		if typeClean == 'all':
			self.LeCodbar.clear()
			self.LeOnuNpedido.clear()
			
		#Cleaning OLT fields
		self.LeOltMac.clear()
		self.LeOltCprod.clear()
		self.LeOltNserie.clear()
		self.LeOltData.clear()
		self.LeOltDproduto.clear()
		self.LeOltNpedido.clear()
		self.LeOltTec.clear()
		self.LeOltResets.clear()
		self.LeOltVhw.clear()
		self.LeOltVfw.clear()
		self.LeOltSystem.clear()
		self.LeOltAsgos.clear()
		self.LeOltStartup.clear()
		
		#Cleaning ONU fields
		try:
			codbarMidText = self.LeCodbar.text().mid(10,5)
		except:
			codbarMidText = self.LeCodbar.text()[9:14]
			
		if (codbarMidText != '61392' or codbarMidText != '80273' or codbarMidText != '80274'):
			self.LeOnuNpedido.clear()
			self.LaOnuLayer.setHidden(True)
		self.LeOnuMac.clear()
		self.LeOnuCprod.clear()
		self.LeOnuNserie.clear()
		self.LeOnuNspon.clear()
		self.LeOnuData.clear()
		self.LeOnuDproduto.clear()
		self.LeOnuTec.clear()
		self.LeOnuResets.clear()
		self.LeOnuVhw.clear()
		self.LeOnuVfw.clear()
		self.LeOnuSystem.clear()
		self.LeOnuGtin.clear()
		self.LaOnuStatusPVL2.setHidden(True)
		self.LbOnuStatusPVL2.setHidden(True)
		self.LaOnuStatusPVL3Lite.setHidden(True)
		self.LbOnuStatusPVL3Lite.setHidden(True)
		self.LaOnuStatusPVL3Full.setHidden(True)
		self.LbOnuStatusPVL3Full.setHidden(True)
# 		self.LaOnuLayer.setCurrentIndex(0)
		
		#Cleaning STM1 fields
		self.LeSTM1Cprod.clear()
		self.LeSTM1Nserie.clear()
		self.LeSTM1Data.clear()
		self.LeSTM1Npedido.clear()
		self.LeSTM1Dproduto.clear()
		self.LeSTM1Tec.clear()
		self.LeSTM1Resets.clear()
		self.LeSTM1Vhw.clear()
		self.LeSTM1Vfw.clear()
		
		#Cleaning OLT Blade fields
		self.LeOltBladeMac.clear()
		self.LeOltBladeCprod.clear()
		self.LeOltBladeNserie.clear()
		self.LeOltBladeData.clear()		
		self.LeOltBladeNpedido.clear()
		self.LeOltBladeDproduto.clear()
		self.LeOltBladeTec.clear()
		self.LeOltBladeResets.clear()
		self.LeOltBladeVhw.clear()
		self.LeOltBladeVfw.clear()
		self.LeOltBladeSystem.clear()
		self.LeOltBladeAsgos.clear()
		self.LeOltBladeStartup.clear()
		
		#Cleaning ONU fields
		self.LeMSDDMac.clear()
		self.LeMSDDCprod.clear()
		self.LeMSDDNserie.clear()
		self.LeMSDDNspon.clear()
		self.LeMSDDData.clear()
		self.LeMSDDNpedido.clear()
		self.LeMSDDDproduto.clear()
		self.LeMSDDTec.clear()
		self.LeMSDDResets.clear()
		self.LeMSDDVhw.clear()
		self.LeMSDDVfw.clear()
		self.LeMSDDSystem.clear()

		#Cleaning OLT Maple fields
		self.LeOltMapleModel.clear()
		self.LeOltMapleMac.clear()
		self.LeOltMapleCprod.clear()
		self.LeOltMapleNserie.clear()
		self.LeOltMapleData.clear()	

		self.PbWrite.setEnabled(True)
		self.PbRead.setEnabled(True)
		self.PbSend.setEnabled(False)
		
	def invGenerate(self):
		self.removeInvFile()
		gfile = invfile()

		#Verify for ONU with multiple licenses, if ther is any of them checked (L2, L3 Lite or L3 Full)
		#  name          					PCode
		# ONU LD 582 L2+ L3Lite+ L3Full	(DEFINITIVO)	61392
		#----------------------------------------
		# ONU LD 581 L2+L3 	(Fictício)		00033
		'''FIXME: colocar códigos corretos'''
		
		flag_newOrder = False
		flag_OrderCompleted = False
		
		if (self.LeOnuCprod.text() == '61392' or self.LeOnuCprod.text() == '00033'
			or self.LeOnuCprod.text() == '80273' or self.LeOnuCprod.text() == '80274'):
			if str(self.LeOnuNpedido.text()) == '' or str(self.LeOnuNpedido.text()) == "Digite Pedido..." :
				self.LeOnuNpedido.setStyleSheet("color: rgb(200, 0, 0);")
				self.LeOnuNpedido.setText(QApplication.translate("PDMainWindow", "Digite Pedido...", None, QApplication.UnicodeUTF8))
				self.showInformDialog('Impossivel gravar inventario. Introduza Pedido de Venda')
				return None
			if int(self.LeOnuNpedido.text()) > 65535:
				self.showInformDialog('Aviso: Pedido de Venda deverá ser menor que 65535')
				return None
			try:
				f = open(orders_path + str(self.LeOnuNpedido.text()), 'r') 
			except:
				self.formSalesOrder(self.LeOnuNpedido.text())
				try:
					f = open(orders_path + str(self.LeOnuNpedido.text()), 'r')
					flag_newOrder = True;
				except:
					self.showInformDialog('Impossivel abrir arquivo de Pedido de Venda '+ str(self.LeOnuNpedido.text()))
					return None 
			
			#Apresenta estado do pedido de venda:
			lineL2 = f.readline()
			lineL3Lite = f.readline()
			lineL3Full = f.readline()
			f.close()
			lineL2 = lineL2.split()
			lineL3Lite = lineL3Lite.split()
			lineL3Full = lineL3Full.split()
			self.producedL2 = lineL2[2]
			self.totalL2 = lineL2[3]
			self.producedL3Lite = lineL3Lite[3]
			self.totalL3Lite = lineL3Lite[4]
			self.producedL3Full = lineL3Full[3]
			self.totalL3Full = lineL3Full[4]
			self.LaOnuStatusPVL2.setHidden(False)
			self.LbOnuStatusPVL2.setHidden(False)
			self.LaOnuStatusPVL3Lite.setHidden(False)
			self.LbOnuStatusPVL3Lite.setHidden(False)
			self.LaOnuStatusPVL3Full.setHidden(False)
			self.LbOnuStatusPVL3Full.setHidden(False)
			self.LbOnuStatusPVL2.setText(str(self.producedL2 + "/" + self.totalL2))
			self.LbOnuStatusPVL3Lite.setText(str(self.producedL3Lite + "/" + self.totalL3Lite))
			self.LbOnuStatusPVL3Full.setText(str(self.producedL3Full + "/" + self.totalL3Full))
			
			#Após introduzir o pedido de venda PELA PRIMEIRA VEZ, não segue com a criação do inventário.
			if flag_newOrder == True :
				return None
			
			if self.LaOnuLayer.currentIndex() == 0 :
				self.showInformDialog('Impossivel gravar inventario. Escolha o produto..')
				return None
			
			if self.LaOnuLayer.currentIndex() == 1:
				if self.producedL2 == self.totalL2:
					self.showInformDialog('Produzidas ' +self.producedL2 + '/' + self.totalL2 + ' ONU-HQ2*** (L2) ')
					flag_OrderCompleted = True
				else:
					self.producedL2 = str( int( self.producedL2 ) + 1 )
					
			if self.LaOnuLayer.currentIndex() == 2:
				if self.producedL3Lite == self.totalL3Lite:
					self.showInformDialog('Produzidas ' +self.producedL3Lite + '/' + self.totalL3Lite + ' ONU-JQ2*** (L3 Lite) ')
					flag_OrderCompleted = True
				else:
					self.producedL3Lite = str( int( self.producedL3Lite ) + 1 )
					
			elif self.LaOnuLayer.currentIndex() == 3:
				if self.producedL3Full == self.totalL3Full:
					self.showInformDialog('Produzidas ' +self.producedL3Full + '/' + self.totalL3Full + ' ONU-KQ2*** (L3 Full) ')
					flag_OrderCompleted = True
				else:
					self.producedL3Full = str( int( self.producedL3Full ) + 1 )
			
		else:
			self.LaOnuStatusPVL2.setHidden(True)
			self.LbOnuStatusPVL2.setHidden(True)
			self.LaOnuStatusPVL3Lite.setHidden(True)
			self.LbOnuStatusPVL3Lite.setHidden(True)	
			self.LaOnuStatusPVL3Full.setHidden(True)
			self.LbOnuStatusPVL3Full.setHidden(True)
		
		#  name          PCode
		#OLT 2502 	 26676 7899936802597 7899936802603 7899936802627
		#OLT 2504 	 26677 7899936802771
		#OLT FIT  	 61952 7899936802610
		if (self.LeOltCprod.text() == '26676' or self.LeOltCprod.text() == '26677' 
		    or  self.LeOltCprod.text() == '61952' or  self.LeOltCprod.text() == '80259'
		    or  self.LeOltCprod.text() == '80260' or  self.LeOltCprod.text() == '80262' 
		    or  self.LeOltCprod.text() == '80277' or  self.LeOltCprod.text() == '80261'):
			if str(self.LeOltMac.text()).__len__() == 0:
				self.showInformDialog('Impossivel gravar inventario. Falta mac-address')
				return None
			gfile.olt(self)
		
		#  name          					PCode
		# ONU 500 - Fitec 					18094
		# ONU 500 PC 	 					27772
		# ONU 500 APC	 					56254
		# ONU 500S APC	 					55982
		# ONU 500S PC	 					58938
		# ONU 500V	 						56109
		# ONU 1600 PC	 					55980 7899936802757
		# ONU 1600 APC	 					57107
		# ONU LD 582 L2+L3 Lite+ L3 Full 	61392
		# ONU LD 1180						62441
		# ONU LD 1182						62439
		# ONU LD 1182-W						61728
		# ONU LD 1182-V						62445
		# ONU LD 1182-Y						62620
		# ONU LD 1182-WV					62448
		# ONU LD 1182-WY					62450
		#----------------------------------------
		# MSDD		  		(Fictício)		00022
		# ONU LD 581 L2+L3 	(Fictício)		00033
		
		
			
			
			'''FIXME: colocar códigos corretos'''
		elif ( self.LeOnuCprod.text() == '27772' or self.LeOnuCprod.text() == '18094' 
			or self.LeOnuCprod.text() == '56254' or self.LeOnuCprod.text() == '55982' 
			or self.LeOnuCprod.text() == '58938' or self.LeOnuCprod.text() == '56109' 
			or self.LeOnuCprod.text() == '55980' or self.LeOnuCprod.text() == '57107'
			or self.LeOnuCprod.text() == '61392' or self.LeOnuCprod.text() == '62441' 
			or self.LeOnuCprod.text() == '62439' or self.LeOnuCprod.text() == '61728' 
			or self.LeOnuCprod.text() == '62445' or self.LeOnuCprod.text() == '62620' 
			or self.LeOnuCprod.text() == '62448' or self.LeOnuCprod.text() == '62450' 
			or self.LeOnuCprod.text() == '00033' or self.LeOnuCprod.text() == '80275'
			or self.LeOnuCprod.text() == '80273' or self.LeOnuCprod.text() == '80274'):
			if str(self.LeOnuMac.text()).__len__() == 0:
				self.showInformDialog('Impossivel gravar inventario. Falta mac-address')
				return None

			#Insert firmware info, into Chronos
			if (self.LeOnuCprod.text() == '61392' or self.LeOnuCprod.text() == '80273'
				or self.LeOnuCprod.text() == '80274'):
				mac = MAC()
				
				#Verify if this is the first enterance at chronos, for this MAC
				firm = mac.getFirmware_chronos(self.LeCodbar.text())
				if firm == None and flag_OrderCompleted == False:
					file = open(orders_path + str(self.LeOnuNpedido.text()), 'w+')
					file.write("ONU-HQ2*** (L2): " + self.producedL2 + ' ' + self.totalL2 + " \n")
					file.write("ONU-JQ2*** (L3 Lite): " + self.producedL3Lite + ' ' + self.totalL3Lite + " \n")
					file.write("ONU-KQ2*** (L3 Full): " + self.producedL3Full + ' ' + self.totalL3Full + " \n")
					file.close()
				
					mac.insertEAN_chronos(self.LeCodbar.text(), self.LaOnuLayer.currentIndex()-1)
					firm = mac.getFirmware_chronos(self.LeCodbar.text())
					if firm == None:
						self.showInformDialog("Impossivel inserir entrada no Chronos")
				
					#Atualiza o campo de status do pedido de venda	
					self.LbOnuStatusPVL2.setText(str(self.producedL2 + "/" + self.totalL2))
					self.LbOnuStatusPVL3Lite.setText(str(self.producedL3Lite + "/" + self.totalL3Lite))
					self.LbOnuStatusPVL3Full.setText(str(self.producedL3Full + "/" + self.totalL3Full))
					
			gfile.onu(self)
			self.LeCodbar.selectAll()
			self.LeCodbar.setFocus()
			
		#NEW ONUs
		elif (self.LeOnuGtin.text() == '7899936800050' or self.LeOnuGtin.text() == '7899936002782'
			or self.LeOnuGtin.text() == '7899936802665' or self.LeOnuGtin.text() == '7899936006063'
			or self.LeOnuGtin.text() == '7899936000610' or self.LeOnuGtin.text() == '7899936006865'
			or self.LeOnuGtin.text() == '7893137299699'):
			if str(self.LeOnuMac.text()).__len__() == 0:
				self.showInformDialog('Impossivel gravar inventario. Falta mac-address')
				return None	
			
			gfile.newonu(self)
			self.LeCodbar.selectAll()
			self.LeCodbar.setFocus()
			
		#  name         PCode
		#STM1-GW		28110
		elif  self.LeSTM1Cprod.text() == '28110':
			gfile.stm1(self)
		
		#  name         PCode
		#OLT BLADE	 	000011 (Fictício)
			'''FIXME: colocar códigos corretos'''
		elif self.LeOltBladeCprod.text() == '00011':
			if str(self.LeOltBladeMac.text()).__len__() == 0:
				self.showInformDialog('Impossivel gravar inventario. Falta mac-address')
				return None
			gfile.oltblade(self)
		
		#  name         PCode
		#MSDD	 		000022 (Fictício)
			'''FIXME: colocar códigos corretos'''
		elif self.LeMSDDCprod.text() == '00022':
			if str(self.LeMSDDMac.text()).__len__() == 0:
				self.showInformDialog('Impossivel gravar inventario. Falta mac-address')
				return None
			gfile.msdd(self)

	def invGenerateToSend(self):
		gSend = invSend()
		#  name         PCode
		# OLT MAPLE 3516 		            7899936006131
		# OLT MAPLE 3508 		           	7893137283605
		if (self.LeOltMapleCprod.text() == '7899936006131' or self.LeOltMapleCprod.text() == '7893137283605'):
			if str(self.LeOltMapleMac.text()).__len__() == 0:
				self.showInformDialog('Impossivel gravar inventario. Falta mac-address')
				return None
		retStr = gSend.oltMaple(self)
		if retStr[0] == 'S':
			self.showInformDialog(retStr)
		elif retStr[0] == 'E':
			self.showErroDialog(retStr)
		elif retStr[0] == 'I':
			self.showAcceptDialog(retStr)
			self.clearFields('all')

	def invRead(self):
		self.clearFields('all')
		
		if os.path.isfile('tftpboot/oltinv.cpt') == True:
			if sys.platform == "win32":
				os.system("ccrypt.exe -dfK dp2a3r2mhbolt tftpboot/oltinv.cpt")
			else:
				os.system("ccrypt -dfK dp2a3r2mhbolt tftpboot/oltinv.cpt")
		elif os.path.isfile('tftpboot/onuinv.cpt') == True:
			if sys.platform == "win32":
				os.system("ccrypt.exe -dfK dp2a3r2mhb tftpboot/onuinv.cpt")
			else:
				os.system("ccrypt -dfK dp2a3r2mhb tftpboot/onuinv.cpt")
		elif os.path.isfile('tftpboot/stm1inv.cpt') == True:
			if sys.platform == "win32":
				os.system("ccrypt.exe -dfK dp2a3r2mhbstm1 tftpboot/stm1inv.cpt")
			else:
				os.system("ccrypt -dfK dp2a3r2mhbstm1 tftpboot/stm1inv.cpt")
		elif os.path.isfile('tftpboot/oltbladeinv.cpt') == True:
			if sys.platform == "win32":
				os.system("ccrypt.exe -dfK dp2a3r2mhboltblade tftpboot/oltbladeinv.cpt")
			else:
				os.system("ccrypt -dfK dp2a3r2mhboltblade tftpboot/oltbladeinv.cpt")
		elif os.path.isfile('tftpboot/msddinv.cpt') == True:
			if sys.platform == "win32":
				os.system("ccrypt.exe -dfK dp2a3r2mhbmsdd tftpboot/msddinv.cpt")
			else:
				os.system("ccrypt -dfK dp2a3r2mhbmsdd tftpboot/msddinv.cpt")
		else:
			pass 
		
		
		if os.path.isfile('tftpboot/oltinv') == True:
			f = open('tftpboot/oltinv','rb')
			
			self.PDtabWidget.setCurrentIndex(0)
			
			data = f.read(6)
			tupples = struct.unpack('6s',data)
			mac = binascii.b2a_hex(tupples[0])
			try:
				self.LeOltMac.setText(mac.upper())
			except:
				self.LeOltMac.setText(str(mac.upper(), encoding='ascii').rstrip('\x00'))
			
			data = f.read(30)
			tupples = struct.unpack('30s',data)
			try:
				self.LeOltDproduto.setText(tupples[0])
			except:
				self.LeOltDproduto.setText(str(tupples[0], encoding='ascii').rstrip('\x00'))
			
			data = f.read(2)
			tupples = struct.unpack('>H',data)
			self.LeOltCprod.setText(str(tupples[0]))
			
			data = f.read(4)
			tupples = struct.unpack('>I',data)
			self.LeOltNserie.setText(str(tupples[0]))
			
			data = f.read(11)
			tupples = struct.unpack('11s',data)
			try:
				self.LeOltData.setText(tupples[0])
			except:
				self.LeOltData.setText(str(tupples[0], encoding='ascii').rstrip('\x00'))
			
			data = f.read(2)
			tupples = struct.unpack('>H',data)
			self.LeOltNpedido.setText(str(tupples[0]))
			
			data = f.read(1)
			tupples = struct.unpack('>B',data)
			self.LeOltVhw.setText(str(tupples[0]))
			
			data = f.read(1)
			tupples = struct.unpack('>B',data)
			self.LeOltVfw.setText(str(tupples[0]))
			
			data = f.read(16)
			tupples = struct.unpack('16s',data)
			try:
				self.LeOltSystem.setText(tupples[0])
			except:
				self.LeOltSystem.setText(str(tupples[0], encoding='ascii').rstrip('\x00'))
			
			data = f.read(16)
			tupples = struct.unpack('16s',data)
			try:
				self.LeOltStartup.setText(tupples[0])
			except:
				self.LeOltStartup.setText(str(tupples[0], encoding='ascii').rstrip('\x00'))
			
			data = f.read(16)
			tupples = struct.unpack('16s',data)
			try:
				self.LeOltAsgos.setText(tupples[0])
			except:
				self.LeOltAsgos.setText(str(tupples[0],encoding='ascii').rstrip('\x00'))
			
			data = f.read(100)
			tupples = struct.unpack('100s',data)
			try:
				self.LeOltTec.setText(tupples[0])
			except:
				self.LeOltTec.setText(str(tupples[0], encoding='ascii').rstrip('\x00'))
			
			data = f.read(2)
			tupples = struct.unpack('H',data)
			self.LeOltResets.setText(str(tupples[0]))
			
			f.close()
			
		elif os.path.isfile('tftpboot/onuinv') == True:
			#01789993680005011170124210106423
			f = open('tftpboot/onuinv','rb')
			
			self.PDtabWidget.setCurrentIndex(1)
			
			data = f.read(6)
			tupples = struct.unpack('6s',data)
			mac = binascii.b2a_hex(tupples[0])
			print (mac)
			try:
				self.LeOnuMac.setText(mac.upper())
			except:
				self.LeOnuMac.setText(str(mac.upper(),encoding='ascii').rstrip('\x00'))
			
			data = f.read(30)
			tupples = struct.unpack('30s',data)
			try:
				self.LeOnuDproduto.setText(tupples[0])
			except:
				self.LeOnuDproduto.setText(str(tupples[0],encoding='ascii').rstrip('\x00'))
			
			data = f.read(2)
			tupples = struct.unpack('>H',data)
			self.LeOnuCprod.setText(str(tupples[0]))
			
			data = f.read(4)
			tupples = struct.unpack('>I',data)
			self.LeOnuNserie.setText(str(tupples[0]))
			
			data = f.read(8)
			tupples = struct.unpack('8s',data)
			ponserial = binascii.b2a_hex(tupples[0])
			try:
				self.LeOnuNspon.setText(ponserial.upper())
			except:
				self.LeOnuNspon.setText(str(ponserial.upper(),encoding='ascii').rstrip('\x00'))
			
			data = f.read(11)
			tupples = struct.unpack('11s',data)
			try:
				self.LeOnuData.setText(tupples[0])
			except:
				self.LeOnuData.setText(str(tupples[0],encoding='ascii').rstrip('\x00'))
			
			data = f.read(2)
			tupples = struct.unpack('>H',data)
			self.LeOnuNpedido.setText(str(tupples[0]))
			
			data = f.read(1)
			tupples = struct.unpack('>B',data)
			self.LeOnuVhw.setText(str(tupples[0]))
			
			data = f.read(1)
			tupples = struct.unpack('>B',data)
			'''FIXME: colocar códigos corretos [00033 -> ONU582]'''
			if(str(self.LeOnuCprod.text()) == '61392' or str(self.LeOnuCprod.text()) == '00033'
				or str(self.LeOnuCprod.text()) == '80273' or str(self.LeOnuCprod.text()) == '80274'):
				if(tupples[0] == 2):
					self.LeOnuVfw.setText('L3 Full')
				elif(tupples[0] == 1):
					self.LeOnuVfw.setText('L3 Lite')
				elif(tupples[0] == 0):
					self.LeOnuVfw.setText('L2')
				else:
					self.LeOnuVfw.clear()
			else:	
				self.LeOnuVfw.setText(str(tupples[0]))
			
			data = f.read(16)
			tupples = struct.unpack('16s',data)
			try:
				self.LeOnuSystem.setText(tupples[0])
			except:
				self.LeOnuSystem.setText(str(tupples[0], encoding='ascii').rstrip('\x00'))
			
			data = f.read(100)
			tupples = struct.unpack('100s',data)
			print (tupples)
			
			try:
				self.LeOnuTec.setText(tupples[0])
			except:
				self.LeOnuTec.setText(str(tupples[0], encoding='ascii').rstrip('\x00'))
			
			data = f.read(2)
			tupples = struct.unpack('H',data)
			self.LeOnuResets.setText(str(tupples[0]))
			
			if (self.LeOnuCprod.text() == '0'):
				data = f.read(21)
				tupples = struct.unpack('21s',data)
				try:
					self.LeOnuGtin.setText(tupples[0])
				except:
					self.LeOnuGtin.setText(str(tupples[0], encoding='ascii').rstrip('\x00'))
			
			f.close()
		elif os.path.isfile('tftpboot/stm1inv') == True:
			f = open('tftpboot/stm1inv','rb')
			
			self.PDtabWidget.setCurrentIndex(2)
			
			data = f.read(30)
			tupples = struct.unpack('30s',data)
			try:
				self.LeSTM1Dproduto.setText(tupples[0])
			except:
				self.LeSTM1Dproduto.setText(str(tupples[0], encoding='ascii').rstrip('\x00'))
			
			data = f.read(2)
			tupples = struct.unpack('>H',data)
			self.LeSTM1Cprod.setText(str(tupples[0]))
			
			data = f.read(4)
			tupples = struct.unpack('>I',data)
			self.LeSTM1Nserie.setText(str(tupples[0]))
			
			data = f.read(11)
			tupples = struct.unpack('11s',data)
			try:
				self.LeSTM1Data.setText(tupples[0])
			except:
				self.LeSTM1Data.setText(str(tupples[0],encoding='ascii').rstrip('\x00'))
			
			data = f.read(2)
			tupples = struct.unpack('>H',data)
			self.LeSTM1Npedido.setText(str(tupples[0]))
			
			data = f.read(1)
			tupples = struct.unpack('>B',data)
			self.LeSTM1Vhw.setText(str(tupples[0]))
			
			data = f.read(1)
			tupples = struct.unpack('>B',data)
			self.LeSTM1Vfw.setText(str(tupples[0]))
			
			data = f.read(100)
			tupples = struct.unpack('100s',data)
			try:
				self.LeSTM1Tec.setText(tupples[0])
			except:
				self.LeSTM1Tec.setText(str(tupples[0], encoding='ascii').rstrip('\x00'))
			
			data = f.read(2)
			tupples = struct.unpack('H',data)
			self.LeSTM1Resets.setText(str(tupples[0]))
			
		elif os.path.isfile('tftpboot/oltbladeinv') == True:
			f = open('tftpboot/oltbladeinv','rb')
			
			self.PDtabWidget.setCurrentIndex(3)
			
			data = f.read(6)
			tupples = struct.unpack('6s',data)
			mac = binascii.b2a_hex(tupples[0])
			try:
				self.LeOltBladeMac.setText(mac.upper())
			except:
				self.LeOltBladeMac.setText(str(mac.upper(), encoding='ascii').rstrip('\x00'))
			
			data = f.read(30)
			tupples = struct.unpack('30s',data)
			try:
				self.LeOltBladeDproduto.setText(tupples[0])
			except:
				self.LeOltBladeDproduto.setText(str(tupples[0], encoding='ascii').rstrip('\x00'))
			
			data = f.read(2)
			tupples = struct.unpack('>H',data)
			self.LeOltBladeCprod.setText(str(tupples[0]))
			
			data = f.read(4)
			tupples = struct.unpack('>I',data)
			self.LeOltBladeNserie.setText(str(tupples[0]))
			
			data = f.read(11)
			tupples = struct.unpack('11s',data)
			try:
				self.LeOltBladeData.setText(tupples[0])
			except:
				self.LeOltBladeData.setText(str(tupples[0], encoding='ascii').rstrip('\x00'))
			
			data = f.read(2)
			tupples = struct.unpack('>H',data)
			self.LeOltBladeNpedido.setText(str(tupples[0]))
			
			data = f.read(1)
			tupples = struct.unpack('>B',data)
			self.LeOltBladeVhw.setText(str(tupples[0]))
			
			data = f.read(1)
			tupples = struct.unpack('>B',data)
			self.LeOltBladeVfw.setText(str(tupples[0]))
			
			data = f.read(16)
			tupples = struct.unpack('16s',data)
			try:
				self.LeOltBladeSystem.setText(tupples[0])
			except:
				self.LeOltBladeSystem.setText(str(tupples[0], encoding='ascii').rstrip('\x00'))
			
			data = f.read(16)
			tupples = struct.unpack('16s',data)
			try:
				self.LeOltBladeStartup.setText(tupples[0])
			except:
				self.LeOltBladeStartup.setText(str(tupples[0], encoding='ascii').rstrip('\x00'))
			
			data = f.read(16)
			tupples = struct.unpack('16s',data)
			try:
				self.LeOltBladeAsgos.setText(tupples[0])
			except:
				self.LeOltBladeAsgos.setText(str(tupples[0], encoding='ascii').rstrip('\x00'))
			
			data = f.read(100)
			tupples = struct.unpack('100s',data)
			try:
				self.LeOltBladeTec.setText(tupples[0])
			except:	
				self.LeOltBladeTec.setText(str(tupples[0], encoding='ascii').rstrip('\x00'))
			
			data = f.read(2)
			tupples = struct.unpack('H',data)
			self.LeOltBladeResets.setText(str(tupples[0]))
			
			f.close()
			
		elif os.path.isfile('tftpboot/msddinv') == True:
			f = open('tftpboot/msddinv','rb')
			
			self.PDtabWidget.setCurrentIndex(4)
			
			data = f.read(6)
			tupples = struct.unpack('6s',data)
			mac = binascii.b2a_hex(tupples[0])
			try:
				self.LeMSDDMac.setText(mac.upper())
			except:
				self.LeMSDDMac.setText(str(mac.upper(), encoding='ascii').rstrip('\x00'))
			
			data = f.read(30)
			tupples = struct.unpack('30s',data)
			try:
				self.LeMSDDDproduto.setText(tupples[0])
			except:
				self.LeMSDDDproduto.setText(str(tupples[0], encoding='ascii').rstrip('\x00'))
			
			data = f.read(2)
			tupples = struct.unpack('>H',data)
			self.LeMSDDCprod.setText(str(tupples[0]))
			
			data = f.read(4)
			tupples = struct.unpack('>I',data)
			self.LeMSDDNserie.setText(str(tupples[0]))
			
			data = f.read(8)
			tupples = struct.unpack('8s',data)
			ponserial = binascii.b2a_hex(tupples[0])
			try:
				self.LeMSDDNspon.setText(ponserial.upper())
			except:
				self.LeMSDDNspon.setText(str(ponserial.upper(), encoding='ascii').rstrip('\x00'))
			
			data = f.read(11)
			tupples = struct.unpack('11s',data)
			try:
				self.LeMSDDData.setText(tupples[0])
			except:
				self.LeMSDDData.setText(str(tupples[0], encoding='ascii').rstrip('\x00'))
			
			data = f.read(2)
			tupples = struct.unpack('>H',data)
			self.LeMSDDNpedido.setText(str(tupples[0]))
			
			data = f.read(1)
			tupples = struct.unpack('>B',data)
			self.LeMSDDVhw.setText(str(tupples[0]))
			
			data = f.read(1)
			tupples = struct.unpack('>B',data)
			self.LeMSDDVfw.setText(str(tupples[0]))
			
			data = f.read(16)
			tupples = struct.unpack('16s',data)
			try:
				self.LeMSDDSystem.setText(tupples[0])
			except:
				self.LeMSDDSystem.setText(str(tupples[0], encoding='ascii').rstrip('\x00'))
			
			data = f.read(100)
			tupples = struct.unpack('100s',data)
			try:
				self.LeMSDDTec.setText(tupples[0])
			except:
				self.LeMSDDTec.setText(str(tupples[0], encoding='ascii').rstrip('\x00'))
			
			data = f.read(2)
			tupples = struct.unpack('H',data)
			self.LeMSDDResets.setText(str(tupples[0]))
			
			f.close()
		
		else:
			pass
		
	def calculateBarCode(self):
		try:
			codBarLenght = self.LeCodbar.text().length()
		except: 
			codBarLenght = len(self.LeCodbar.text())
			
		if codBarLenght == 32 :
			self.clearFields('Not all')
			self.removeInvFile()

			'''UPDATE this function every time you add a new Product Code '''
			#Python2 Vs Python3
			try:
				ProdCode = self.LeCodbar.text().mid(10,5)
				Gtin = self.LeCodbar.text().mid(3,13)
				if self.LeCodbar.text().mid(6,4) == '2386':
					isFurukawa = 0;
				elif (self.LeCodbar.text().mid(6,4) == '9936' or self.LeCodbar.text().mid(6,4) == '3137'):
					isFurukawa = 1
				else:
					self.showInformDialog("Código EAN não cadastrado")
					return
			except:
				ProdCode = self.LeCodbar.text()[9:15]
				Gtin = self.LeCodbar.text()[3:16]
				if self.LeCodbar.text()[6:10] == '2386':
					isFurukawa = 0;
				elif (self.LeCodbar.text()[6:10] == '9936' or self.LeCodbar.text()[6:10] == '3137'):
					isFurukawa = 1
				else:
					self.showInformDialog("Código EAN não cadastrado")
					return
			
			
			if (self.verifyProdCode(ProdCode) != '1'):
				if (self.verifyGtin(Gtin) != '1'):
					self.showInformDialog("Código de Produto não encontrado")
					return
			
			if ProdCode == '28110':
				self.PDtabWidget.setCurrentIndex(2)
				
				#Python2 Vs Python3
				try:
					self.LeSTM1Cprod.setText(self.LeCodbar.text().mid(10,5))
					self.LeSTM1Nserie.setText(self.LeCodbar.text().mid(26,6))
					self.LeSTM1Data.setText(self.LeCodbar.text().mid(22,2)+'/'+self.LeCodbar.text().mid(20,2)+'/20'+self.LeCodbar.text().mid(18,2))
				except:
					self.LeSTM1Cprod.setText(self.LeCodbar.text()[10:15])
					self.LeSTM1Nserie.setText(self.LeCodbar.text()[26:32])
					self.LeSTM1Data.setText(self.LeCodbar.text()[22:24]+'/'+self.LeCodbar.text()[20,22]+'/20'+self.LeCodbar.text()[18:20])
				return

			mac = MAC()
			
			if (ProdCode == '61392' or ProdCode == '80273' or ProdCode == '80274'):
				chronosDb = mac.verify_chronosDb()
				if chronosDb != '1':
					self.showInformDialog("Impossivel conectar à "+ chronosDb )
					return
			
			strmac = mac.catchMAC(self.LeCodbar.text(), ProdCode, isFurukawa, str(Gtin))
			if strmac == None:
				mac.insertEAN(self.LeCodbar.text(), str(ProdCode), isFurukawa, str(Gtin))
				strmac = mac.getMAC(self.LeCodbar.text(), isFurukawa)
				if strmac == None:
					self.showInformDialog("Impossivel conectar ao Banco de Dados")
					return
				'''FIXME: corrigir códigos de produto'''
				if (ProdCode == '61392' or ProdCode == '00033'
					or ProdCode == '80273' or ProdCode == '80274'):
					self.LaOnuLayer.setHidden(False)
					
			elif (ProdCode == '61392' or ProdCode == '80273' or ProdCode == '80274'):	#Quando o código de barras já existe, apresenta o tipo de Firmware
				layer = mac.getFirmware_chronos(self.LeCodbar.text())
				if layer != None :
					if layer == '2':
						self.LeOnuVfw.setText('L3 Full')
						self.LaOnuLayer.setCurrentIndex(3)
					elif layer == '1':
						self.LeOnuVfw.setText('L3 Lite')
						self.LaOnuLayer.setCurrentIndex(2)
					elif layer == '0':
						self.LeOnuVfw.setText('L2')
						self.LaOnuLayer.setCurrentIndex(1)
					else:
						self.LaOnuLayer.setCurrentIndex(1)
						
				
			if (ProdCode == '61392' or ProdCode == '80273' or ProdCode == '80274'):
				try:
					f = open(orders_path + str(self.LeOnuNpedido.text()), 'r') 
					lineL2 = f.readline()
					lineL3Lite = f.readline()
					lineL3Full = f.readline()
					f.close()
					lineL2 = lineL2.split()
					lineL3Lite = lineL3Lite.split()
					lineL3Full = lineL3Full.split()
					self.producedL2 = lineL2[2]
					self.totalL2 = lineL2[3]
					self.producedL3Lite = lineL3Lite[3]
					self.totalL3Lite = lineL3Lite[4]
					self.producedL3Full = lineL3Full[3]
					self.totalL3Full = lineL3Full[4]
					self.LaOnuStatusPVL2.setHidden(False)
					self.LbOnuStatusPVL2.setHidden(False)
					self.LaOnuStatusPVL3Lite.setHidden(False)
					self.LbOnuStatusPVL3Lite.setHidden(False)
					self.LaOnuStatusPVL3Full.setHidden(False)
					self.LbOnuStatusPVL3Full.setHidden(False)
					self.LbOnuStatusPVL2.setText(str(self.producedL2 + "/" + self.totalL2))
					self.LbOnuStatusPVL3Lite.setText(str(self.producedL3Lite + "/" + self.totalL3Lite))
					self.LbOnuStatusPVL3Full.setText(str(self.producedL3Full + "/" + self.totalL3Full))
				except:	
					if str(self.LeOnuNpedido.text()) == "":
						self.LeOnuNpedido.setStyleSheet("color: rgb(200, 0, 0);")
						self.LeOnuNpedido.setText(QApplication.translate("PDMainWindow", "Digite Pedido...", None, QApplication.UnicodeUTF8))
					self.LaOnuStatusPVL2.setHidden(True)
					self.LbOnuStatusPVL2.setHidden(True)
					self.LaOnuStatusPVL3Lite.setHidden(True)
					self.LbOnuStatusPVL3Lite.setHidden(True)
					self.LaOnuStatusPVL3Full.setHidden(True)
					self.LbOnuStatusPVL3Full.setHidden(True)
			
			if (ProdCode == '26676' or ProdCode == '26677' or ProdCode == '61952' or 
				ProdCode == '80259' or ProdCode == '80260' or ProdCode == '80262' or
				ProdCode == '80277' or ProdCode == '80261'):
				self.PDtabWidget.setCurrentIndex(0)
				if isFurukawa:
					self.LeOltMac.setText(strmac.upper())
				else:
					self.LeOltMac.setText('00'+strmac.upper())
					
				#Python2 Vs Python3	
				try:
					self.LeOltCprod.setText(self.LeCodbar.text().mid(10,5))
					self.LeOltNserie.setText(self.LeCodbar.text().mid(26,6))
					self.LeOltData.setText(self.LeCodbar.text().mid(22,2)+'/'+self.LeCodbar.text().mid(20,2)+'/20'+self.LeCodbar.text().mid(18,2))
				except:
					self.LeOltCprod.setText(self.LeCodbar.text()[10:15])
					self.LeOltNserie.setText(self.LeCodbar.text()[26:32])
					self.LeOltData.setText(self.LeCodbar.text()[22:24]+'/'+self.LeCodbar.text()[20:22]+'/20'+self.LeCodbar.text()[18:20])

			#  name          					PCode
			# ONU 500 - Fitec 					18094
			# ONU 500 PC 						27772
			# ONU 500 APC	 					56254
			# ONU 500S APC	 					55982
			# ONU 500S PC	 					58938
			# ONU 500V			 				56109
			# ONU 1600 PC		 				55980 7899936802757
			# ONU 1600 APC	 					57107
			# ONU LD 582 L2+L3 Lite+ L3 Full 	61392
			# ONU LD 1180						62441
			# ONU LD 1182						62439
			# ONU LD 1182-W						61728
			# ONU LD 1182-V						62445
			# ONU LD 1182-Y						62620
			# ONU LD 1182-WV					62448
			# ONU LD 1182-WY					62450
			#----------------------------------------
			# OLT BLADE  		(Fictício)		00011
			# MSDD		  		(Fictício)		00022
			# ONU LD 581 L2+L3 	(Fictício)		00033
			
			
				'''FIXME: corrigir códigos de produto'''
			elif (ProdCode == '18094' or ProdCode == '27772' 
				or ProdCode == '56254' or ProdCode == '55982' 
				or ProdCode == '58938' or ProdCode == '56109'
				or ProdCode == '55980' or ProdCode == '57107'
				or ProdCode == '61392' or ProdCode == '62441' 
				or ProdCode == '62439' or ProdCode == '61728' 
				or ProdCode == '62445' or ProdCode == '62620' 
				or ProdCode == '62448' or ProdCode == '62450' 
				or ProdCode == '00033' or ProdCode == '80275'
				or ProdCode == '80273' or ProdCode == '80274'):
				
				self.PDtabWidget.setCurrentIndex(1)
				if isFurukawa == 1:
					self.LeOnuMac.setText(strmac.upper())
				else:
					self.LeOnuMac.setText('00'+strmac.upper())
					
				#Python2 Vs Python3
				try:
					self.LeOnuCprod.setText(self.LeCodbar.text().mid(10,5))
					self.LeOnuNserie.setText(self.LeCodbar.text().mid(26,6))
					self.LeOnuData.setText(self.LeCodbar.text().mid(22,2)+'/'+self.LeCodbar.text().mid(20,2)+'/20'+self.LeCodbar.text().mid(18,2))
				except:
					self.LeOnuCprod.setText(self.LeCodbar.text()[10:15])
					self.LeOnuNserie.setText(self.LeCodbar.text()[26:32])
					self.LeOnuData.setText(self.LeCodbar.text()[22:24]+'/'+self.LeCodbar.text()[20:22]+'/20'+self.LeCodbar.text()[18:20])
					
				if self.LeOnuNserie.text().__len__() == 0 or self.LeOnuCprod.text().__len__() == 0:
					ponnumber="46524b5700000000"
				else:
					
					'''FIXME: ATENÇÃO!!! REVER ESTAS CONDIÇÕES PARA AS NOVAS ONU '''
					# Code product for Onu 2 eth 0 Fxs
					if self.LeOnuCprod.text() == '27772' or self.LeOnuCprod.text() == '56254':
						base = 0x01000000
					# Cod product for Onu 2 eth 2 Fxs
					elif self.LeOnuCprod.text() == '18094':
						base = 0x02000000
						
					elif (self.LeOnuCprod.text() == '55980' or self.LeOnuCprod.text() == '57107' or self.LeOnuCprod.text() == '80275'):
						base = 0x04000000
						
					elif self.LeOnuCprod.text() == '55982' or self.LeOnuCprod.text() == '56254':
						base = 0x05000000
						
					elif self.LeOnuCprod.text() == '56109':
						base = 0x06000000
					# Cod product for Onu 582 L2+ L3 Lite+ L3 Full
					elif (self.LeOnuCprod.text() == '61392' or self.LeOnuCprod.text() == '80273' or self.LeOnuCprod.text() == '80274'): 
						base = 0x10000000
						
					elif  (self.LeOnuCprod.text() == '62441' or self.LeOnuCprod.text() == '62439' 
						or self.LeOnuCprod.text() == '61728' or self.LeOnuCprod.text() == '62445' 
						or self.LeOnuCprod.text() == '62620' or self.LeOnuCprod.text() == '62448' 
						or self.LeOnuCprod.text() == '62450' or self.LeOnuCprod.text() == '00033'):
						base = 0x11000000
						
					else:
						self.showInformDialog("Código de produto não disponivél para essa versão")
					
					ponnumber = 0x46524b5700000000 + base + int(str(self.LeOnuNserie.text()))
					
				self.LeOnuNspon.setText(str(hex(ponnumber).rstrip("L").lstrip("0x")))
				
# 				'''FIXME: corrigir códigos de produto'''
# 				if (self.LeCodbar.text().mid(10,5) == '61392' or self.LeCodbar.text().mid(10,5) == '00033'):
# 					self.LaOnuLayer.setHidden(False)
				
			#new Onus read all the gtin and not only a part of the field
			# 37050049 - MODEM OPTICO GPON LW110-20BP – EAN = 7899936000610
			# 37050050 - MODEM OPTICO LIGHTDRIVE GPON LD510-40BP – EAN = 7899936006865
			# 50582508 - MODEM OPTICO LIGHTDRIVE GPON LD510-40BP – EAN = 7893137299699 (Turnkey)
			

			elif (Gtin == '7899936800050' or Gtin == '7899936002782'
				or Gtin == '7899936802665' or Gtin == '7899936006063'
				or Gtin == '7899936000610' or Gtin == '7899936006865'
				or Gtin == '7899936006865'):
				self.PDtabWidget.setCurrentIndex(1)
				if isFurukawa == 1:
					self.LeOnuMac.setText(strmac.upper())
				else:
					self.LeOnuMac.setText('00'+strmac.upper())
					
				self.LeOnuCprod.setText('0')
				
				#Python2 Vs Python3
				try:
					self.LeOnuNserie.setText(self.LeCodbar.text().mid(26,6))
					self.LeOnuData.setText(self.LeCodbar.text().mid(22,2)+'/'+self.LeCodbar.text().mid(20,2)+'/20'+self.LeCodbar.text().mid(18,2))
				except:
					self.LeOnuNserie.setText(self.LeCodbar.text()[26:32])
					self.LeOnuData.setText(self.LeCodbar.text()[22:24]+'/'+self.LeCodbar.text()[20:22]+'/20'+self.LeCodbar.text()[18:20])
					
				if self.LeOnuNserie.text().__len__() == 0 or self.LeOnuCprod.text().__len__() == 0:
					ponnumber="46524b5700000000"
				elif (Gtin == '7899936800050' or Gtin == '7899936802665'):
					base = 0x13000000
				elif (Gtin == '7899936002782' or Gtin == '7899936006063'):
					base = 0x14000000
				elif (Gtin == '7899936000610'): 
					base = 0x20000000
				elif (Gtin == '7899936006865'):
					base = 0x22000000
				elif (Gtin == '7893137299699'):
					base = 0x24000000				#verificar esse valor em base.
					
				ponnumber = 0x46524b5700000000 + base + int(str(self.LeOnuNserie.text()))
					
				self.LeOnuNspon.setText(str(hex(ponnumber).rstrip("L").lstrip("0x")))
				self.LeOnuGtin.setText(Gtin)

			
				
				
			#	name	Descrp.		PCode
			#OLT BLADE (Fictício) 	00011
				'''FIXME: corrigir códigos de produto'''
			elif ProdCode == '00011':
				self.PDtabWidget.setCurrentIndex(3)
				if isFurukawa == 1:
					self.LeOltBladeMac.setText(strmac.upper())
				else:
					self.LeOltBladeMac.setText('00'+strmac.upper())
					
				#Python2 Vs Python3
				try:
					self.LeOltBladeCprod.setText(self.LeCodbar.text().mid(10,5))
					self.LeOltBladeNserie.setText(self.LeCodbar.text().mid(26,6))
					self.LeOltBladeData.setText(self.LeCodbar.text().mid(22,2)+'/'+self.LeCodbar.text().mid(20,2)+'/20'+self.LeCodbar.text().mid(18,2))
				except:
					self.LeOltBladeCprod.setText(self.LeCodbar.text()[10:15])
					self.LeOltBladeNserie.setText(self.LeCodbar.text()[26:32])
					self.LeOltBladeData.setText(self.LeCodbar.text()[22:24]+'/'+self.LeCodbar.text()[20:22]+'/20'+self.LeCodbar.text()[18:20])

					
			# name				  Descrp.		PCode
			# MSDD  			(Fictício)		00022
				'''FIXME: corrigir códigos de produto'''
			elif ProdCode == '00022':
				
				self.PDtabWidget.setCurrentIndex(4)
				if isFurukawa == 1:
					self.LeMSDDMac.setText(strmac.upper())
				else:
					self.LeMSDDMac.setText('00'+strmac.upper())
					
				#Python2 Vs Python3
				try:
					self.LeMSDDCprod.setText(self.LeCodbar.text().mid(10,5))
					self.LeMSDDNserie.setText(self.LeCodbar.text().mid(26,6))
					self.LeMSDDData.setText(self.LeCodbar.text().mid(22,2)+'/'+self.LeCodbar.text().mid(20,2)+'/20'+self.LeCodbar.text().mid(18,2))
				except:
					self.LeMSDDCprod.setText(self.LeCodbar.text()[10:15])
					self.LeMSDDNserie.setText(self.LeCodbar.text()[26:32])
					self.LeMSDDData.setText(self.LeCodbar.text()[22:24]+'/'+self.LeCodbar.text()[20:22]+'/20'+self.LeCodbar.text()[18:20])
					
				if self.LeMSDDNserie.text().__len__() == 0 or self.LeMSDDCprod.text().__len__() == 0:
					ponnumber="46524b5700000000"
				else:
					
					'''FIXME: ATENÇÃO!!! REVER ESTAS CONDIÇÕES PARA O MSDD '''
					# Code product for MSDD 
					if self.LeMSDDCprod.text() == '00022':
						base = 0x99000000 #<- Atenção, estes são valores aleatórios! ATUALIZAR quando for conhecido o código final
					else:
						self.showInformDialog("Código de produto não disponivél para essa versão")
						
					ponnumber = 0x46524b5700000000 + base + int(str(self.LeOnuNserie.text()))
					
				self.LeMSDDNspon.setText(str(hex(ponnumber).rstrip("L").lstrip("0x")))

			#	name	Descrp.		PCode
			# OLT MAPLE 3516 		            7899936006131
			# OLT MAPLE 3508 		           	7893137283605
			elif (Gtin == '7899936006131' or Gtin == '7893137283605'):
				self.PDtabWidget.setCurrentIndex(5)
				if isFurukawa == 1:
					self.LeOltMapleMac.setText(strmac.upper())
				else:
					self.LeOltMapleMac.setText('00'+strmac.upper())
					
				if Gtin == '7899936006131':
					self.LeOltMapleModel.setText('3516')
				else:
					self.LeOltMapleModel.setText('3508')
				
				#Python2 Vs Python3
				try:
					self.LeOltMapleCprod.setText(self.LeCodbar.text().mid(3,13))
					self.LeOltMapleNserie.setText(self.LeCodbar.text().mid(26,6))
					self.LeOltMapleData.setText(self.LeCodbar.text().mid(22,2)+'/'+self.LeCodbar.text().mid(20,2)+'/20'+self.LeCodbar.text().mid(18,2))
				except:
					self.LeOltMapleCprod.setText(self.LeCodbar.text()[3:16])
					self.LeOltMapleNserie.setText(self.LeCodbar.text()[26:32])
					self.LeOltMapleData.setText(self.LeCodbar.text()[22:24]+'/'+self.LeCodbar.text()[20:22]+'/20'+self.LeCodbar.text()[18:20])
					
				self.PbSend.setFocus()
				self.PbSend.setEnabled(True)
				self.PbWrite.setEnabled(False)
				self.PbRead.setEnabled(False)
				
			self.PbWrite.setFocus()
	
	def verifyProdCode(self,ProdCode):
		if not (ProdCode == '18094' or ProdCode == '27772' 
			or ProdCode == '56254' or ProdCode == '55982' 
			or ProdCode == '58938' or ProdCode == '56109'
			or ProdCode == '55980' or ProdCode == '57107'
			or ProdCode == '28110' or ProdCode == '26676'
			or ProdCode == '26677' or ProdCode == '61392' 
			or ProdCode == '62441' or ProdCode == '62439' 
			or ProdCode == '61728' or ProdCode == '62445' 
			or ProdCode == '62620' or ProdCode == '62448' 
			or ProdCode == '62450' or ProdCode == '00033' 
			or ProdCode == '61952' or ProdCode == '80259'
			or ProdCode == '80260' or ProdCode == '80262'
			or ProdCode == '80277' or ProdCode == '80261'
			or ProdCode == '80275' or ProdCode == '80273' 
			or ProdCode == '80274'):

			return ProdCode
		else :
			return '1'
	
	def verifyGtin(self, Gtin):
		if not (Gtin == '7899936800050' or Gtin == '7899936002782'
		 or Gtin == '7899936006131' or Gtin == '7893137283605' 
		 or Gtin == '7899936802665' or Gtin == '7899936006063' 
		 or Gtin == '7899936000610' or Gtin == '7899936006865'
		 or Gtin == '7893137299699'):
			return Gtin
		else:
			return '1'

	def checkIfL3(self, text):
		if self.LaOnuLayer.currentIndex() == 3:
			self.LeOnuVfw.setText('L3 Full')
		elif self.LaOnuLayer.currentIndex() == 2:
			self.LeOnuVfw.setText('L3 Lite')
		elif self.LaOnuLayer.currentIndex() == 1:
			self.LeOnuVfw.setText('L2')
		elif self.LaOnuLayer.currentIndex() == 0:
			self.LeOnuVfw.clear()
		
	def LeOnuDataCheckWithOutAccent(self):
		self.checkWithOutAccent(self.LeOnuDproduto)
	
	def LeMSDDDataCheckWithOutAccent(self):
		self.checkWithOutAccent(self.LeMSDDDproduto)
		
	def LeOltDataCheckWithOutAccent(self):
		self.checkWithOutAccent(self.LeOltDproduto)
		
	def LeOltBladeDataCheckWithOutAccent(self):
		self.checkWithOutAccent(self.LeOltBladeDproduto)
		
	def LeSTM1DataCheckWithOutAccent(self):
		self.checkWithOutAccent(self.LeSTM1Dproduto)
		
	def LeOnuTecCheckWithOutAccent(self):
		self.checkWithOutAccent(self.LeOnuTec)
		
	def LeMSDDTecCheckWithOutAccent(self):
		self.checkWithOutAccent(self.LeMSDDTec)
		
	def LeOltTecCheckWithOutAccent(self):
		self.checkWithOutAccent(self.LeOltTec)
		
	def LeOltBladeTecCheckWithOutAccent(self):
		self.checkWithOutAccent(self.LeOltBladeTec)
		
	def LeSTM1TecCheckWithOutAccent(self):
		self.checkWithOutAccent(self.LeSTM1Tec)

	def LeOltNpedidoCheckIfDigit(self):
		self.checkIfDigit(self.LeOltNpedido)
	
	def LeOltBladeNpedidoCheckIfDigit(self):
		self.checkIfDigit(self.LeOltBladeNpedido)

	def LeOnuNpedidoCheckIfDigit(self):
		self.checkIfDigitPV(self.LeOnuNpedido)
		
		
	def LeMSDDNpedidoCheckIfDigit(self):
		self.checkIfDigit(self.LeMSDDNpedido)
		
	def LeSTM1NpedidoCheckIfDigit(self):
		self.checkIfDigit(self.LeSTM1Npedido)
				
	def leCodeBarCheckIfDigit(self):
		self.checkIfDigit(self.LeCodbar)
	
	def checkIfDigitPV(self, field):
		pattern = r'[^0-9]'
		try:
			strLen = field.text().length()
		except:
			strlen = len(field.text())
		if ( re.search(pattern,field.text()) or strlen > 5):
			field.setText(field.text()[:-1])
			
	def checkIfDigit(self, field):
		pattern = r'[^0-9]'
		if re.search(pattern,field.text()):
			field.setText(field.text()[:-1])
		
	def checkWithOutAccent(self, field):
		pattern = r'[^\s\.A-Za-z0-9_-]'
		if re.search(pattern,field.text()):
			field.setText(field.text()[:-1])
			
	def	LeOnuNpedidoCheckEmptyness(self):
		if str(self.LeOnuNpedido.text()) == "Digite Pedido...":
			self.LeOnuNpedido.setStyleSheet("color: rgb(0, 0, 0);")
			self.LeOnuNpedido.setText("")
			
	def LeOnuNpedidoCheckOrder(self):
		if (self.LeOnuCprod.text() == '61392' or self.LeOnuCprod.text() == '80273' or self.LeOnuCprod.text() == '80274'):
			if (str(self.LeOnuNpedido.text()) != "Digite Pedido..." and str(self.LeOnuNpedido.text()) != '' ): 
				if int(self.LeOnuNpedido.text()) > 65535:
					self.showInformDialog('Aviso: Pedido de Venda deverá ser menor que 65535')
					return None
				try:
					f = open(orders_path + str(self.LeOnuNpedido.text()), 'r') 
				except:
					self.formSalesOrder(self.LeOnuNpedido.text())
					try:
						f = open(orders_path + str(self.LeOnuNpedido.text()), 'r')
					except:
						self.showInformDialog('Impossivel abrir arquivo de Pedido de Venda '+ str(self.LeOnuNpedido.text()))
						return None 

				lineL2 = f.readline()
				lineL3Lite = f.readline()
				lineL3Full = f.readline()
				f.close()
				lineL2 = lineL2.split()
				lineL3Lite = lineL3Lite.split()
				lineL3Full = lineL3Full.split()
				self.producedL2 = lineL2[2]
				self.totalL2 = lineL2[3]
				self.producedL3Lite = lineL3Lite[3]
				self.totalL3Lite = lineL3Lite[4]
				self.producedL3Full = lineL3Full[3]
				self.totalL3Full = lineL3Full[4]
				self.LaOnuStatusPVL2.setHidden(False)
				self.LbOnuStatusPVL2.setHidden(False)
				self.LaOnuStatusPVL3Lite.setHidden(False)
				self.LbOnuStatusPVL3Lite.setHidden(False)
				self.LaOnuStatusPVL3Full.setHidden(False)
				self.LbOnuStatusPVL3Full.setHidden(False)
				self.LbOnuStatusPVL2.setText(str(self.producedL2 + "/" + self.totalL2))
				self.LbOnuStatusPVL3Lite.setText(str(self.producedL3Lite + "/" + self.totalL3Lite))
				self.LbOnuStatusPVL3Full.setText(str(self.producedL3Full + "/" + self.totalL3Full))
