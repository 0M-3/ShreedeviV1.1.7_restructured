"""Entry point for PyBookKeeper (restructured from ``script.exe``)."""

import sys

from PyQt5 import QtWidgets

from Common.frontend_window import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
