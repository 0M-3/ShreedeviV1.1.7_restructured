"""Daily opening dialog (rates and opening cash)."""

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi

from Common.backend import Store_Opening


class Opening(QtWidgets.QDialog):
    """Dialog used to enter gold/silver rates and opening cash."""

    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('Common/Opening.ui', self)
        self.Submit.clicked.connect(self.Submit_data)
        self.Cancel.clicked.connect(self.reject)
        self.show()

    def Submit_data(self):
        """Validate and persist the opening data."""
        if (self.GoldRate.value() != 0 and self.SilverRate.value() != 0 and
                self.OpnCash.value() != 0):
            Store_Opening(
                self.GoldRate.value(),
                self.SilverRate.value(),
                self.OpnCash.value(),
            )
            QtWidgets.QMessageBox.information(
                self,
                'Data Entry Confirmation',
                'The details have been entered',
            )
        else:
            QtWidgets.QMessageBox.warning(
                self,
                'Invalid Entry',
                'Please retry your details',
            )


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    dialog = Opening()
    sys.exit(app.exec_())
