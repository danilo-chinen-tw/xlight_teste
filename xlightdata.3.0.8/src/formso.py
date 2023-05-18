# stdDialogDemo_pyside.py
 
try:
	from PyQt4 import QtCore, QtGui
	from PyQt4.QtGui import QPalette, QColor, QDialog
except:
	from PyQt5 import QtCore, QtGui, QtWidgets
	from PyQt5.QtGui import QPalette, QColor
	from PyQt5.QtWidgets import QDialog
	
import re
import os
from os import path
from fileinput import close

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
    
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = path.relpath("../orders/")
orders_path = os.path.join(script_dir, rel_path) + "/"
 
########################################################################
class SalesOrder(QDialog):
 
    #----------------------------------------------------------------------
    def __init__(self, salesOrder):
        """Constructor"""
        super(SalesOrder, self).__init__()
#         QtGui.QWidget.__init__(self)
 
        self.sOrder = salesOrder
        self.label = QtGui.QLabel("         Quantidade")
 
        # create the editable fields
        self.quantityL2 = QtGui.QLineEdit() 
        self.quantityL3Lite = QtGui.QLineEdit()
        self.quantityL3Full = QtGui.QLineEdit()
 
        # layout widgets
        formLayout = QtGui.QFormLayout(self)
        formLayout.addRow(self.tr(""), self.label)
        formLayout.addRow(self.tr("ONU-HQ2*** (L2):"), self.quantityL2)
        formLayout.addRow(self.tr("ONU-JQ2*** (L3 Lite):"), self.quantityL3Lite)
        formLayout.addRow(self.tr("ONU-KQ2*** (L3 Full):"), self.quantityL3Full)
        formLayout.setFormAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        formLayout.setLabelAlignment(QtCore.Qt.AlignLeft)
        self.setLayout(formLayout)
        
        self.createButton = QtGui.QPushButton("Criar",self)
        self.createButton.setGeometry(90, 160, 130, 30)
        # connect the button to the function (signals to slots)
        self.connect(self.createButton, QtCore.SIGNAL("clicked()"), self.createFile)
        self.connect(self.quantityL2, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.quantityL2CheckIfDigit)
        self.connect(self.quantityL3Lite, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.quantityL3LiteCheckIfDigit)
        self.connect(self.quantityL3Full, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.quantityL3FullCheckIfDigit)
        
        # set the position and size of the window
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Pedido de Venda "+ self.sOrder)
 
    #----------------------------------------------------------------------
    def quantityL2CheckIfDigit(self):
        self.checkIfDigit(self.quantityL2)
        
    #----------------------------------------------------------------------
    def quantityL3LiteCheckIfDigit(self):
        self.checkIfDigit(self.quantityL3Lite)
        
    #----------------------------------------------------------------------
    def quantityL3FullCheckIfDigit(self):
        self.checkIfDigit(self.quantityL3Full)
        
    #----------------------------------------------------------------------
    def createFile(self):
        """
        Check if field are passed with numbers
        """
        if self.quantityL2.text() == "":
            return None
        if self.quantityL3Lite.text() == "":
            return None
        if self.quantityL3Full.text() == "":
            return None
        
        if (self.quantityL2.text() == "0" and self.quantityL3Lite.text() == "0" and self.quantityL3Full.text() == "0"):
            return None
        
        file = open(orders_path + str(self.sOrder), 'w+')
        file.write("ONU-HQ2*** (L2): 0 " + str(int(self.quantityL2.text())) + " \n")
        file.write("ONU-JQ2*** (L3 Lite): 0 " + str(int(self.quantityL3Lite.text())) + " \n")
        file.write("ONU-KQ2*** (L3 Full): 0 " + str(int(self.quantityL3Full.text())) + " \n")
        file.close()
        
        # Fill the fields with the total amount for the Sales Order
        
        #Close the GUI Window
        self.close()
            
    def checkIfDigit(self, field):
        pattern = r'[^0-9]'
        if ( re.search(pattern,field.text()) or field.text().length() > 6):
            field.setText(field.text()[:-1])
            
 
#----------------------------------------------------------------------
# if __name__ == "__main__":
#     app = QtGui.QApplication([])
#     form = SalesOrder("1234")
#     form.show()
#     app.exec_()
