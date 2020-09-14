# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
from PyQt5.QtGui import QPixmap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1069, 868)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(170, 20, 61, 51))
        self.label_9.setStyleSheet("image: url(:/Arrow/symbols/arrow_up.png);")
        self.label_9.setText("")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(160, 500, 81, 51))
        self.label_10.setStyleSheet("image: url(:/Arrow/symbols/arrow.png);")
        self.label_10.setText("")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(-4, 380, 51, 101))
        self.label_11.setStyleSheet("image: url(:/Arrow/symbols/arrow_left.png);")
        self.label_11.setText("")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(130, 40, 141, 271))
        self.label_12.setStyleSheet("image: url(:/Lines/symbols/vertical.png);")
        self.label_12.setText("")

        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(130, 260, 141, 271))
        self.label_14.setStyleSheet("image: url(:/Lines/symbols/vertical.png);")
        self.label_14.setText("")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 310, 121, 191))
        self.label_2.setStyleSheet("image: url(:/Lines/symbols/horizontalbetter.png);")
        self.label_2.setText("")

        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(180, 190, 121, 191))
        self.label_16.setStyleSheet("image: url(:/Lines/symbols/horizontalbetter.png);")
        self.label_16.setText("")

        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(30, 260, 171, 341))
        self.label_17.setStyleSheet("image: url(:/Lines/symbols/horizontalnew.png);")
        self.label_17.setText("")

        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(120, 60, 171, 331))
        self.label_18.setStyleSheet("image: url(:/Lines/symbols/horizontalnew.png);")
        self.label_18.setText("")

        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(110, -40, 171, 331))
        self.label_19.setStyleSheet("image: url(:/Lines/symbols/horizontalnew.png);")
        self.label_19.setText("")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 230, 61, 111))
        self.label.setStyleSheet("image: url(:/Sensors/symbols/thermocouple.png);")
        self.label.setText("")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 350, 61, 111))
        self.label_3.setStyleSheet("image: url(:/Sensors/symbols/thermocouple.png);")
        self.label_3.setText("")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 200, 71, 51))
        self.label_4.setStyleSheet("image: url(:/Valve/symbols/open valve.png);")
        self.label_4.setText("")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 190, 71, 61))
        self.label_5.setStyleSheet("image: url(:/Valve/symbols/relief valve.png);")
        self.label_5.setText("")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 70, 71, 101))
        self.label_6.setStyleSheet("image: url(:/Gauge/symbols/gauge.png);")
        self.label_6.setText("")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(260, 60, 81, 121))
        self.label_7.setStyleSheet("image: url(:/Sensors/symbols/pressure transmitter.png);")
        self.label_7.setText("")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(150, 260, 101, 171))
        self.label_8.setStyleSheet("image: url(:/Tank/symbols/vessel.png);")
        self.label_8.setText("")

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(-10, 430, 241, 101))
        self.label_13.setStyleSheet("image: url(:/Lines/symbols/verticalbetter1.png);")
        self.label_13.setText("")

        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(70, 440, 81, 121))
        self.label_15.setStyleSheet("image: url(:/Sensors/symbols/pressure transmitter.png);")
        self.label_15.setText("")

        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(270, 170, 91, 21))
        self.label_20.setStyleSheet("color: rgb(0, 0, 0);")

        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(80, 170, 81, 21))
        self.label_21.setStyleSheet("color: rgb(0, 0, 0);")

        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(90, 60, 91, 21))
        self.label_22.setStyleSheet("color: rgb(0, 0, 0);")

        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(260, 60, 91, 21))
        self.label_23.setStyleSheet("color: rgb(0, 0, 0);")

        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(270, 310, 101, 21))
        self.label_24.setStyleSheet("color: rgb(0, 0, 0);")

        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(270, 430, 101, 21))
        self.label_25.setStyleSheet("color: rgb(0, 0, 0);")

        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(70, 540, 91, 21))
        self.label_26.setStyleSheet("color: rgb(0, 0, 0);")

        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(190, 330, 31, 21))
        self.label_27.setStyleSheet("color: rgb(0, 0, 0);")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(340, 110, 51, 21))

        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(396, 100, 61, 41))
        self.label_28.setStyleSheet("color: rgb(0, 0, 0);")

        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(140, 550, 51, 41))
        self.label_29.setStyleSheet("color: rgb(0, 0, 0);")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 560, 51, 21))

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(290, 330, 51, 21))

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 450, 51, 21))

        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(350, 320, 61, 41))
        self.label_30.setStyleSheet("color: rgb(0, 0, 0);")

        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(350, 440, 61, 41))
        self.label_31.setStyleSheet("color: rgb(0, 0, 0);")

        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(100, 550, 41, 41))
        self.label_32.setStyleSheet("color: rgb(0, 0, 0);")

        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(300, 320, 41, 41))
        self.label_33.setStyleSheet("color: rgb(0, 0, 0);")

        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(300, 440, 41, 41))
        self.label_34.setStyleSheet("color: rgb(0, 0, 0);")

        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(360, 100, 41, 41))
        self.label_35.setStyleSheet("color: rgb(0, 0, 0);")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(120, 280, 31, 131))
        self.progressBar.setProperty("value", 70)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(40, 330, 51, 21))

        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(100, 320, 51, 41))
        self.label_36.setStyleSheet("color: rgb(0, 0, 0);")

        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setGeometry(QtCore.QRect(60, 320, 41, 41))
        self.label_37.setStyleSheet("color: rgb(0, 0, 0);")

        self.widget = PlotWidget(self.centralwidget)
        self.widget.setLabel('left', 'Pressure [psi]')
        self.widget.setTitle('PT-OX-VENT')
        self.widget.setLabel('bottom', 'Time [psi]')
        self.widget.setXRange(0,100)
        self.widget.setYRange(0,500)
        self.widget.setGeometry(QtCore.QRect(490, 30, 491, 151))

        self.widget_2 = PlotWidget(self.centralwidget)
        self.widget_2.setLabel('bottom', 'Time [sec]')
        self.widget_2.setLabel('left', 'Pressure [psi]')
        self.widget_2.setTitle('PT-OX-TANK')
        self.widget_2.setXRange(0,100)
        self.widget_2.setYRange(0,500)
        self.widget_2.setGeometry(QtCore.QRect(490, 190, 491, 151))

        self.widget_3 = PlotWidget(self.centralwidget)
        self.widget_3.setLabel('bottom', 'Time [s]')
        self.widget_3.setLabel('left', 'Temp [K]')
        self.widget_3.setTitle('TC-OX-TANK-1')
        self.widget_3.setXRange(0,100)
        self.widget_3.setYRange(0,4000)
        self.widget_3.setGeometry(QtCore.QRect(490, 350, 491, 151))

        self.widget_4 = PlotWidget(self.centralwidget)
        self.widget_4.setLabel('bottom', 'Time [s]')
        self.widget_4.setLabel('left', 'Temp [K]')
        self.widget_4.setTitle('TC-OX-TANK-2')
        self.widget_4.setXRange(0,100)
        self.widget_4.setYRange(0,4000)
        self.widget_4.setGeometry(QtCore.QRect(490, 510, 491, 151))

        self.widget_5 = PlotWidget(self.centralwidget)
        self.widget_5.setLabel('bottom', 'Time [s]')
        self.widget_5.setLabel('left', 'Mass [lb]')
        self.widget_5.setTitle('LOX Fuel Mass')
        self.widget_5.setXRange(0,100)
        self.widget_5.setYRange(0,500)
        self.widget_5.setGeometry(QtCore.QRect(490, 670, 491, 151))

        

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1069, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("Liquid Oxygen Tank Monitor")
        self.label_20.setText(_translate("MainWindow", "BLEED-OX"))
        self.label_21.setText(_translate("MainWindow", "VENT-OX"))
        self.label_22.setText(_translate("MainWindow", "G-OX"))
        self.label_23.setText(_translate("MainWindow", "PT-OX-VENT"))
        self.label_24.setText(_translate("MainWindow", "TC-OX-TANK-1"))
        self.label_25.setText(_translate("MainWindow", "TC-OX-TANK-2"))
        self.label_26.setText(_translate("MainWindow", "PT-OX-TANK"))
        self.label_27.setText(_translate("MainWindow", "LOX"))
        self.label_28.setText(_translate("MainWindow", "psi"))
        self.label_29.setText(_translate("MainWindow", "psi"))

        self.label_30.setText(_translate("MainWindow", "K°"))
        self.label_31.setText(_translate("MainWindow", "K°"))
        self.label_32.setText(_translate("MainWindow", "491"))
        self.label_33.setText(_translate("MainWindow", "2672"))
        self.label_34.setText(_translate("MainWindow", "2193"))
        self.label_35.setText(_translate("MainWindow", "283"))

        self.label_36.setText(_translate("MainWindow", "lb"))
        self.label_37.setText(_translate("MainWindow", "384"))

import source

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    app.setStyleSheet('QMainWindow{background-color: darkgray;border: 1px solid black;}')
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

