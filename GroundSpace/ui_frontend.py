# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 270)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.editsVL = QtWidgets.QVBoxLayout()
        self.editsVL.setObjectName("editsVL")
        self.basedirLabel = QtWidgets.QLabel(Dialog)
        self.basedirLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.basedirLabel.setObjectName("basedirLabel")
        self.editsVL.addWidget(self.basedirLabel)
        self.patternLabel = QtWidgets.QLabel(Dialog)
        self.patternLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.patternLabel.setObjectName("patternLabel")
        self.editsVL.addWidget(self.patternLabel)
        self.repetitionsLabel = QtWidgets.QLabel(Dialog)
        self.repetitionsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.repetitionsLabel.setObjectName("repetitionsLabel")
        self.editsVL.addWidget(self.repetitionsLabel)
        self.resultfilesizeLabel = QtWidgets.QLabel(Dialog)
        self.resultfilesizeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.resultfilesizeLabel.setObjectName("resultfilesizeLabel")
        self.editsVL.addWidget(self.resultfilesizeLabel)
        self.numberoffilesLabel = QtWidgets.QLabel(Dialog)
        self.numberoffilesLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.numberoffilesLabel.setObjectName("numberoffilesLabel")
        self.editsVL.addWidget(self.numberoffilesLabel)
        self.horizontalLayout.addLayout(self.editsVL)
        self.labelVL = QtWidgets.QVBoxLayout()
        self.labelVL.setObjectName("labelVL")
        self.basedirLE = QtWidgets.QLineEdit(Dialog)
        self.basedirLE.setObjectName("basedirLE")
        self.labelVL.addWidget(self.basedirLE)
        self.patternLE = QtWidgets.QLineEdit(Dialog)
        self.patternLE.setObjectName("patternLE")
        self.labelVL.addWidget(self.patternLE)
        self.repetitionsLE = QtWidgets.QLineEdit(Dialog)
        self.repetitionsLE.setObjectName("repetitionsLE")
        self.labelVL.addWidget(self.repetitionsLE)
        self.resultingfilesizeLE = QtWidgets.QLineEdit(Dialog)
        self.resultingfilesizeLE.setObjectName("resultingfilesizeLE")
        self.labelVL.addWidget(self.resultingfilesizeLE)
        self.numberoffilesLE = QtWidgets.QLineEdit(Dialog)
        self.numberoffilesLE.setObjectName("numberoffilesLE")
        self.labelVL.addWidget(self.numberoffilesLE)
        self.horizontalLayout.addLayout(self.labelVL)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 31)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Abort|QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "GroundSpace"))
        self.basedirLabel.setText(_translate("Dialog", "base dir:"))
        self.patternLabel.setText(_translate("Dialog", "pattern:"))
        self.repetitionsLabel.setText(_translate("Dialog", "repetitions:"))
        self.resultfilesizeLabel.setText(_translate("Dialog", "resulting file size:"))
        self.numberoffilesLabel.setText(_translate("Dialog", "number of files:"))
