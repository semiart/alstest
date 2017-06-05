# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'als.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlibwidget import MatplotlibWidget

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(844, 774)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.lblIrRampInterval = QtWidgets.QLabel(Form)
        self.lblIrRampInterval.setObjectName("lblIrRampInterval")
        self.gridLayout.addWidget(self.lblIrRampInterval, 1, 0, 1, 1)
        self.lblIrLevel = QtWidgets.QLabel(Form)
        self.lblIrLevel.setObjectName("lblIrLevel")
        self.gridLayout.addWidget(self.lblIrLevel, 0, 0, 1, 1)
        self.lblSamplingInterval = QtWidgets.QLabel(Form)
        self.lblSamplingInterval.setObjectName("lblSamplingInterval")
        self.gridLayout.addWidget(self.lblSamplingInterval, 3, 0, 1, 1)
        self.prgAlsLevel = QtWidgets.QProgressBar(Form)
        self.prgAlsLevel.setProperty("value", 23)
        self.prgAlsLevel.setTextVisible(True)
        self.prgAlsLevel.setObjectName("prgAlsLevel")
        self.gridLayout.addWidget(self.prgAlsLevel, 8, 0, 1, 4)
        self.btnConnect = QtWidgets.QPushButton(Form)
        self.btnConnect.setObjectName("btnConnect")
        self.gridLayout.addWidget(self.btnConnect, 3, 3, 1, 1)
        self.pltALSReading = MatplotlibWidget(Form)
        self.pltALSReading.setObjectName("pltALSReading")
        self.gridLayout.addWidget(self.pltALSReading, 5, 0, 1, 4)
        self.sbxIrRampInterval = QtWidgets.QSpinBox(Form)
        self.sbxIrRampInterval.setObjectName("sbxIrRampInterval")
        self.gridLayout.addWidget(self.sbxIrRampInterval, 1, 1, 1, 1)
        self.sbxSamplingInterval = QtWidgets.QSpinBox(Form)
        self.sbxSamplingInterval.setObjectName("sbxSamplingInterval")
        self.gridLayout.addWidget(self.sbxSamplingInterval, 3, 1, 1, 1)
        self.sldIrLevel = QtWidgets.QSlider(Form)
        self.sldIrLevel.setOrientation(QtCore.Qt.Horizontal)
        self.sldIrLevel.setObjectName("sldIrLevel")
        self.gridLayout.addWidget(self.sldIrLevel, 0, 1, 1, 3)
        self.lblAlsLevel = QtWidgets.QLabel(Form)
        self.lblAlsLevel.setObjectName("lblAlsLevel")
        self.gridLayout.addWidget(self.lblAlsLevel, 7, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ALS Test Gui"))
        self.lblIrRampInterval.setText(_translate("Form", "IR Ramp Interval (ms)"))
        self.lblIrLevel.setText(_translate("Form", "Max IR Level 0"))
        self.lblSamplingInterval.setText(_translate("Form", "Sampling Interval (ms)"))
        self.prgAlsLevel.setFormat(_translate("Form", "%p"))
        self.btnConnect.setText(_translate("Form", "Connect"))
        self.lblAlsLevel.setText(_translate("Form", "ALS Level"))

