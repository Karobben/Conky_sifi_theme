#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import *
import os, sys
from PyQt5 import QtGui, QtCore, QtWidgets

class Trans(QApplication):

    def __init__(self):
        super(Trans, self).__init__()
        self.initUI()
        button = QtWidgets.QPushButton('Close', self)
        self.connect(button, QtCore.SIGNAL('clicked()'), QtGui.qApp,
                     QtCore.SLOT('quit()'))

    def initUI(self):
        #self.setAttribute(QtCore.Qt.WA_NoSystemBackground, False)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

if __name__ == '__main__':
    app = QApplication([])
    trans = Trans()
    trans.show()
    sys.exit(app.exec_())
