# Source Generated with Decompyle++
# File: fixed/PYZ-00.pyz_extracted/Common/CCCalcBackend.pyc (Python 3.9)

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from Common.Backend import Get_Billsday, Get_opn
from datetime import date

class CCCalc(QtWidgets.QDialog):
    
    def __init__(self = None):
        super(CCCalc, self).__init__()
        loadUi('Common\\CCCalc.ui', self)
        None((lambda : self.DiffCalc()))
        self.Dateentry.setInputMask('99-99-9999')
        self.Dateentry.setText(date.today().strftime('%d-%m-%Y'))
        None((lambda : self.CashCalc()))
        self.total = 0
        self.CashCalc()
        self.show()

    
    def CashCalc(self):
