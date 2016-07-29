# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
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

class Ui_loginDialog(object):
    def setupUi(self, loginDialog):
        loginDialog.setObjectName(_fromUtf8("loginDialog"))
        loginDialog.resize(485, 344)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/edit-user.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        loginDialog.setWindowIcon(icon)
        self.loginButtonBox = QtGui.QDialogButtonBox(loginDialog)
        self.loginButtonBox.setGeometry(QtCore.QRect(260, 290, 191, 32))
        self.loginButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.loginButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.loginButtonBox.setObjectName(_fromUtf8("loginButtonBox"))
        self.label = QtGui.QLabel(loginDialog)
        self.label.setGeometry(QtCore.QRect(220, 20, 221, 31))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/bristo_logo.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget = QtGui.QTabWidget(loginDialog)
        self.tabWidget.setGeometry(QtCore.QRect(50, 70, 401, 191))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.userTab = QtGui.QWidget()
        self.userTab.setAutoFillBackground(False)
        self.userTab.setObjectName(_fromUtf8("userTab"))
        self.widget = QtGui.QWidget(self.userTab)
        self.widget.setGeometry(QtCore.QRect(18, 49, 361, 51))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.userNameLabel = QtGui.QLabel(self.widget)
        self.userNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.userNameLabel.setObjectName(_fromUtf8("userNameLabel"))
        self.horizontalLayout.addWidget(self.userNameLabel)
        self.userNameLineEdit = QtGui.QLineEdit(self.widget)
        self.userNameLineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 252, 213);"))
        self.userNameLineEdit.setObjectName(_fromUtf8("userNameLineEdit"))
        self.horizontalLayout.addWidget(self.userNameLineEdit)
        self.tabWidget.addTab(self.userTab, icon, _fromUtf8(""))
        self.passwordTab = QtGui.QWidget()
        self.passwordTab.setObjectName(_fromUtf8("passwordTab"))
        self.layoutWidget = QtGui.QWidget(self.passwordTab)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 61, 351, 41))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.passwordLabel = QtGui.QLabel(self.layoutWidget)
        self.passwordLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.gridLayout_2.addWidget(self.passwordLabel, 0, 0, 1, 1)
        self.passwordLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.passwordLineEdit.setStyleSheet(_fromUtf8("background-color: rgb(126, 154, 255);"))
        self.passwordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordLineEdit.setObjectName(_fromUtf8("passwordLineEdit"))
        self.gridLayout_2.addWidget(self.passwordLineEdit, 0, 1, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/lock.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.passwordTab, icon1, _fromUtf8(""))
        self.label_2 = QtGui.QLabel(loginDialog)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.passwordLabel.setBuddy(self.passwordLineEdit)

        self.retranslateUi(loginDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.loginButtonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), loginDialog.accept)
        QtCore.QObject.connect(self.loginButtonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), loginDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(loginDialog)

    def retranslateUi(self, loginDialog):
        loginDialog.setWindowTitle(_translate("loginDialog", "bristoSOF Contacts - Login", None))
        self.userNameLabel.setText(_translate("loginDialog", "Username:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.userTab), _translate("loginDialog", "User", None))
        self.passwordLabel.setText(_translate("loginDialog", "Password:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.passwordTab), _translate("loginDialog", "Password", None))
        self.label_2.setText(_translate("loginDialog", "Login:", None))

import resources_rc
