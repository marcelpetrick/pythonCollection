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
        self.baseDirLabel = QtWidgets.QLabel(frontend)
        self.baseDirLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.baseDirLabel.setObjectName("baseDirLabel")
        self.editsVL.addWidget(self.baseDirLabel)
        self.patternLabel = QtWidgets.QLabel(frontend)
        self.patternLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.patternLabel.setObjectName("patternLabel")
        self.editsVL.addWidget(self.patternLabel)
        self.repsPatternLabel = QtWidgets.QLabel(frontend)
        self.repsPatternLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.repsPatternLabel.setObjectName("repsPatternLabel")
        self.editsVL.addWidget(self.repsPatternLabel)
        self.repsChunkLabel = QtWidgets.QLabel(frontend)
        self.repsChunkLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.repsChunkLabel.setObjectName("repsChunkLabel")
        self.editsVL.addWidget(self.repsChunkLabel)
        self.resultFileSizeLabel = QtWidgets.QLabel(frontend)
        self.resultFileSizeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.resultFileSizeLabel.setObjectName("resultFileSizeLabel")
        self.editsVL.addWidget(self.resultFileSizeLabel)
        self.horizontalLayout.addLayout(self.editsVL)
        self.labelVL = QtWidgets.QVBoxLayout()
        self.labelVL.setObjectName("labelVL")
        self.baseDirLE = QtWidgets.QLineEdit(frontend)
        self.baseDirLE.setEnabled(False)
        self.baseDirLE.setObjectName("baseDirLE")
        self.labelVL.addWidget(self.baseDirLE)
        self.patternLE = QtWidgets.QLineEdit(frontend)
        self.patternLE.setObjectName("patternLE")
        self.labelVL.addWidget(self.patternLE)
        self.repsPatternLE = QtWidgets.QLineEdit(frontend)
        self.repsPatternLE.setObjectName("repsPatternLE")
        self.labelVL.addWidget(self.repsPatternLE)
        self.repsChunkLE = QtWidgets.QLineEdit(frontend)
        self.repsChunkLE.setObjectName("repsChunkLE")
        self.labelVL.addWidget(self.repsChunkLE)
        self.resultFileSizeLE = QtWidgets.QLineEdit(frontend)
        self.resultFileSizeLE.setEnabled(False)
        self.resultFileSizeLE.setObjectName("resultFileSizeLE")
        self.labelVL.addWidget(self.resultFileSizeLE)
        self.horizontalLayout.addLayout(self.labelVL)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.progressBar = QtWidgets.QProgressBar(frontend)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.runPB = QtWidgets.QPushButton(frontend)
        self.runPB.setObjectName("runPB")
        self.verticalLayout.addWidget(self.runPB)
        self.buttonBox = QtWidgets.QDialogButtonBox(frontend)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Abort|QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(frontend)
        QtCore.QMetaObject.connectSlotsByName(frontend)

    def retranslateUi(self, frontend):
        _translate = QtCore.QCoreApplication.translate
        frontend.setWindowTitle(_translate("frontend", "GroundSpace"))
        self.baseDirLabel.setText(_translate("frontend", "base dir:"))
        self.patternLabel.setText(_translate("frontend", "pattern:"))
        self.repsPatternLabel.setText(_translate("frontend", "reps per pattern:"))
        self.repsChunkLabel.setText(_translate("frontend", "reps for for chunks:"))
        self.resultFileSizeLabel.setText(_translate("frontend", "resulting file size:"))
        self.baseDirLE.setPlaceholderText(_translate("frontend", "Currently not implemented"))
        self.resultFileSizeLE.setPlaceholderText(_translate("frontend", "Currently not implemented"))
        self.runPB.setText(_translate("frontend", "Run, Forrest!"))
