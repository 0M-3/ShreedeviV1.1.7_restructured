"""Making-charge calculator dialog."""

from PyQt5 import QtWidgets, QtGui
from PyQt5.uic import loadUi


class Making(QtWidgets.QDialog):
    """Helper dialog to calculate the making charge per gram."""

    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('Common/MakingCalc.ui', self)
        self.Mamount.valueChanged.connect(self.Calc)
        self.Mntwt.valueChanged.connect(self.Calc)
        self.Mrate.valueChanged.connect(self.Calc)
        self.EBill.toggled.connect(self.Calc)
        self.show()

    def Calc(self):
        """Compute and display the making charge per gram."""
        if (self.Mamount.value() != 0 and self.Mntwt.value() != 0 and
                self.Mrate.value() != 0):
            if self.Mntwt.value() >= 1:
                if not self.EBill.isChecked():
                    making = (self.Mamount.value() / 1.03 / self.Mntwt.value()
                              - self.Mrate.value())
                else:
                    making = (self.Mamount.value() / self.Mntwt.value()
                              - self.Mrate.value())
            elif not self.EBill.isChecked():
                making = (self.Mamount.value() / 1.03
                          - self.Mntwt.value() * self.Mrate.value())
            else:
                making = (self.Mamount.value()
                          - self.Mntwt.value() * self.Mrate.value())
            print(making)
            self.Result.setText(f'Making: {making}')


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    dialog = Making()
    sys.exit(app.exec_())
