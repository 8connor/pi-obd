# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testfile.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
from pathlib import Path
import sys;
import obd;
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(90, 80, 581, 371))
        self.lcdNumber.setObjectName("lcdNumber")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    # def changeNum (self):
    #     def new_psi(r):
    #         new_num = [int(s) for s in str(r).split() if s.isdigit()]
    #         display_num = round(new_num[0] * 0.14503774)

    #         self.findChild(QtWidgets.QLCDNumber, 'lcdNumber').display(display_num)

    #     def new_oil_temp(r):
    #         print(r.value)

    #         new_num = [int(s) for s in str(r.value.to('f')).split() if s.isdigit()]
    #         print(round(new_num[0]));

    #         self.findChild(QtWidgets.QLCDNumber, 'lcdNumber_2').display()


    #     connection.watch(obd.commands.INTAKE_PRESSURE, callback=new_psi, force=True);
    #     connection.watch(obd.commands.OIL_TEMP, callback=new_oil_temp, force=True);

    #     connection.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
