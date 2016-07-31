# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changepwd.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_changepwdDialog(object):
    def setupUi(self, changepwdDialog):
        changepwdDialog.setObjectName(_fromUtf8("changepwdDialog"))
        changepwdDialog.resize(485, 344)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/edit-user.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        changepwdDialog.setWindowIcon(icon)
        self.changepwdButtonBox = QtGui.QDialogButtonBox(changepwdDialog)
        self.changepwdButtonBox.setGeometry(QtCore.QRect(260, 290, 191, 32))
        self.changepwdButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.changepwdButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.changepwdButtonBox.setObjectName(_fromUtf8("changepwdButtonBox"))
        self.label = QtGui.QLabel(changepwdDialog)
        self.label.setGeometry(QtCore.QRect(220, 20, 221, 31))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/bristo_logo.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.changepwdTabWidget = QtGui.QTabWidget(changepwdDialog)
        self.changepwdTabWidget.setGeometry(QtCore.QRect(50, 70, 401, 191))
        self.changepwdTabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.changepwdTabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.changepwdTabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.changepwdTabWidget.setMovable(False)
        self.changepwdTabWidget.setObjectName(_fromUtf8("changepwdTabWidget"))
        self.userTab = QtGui.QWidget()
        self.userTab.setAutoFillBackground(False)
        self.userTab.setObjectName(_fromUtf8("userTab"))
        self.layoutWidget = QtGui.QWidget(self.userTab)
        self.layoutWidget.setGeometry(QtCore.QRect(18, 49, 361, 51))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.userNameLabel = QtGui.QLabel(self.layoutWidget)
        self.userNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.userNameLabel.setObjectName(_fromUtf8("userNameLabel"))
        self.horizontalLayout.addWidget(self.userNameLabel)
        self.userNameLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.userNameLineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 252, 213);"))
        self.userNameLineEdit.setObjectName(_fromUtf8("userNameLineEdit"))
        self.horizontalLayout.addWidget(self.userNameLineEdit)
        self.changepwdTabWidget.addTab(self.userTab, icon, _fromUtf8(""))
        self.passwordTab = QtGui.QWidget()
        self.passwordTab.setObjectName(_fromUtf8("passwordTab"))
        self.layoutWidget1 = QtGui.QWidget(self.passwordTab)
        self.layoutWidget1.setGeometry(QtCore.QRect(1, 7, 391, 151))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.oldPasswordLabel = QtGui.QLabel(self.layoutWidget1)
        self.oldPasswordLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.oldPasswordLabel.setObjectName(_fromUtf8("oldPasswordLabel"))
        self.gridLayout.addWidget(self.oldPasswordLabel, 0, 0, 1, 1)
        self.oldPasswordLineEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.oldPasswordLineEdit.setStyleSheet(_fromUtf8("background-color: rgb(126, 154, 255);"))
        self.oldPasswordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.oldPasswordLineEdit.setObjectName(_fromUtf8("oldPasswordLineEdit"))
        self.gridLayout.addWidget(self.oldPasswordLineEdit, 0, 1, 1, 1)
        self.newPasswordLabel = QtGui.QLabel(self.layoutWidget1)
        self.newPasswordLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.newPasswordLabel.setObjectName(_fromUtf8("newPasswordLabel"))
        self.gridLayout.addWidget(self.newPasswordLabel, 1, 0, 1, 1)
        self.newPasswordLineEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.newPasswordLineEdit.setStyleSheet(_fromUtf8("background-color: rgb(126, 154, 255);"))
        self.newPasswordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.newPasswordLineEdit.setObjectName(_fromUtf8("newPasswordLineEdit"))
        self.gridLayout.addWidget(self.newPasswordLineEdit, 1, 1, 1, 1)
        self.reenterPasswordLabel = QtGui.QLabel(self.layoutWidget1)
        self.reenterPasswordLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.reenterPasswordLabel.setObjectName(_fromUtf8("reenterPasswordLabel"))
        self.gridLayout.addWidget(self.reenterPasswordLabel, 2, 0, 1, 1)
        self.reenterPasswordLineEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.reenterPasswordLineEdit.setStyleSheet(_fromUtf8("background-color: rgb(126, 154, 255);"))
        self.reenterPasswordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.reenterPasswordLineEdit.setObjectName(_fromUtf8("reenterPasswordLineEdit"))
        self.gridLayout.addWidget(self.reenterPasswordLineEdit, 2, 1, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/lock.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.changepwdTabWidget.addTab(self.passwordTab, icon1, _fromUtf8(""))
        self.changePasswordLabel = QtGui.QLabel(changepwdDialog)
        self.changePasswordLabel.setGeometry(QtCore.QRect(20, 30, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.changePasswordLabel.setFont(font)
        self.changePasswordLabel.setObjectName(_fromUtf8("changePasswordLabel"))
        self.userNameLabel.setBuddy(self.userNameLineEdit)
        self.oldPasswordLabel.setBuddy(self.oldPasswordLineEdit)
        self.newPasswordLabel.setBuddy(self.newPasswordLineEdit)
        self.reenterPasswordLabel.setBuddy(self.reenterPasswordLineEdit)

        self.retranslateUi(changepwdDialog)
        self.changepwdTabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.changepwdButtonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), changepwdDialog.accept)
        QtCore.QObject.connect(self.changepwdButtonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), changepwdDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(changepwdDialog)

    def retranslateUi(self, changepwdDialog):
        changepwdDialog.setWindowTitle(_translate("changepwdDialog", "bristoSOFT-Change Password", None))
        self.userNameLabel.setText(_translate("changepwdDialog", "Username:", None))
        self.changepwdTabWidget.setTabText(self.changepwdTabWidget.indexOf(self.userTab), _translate("changepwdDialog", "User", None))
        self.oldPasswordLabel.setText(_translate("changepwdDialog", "Old Password:", None))
        self.newPasswordLabel.setText(_translate("changepwdDialog", "New Password:", None))
        self.reenterPasswordLabel.setText(_translate("changepwdDialog", "Re-Enter New:", None))
        self.changepwdTabWidget.setTabText(self.changepwdTabWidget.indexOf(self.passwordTab), _translate("changepwdDialog", "Password", None))
        self.changePasswordLabel.setText(_translate("changepwdDialog", "Change Password:", None))

import resources_rc
