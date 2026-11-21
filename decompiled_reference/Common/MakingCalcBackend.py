# Source Generated with Decompyle++
# File: fixed/PYZ-00.pyz_extracted/Common/MakingCalcBackend.pyc (Python 3.9)

from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

class Making(QtWidgets.QDialog):
    
    def __init__(self = None):
        super(Making, self).__init__()
        loadUi('Common\\MakingCalc.ui', self)
        None((lambda : self.Calc()))
        None((lambda : self.Calc()))
        None((lambda : self.Calc()))
        None((lambda : self.Calc()))
        self.show()

    
    def Calc(self):
        if self.Mamount.value() != 0 and self.Mntwt.value() != 0 and self.Mrate.value() != 0:
            if self.Mntwt.value() >= 1:
                if self.EBill.isChecked() != True:
                    Making = self.Mamount.value() / 1.03 / self.Mntwt.value() - self.Mrate.value()
                else:
                    Making = self.Mamount.value() / self.Mntwt.value() - self.Mrate.value()
            elif self.EBill.isChecked() != True:
                Making = self.Mamount.value() / 1.03 - self.Mntwt.value() * self.Mrate.value()
            else:
                Making = self.Mamount.value() - self.Mntwt.value() * self.Mrate.value()
            print(Making)
            self.Result.setText(f'''Making: {Making}''')

    __classcell__ = None

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = Making()
    sys.exit(app.exec_())
