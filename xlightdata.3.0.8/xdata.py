#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

sys.path.append('src/')


try:
	from PyQt4 import QtGui, QtCore
	from PyQt4.QtGui import QMainWindow, QApplication
except:
	from PyQt5 import QtGui, QtCore, QtWidgets
	from PyQt5.QtWidgets import QMainWindow, QApplication

from pondata import *



class Testmain(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self )
	         
		self.ui = Ui_PDMainWindow()
		self.ui.setupUi(self)
		

def stop():
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


if __name__ == "__main__":
	app = QApplication(sys.argv)
	try:
		app.connect(app,  QtCore.SIGNAL("lastWindowClosed()"), stop)
	except:
		app.lastWindowClosed.connect(stop)
	f = Testmain()
	f.show()
	sys.exit(app.exec_())
