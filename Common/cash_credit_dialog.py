"""Cash-credit dialog used to reconcile cash at the end of the day."""

from datetime import datetime

from PyQt5 import QtWidgets, QtGui
from PyQt5.uic import loadUi

from Common.backend import Get_Billsday, Get_opn


class CCCalc(QtWidgets.QDialog):
    """Dialog that computes expected cash and the difference with actual cash."""

    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('Common/CCCalc.ui', self)
        self.Cashinhand.valueChanged.connect(lambda: self.DiffCalc())
        self.Dateentry.setInputMask('99-99-9999')
        self.Dateentry.setText(datetime.today().strftime('%d-%m-%Y'))
        self.Dateentry.textChanged.connect(lambda: self.CashCalc())
        self.total = 0
        self.CashCalc()
        self.show()

    def CashCalc(self):
        """Compute expected cash from the database for the selected date."""
        dte = datetime.strptime(self.Dateentry.text(), '%d-%m-%Y')
        db = Get_Billsday(dte.strftime('%Y-%m-%d'))
        total = Get_opn(dte.strftime('%Y-%m-%d'))

        for row in db:
            trans_type = row[10]
            amount = row[11]
            if trans_type == 'Gold Sale':
                total += amount
            elif trans_type == 'Silver Sale':
                total += amount
            elif trans_type == 'Old Order':
                total += amount
            elif trans_type == 'New Order':
                total += amount
            elif trans_type == 'VC':
                total += amount
            elif trans_type == 'Misc plus':
                total += amount
            elif trans_type == 'Silver Purchase':
                total -= amount
            elif trans_type == 'Misc minus':
                total -= amount
            elif trans_type == 'Expense':
                total -= amount
            elif trans_type == 'Gold Purchase':
                total -= amount

            if row[13] > 0:
                total -= row[13]   # card
            if row[15] > 0:
                total -= row[15]   # UPI
            if row[17] > 0:
                total -= row[17]   # cheque
            if row[19] > 0:
                total -= row[19]   # debt

        self.total = total
        self.ExpCash.setText(f'Expected Cash:      {self.total}')

    def DiffCalc(self):
        """Display the difference between cash-in-hand and expected cash."""
        val = self.Cashinhand.value() - self.total
        self.Diff.setText(f'Difference:            {val}')


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    dialog = CCCalc()
    sys.exit(app.exec_())
