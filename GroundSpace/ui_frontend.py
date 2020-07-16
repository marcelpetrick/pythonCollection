# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frontend(object):
    def setupUi(self, frontend):
        frontend.setObjectName("frontend")
        frontend.resize(480, 270)
        self.verticalLayout = QtWidgets.QVBoxLayout(frontend)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.editsVL = QtWidgets.QVBoxLayout()
        self.editsVL.setObjectName("editsVL")
        self.basedirLabel = QtWidgets.QLabel(frontend)
        self.basedirLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.basedirLabel.setObjectName("basedirLabel")
        self.editsVL.addWidget(self.basedirLabel)
        self.patternLabel = QtWidgets.QLabel(frontend)
        self.patternLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.patternLabel.setObjectName("patternLabel")
        self.editsVL.addWidget(self.patternLabel)
        self.repetitionsLabel = QtWidgets.QLabel(frontend)
        self.repetitionsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.repetitionsLabel.setObjectName("repetitionsLabel")
        self.editsVL.addWidget(self.repetitionsLabel)
        self.resultfilesizeLabel = QtWidgets.QLabel(frontend)
        self.resultfilesizeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.resultfilesizeLabel.setObjectName("resultfilesizeLabel")
        self.editsVL.addWidget(self.resultfilesizeLabel)
        self.numberoffilesLabel = QtWidgets.QLabel(frontend)
        self.numberoffilesLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.numberoffilesLabel.setObjectName("numberoffilesLabel")
        self.editsVL.addWidget(self.numberoffilesLabel)
        self.horizontalLayout.addLayout(self.editsVL)
        self.labelVL = QtWidgets.QVBoxLayout()
        self.labelVL.setObjectName("labelVL")
        self.basedirLE = QtWidgets.QLineEdit(frontend)
        self.basedirLE.setObjectName("basedirLE")
        self.labelVL.addWidget(self.basedirLE)
        self.patternLE = QtWidgets.QLineEdit(frontend)
        self.patternLE.setObjectName("patternLE")
        self.labelVL.addWidget(self.patternLE)
        self.repetitionsLE = QtWidgets.QLineEdit(frontend)
        self.repetitionsLE.setObjectName("repetitionsLE")
        self.labelVL.addWidget(self.repetitionsLE)
        self.resultingfilesizeLE = QtWidgets.QLineEdit(frontend)
        self.resultingfilesizeLE.setObjectName("resultingfilesizeLE")
        self.labelVL.addWidget(self.resultingfilesizeLE)
        self.numberoffilesLE = QtWidgets.QLineEdit(frontend)
        self.numberoffilesLE.setObjectName("numberoffilesLE")
        self.labelVL.addWidget(self.numberoffilesLE)
        self.horizontalLayout.addLayout(self.labelVL)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.progressBar = QtWidgets.QProgressBar(frontend)
        self.progressBar.setProperty("value", 31)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(frontend)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Abort|QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(frontend)
        QtCore.QMetaObject.connectSlotsByName(frontend)

    def retranslateUi(self, frontend):
        _translate = QtCore.QCoreApplication.translate
        frontend.setWindowTitle(_translate("frontend", "GroundSpace"))
        self.basedirLabel.setText(_translate("frontend", "base dir:"))
        self.patternLabel.setText(_translate("frontend", "pattern:"))
        self.repetitionsLabel.setText(_translate("frontend", "repetitions:"))
        self.resultfilesizeLabel.setText(_translate("frontend", "resulting file size:"))
        self.numberoffilesLabel.setText(_translate("frontend", "number of files:"))
