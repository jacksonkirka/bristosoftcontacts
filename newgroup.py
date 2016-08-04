# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newgroup.ui'
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

class Ui_newGroupDialog(object):
    def setupUi(self, newGroupDialog):
        newGroupDialog.setObjectName(_fromUtf8("newGroupDialog"))
        newGroupDialog.resize(632, 655)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/edit-user.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        newGroupDialog.setWindowIcon(icon)
        newGroupDialog.setWindowOpacity(1.0)
        newGroupDialog.setStyleSheet(_fromUtf8(""))
        self.credentialsFrame = QtGui.QFrame(newGroupDialog)
        self.credentialsFrame.setGeometry(QtCore.QRect(10, 10, 611, 181))
        self.credentialsFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.credentialsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.credentialsFrame.setObjectName(_fromUtf8("credentialsFrame"))
        self.layoutWidget = QtGui.QWidget(self.credentialsFrame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 14, 591, 161))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupLabel = QtGui.QLabel(self.layoutWidget)
        self.groupLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.groupLabel.setObjectName(_fromUtf8("groupLabel"))
        self.gridLayout.addWidget(self.groupLabel, 0, 0, 1, 1)
        self.newGroupLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.newGroupLineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 250, 217)"))
        self.newGroupLineEdit.setObjectName(_fromUtf8("newGroupLineEdit"))
        self.gridLayout.addWidget(self.newGroupLineEdit, 0, 1, 1, 1)
        self.passwordLabel = QtGui.QLabel(self.layoutWidget)
        self.passwordLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.gridLayout.addWidget(self.passwordLabel, 1, 0, 1, 1)
        self.passwordLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.passwordLineEdit.setStyleSheet(_fromUtf8("background-color: rgb(153, 204, 255)"))
        self.passwordLineEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.passwordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordLineEdit.setObjectName(_fromUtf8("passwordLineEdit"))
        self.gridLayout.addWidget(self.passwordLineEdit, 1, 1, 1, 1)
        self.confirmPasswordLabel = QtGui.QLabel(self.layoutWidget)
        self.confirmPasswordLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.confirmPasswordLabel.setObjectName(_fromUtf8("confirmPasswordLabel"))
        self.gridLayout.addWidget(self.confirmPasswordLabel, 2, 0, 1, 1)
        self.confirmPasswordLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.confirmPasswordLineEdit.setStyleSheet(_fromUtf8("background-color: rgb(153, 204, 255)"))
        self.confirmPasswordLineEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.confirmPasswordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.confirmPasswordLineEdit.setObjectName(_fromUtf8("confirmPasswordLineEdit"))
        self.gridLayout.addWidget(self.confirmPasswordLineEdit, 2, 1, 1, 1)
        self.newGroupTabWidget = QtGui.QTabWidget(newGroupDialog)
        self.newGroupTabWidget.setGeometry(QtCore.QRect(10, 220, 611, 371))
        self.newGroupTabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.newGroupTabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.newGroupTabWidget.setTabsClosable(False)
        self.newGroupTabWidget.setMovable(True)
        self.newGroupTabWidget.setObjectName(_fromUtf8("newGroupTabWidget"))
        self.groupDescriptionTab = QtGui.QWidget()
        self.groupDescriptionTab.setObjectName(_fromUtf8("groupDescriptionTab"))
        self.descriptionFrame = QtGui.QFrame(self.groupDescriptionTab)
        self.descriptionFrame.setGeometry(QtCore.QRect(10, 10, 581, 271))
        self.descriptionFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.descriptionFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.descriptionFrame.setLineWidth(2)
        self.descriptionFrame.setObjectName(_fromUtf8("descriptionFrame"))
        self.descTextEdit = QtGui.QTextEdit(self.descriptionFrame)
        self.descTextEdit.setGeometry(QtCore.QRect(13, 17, 551, 241))
        self.descTextEdit.setStyleSheet(_fromUtf8("background-color: rgb(245,245,245);"))
        self.descTextEdit.setObjectName(_fromUtf8("descTextEdit"))
        self.newGroupLabel = QtGui.QLabel(self.groupDescriptionTab)
        self.newGroupLabel.setGeometry(QtCore.QRect(380, 290, 211, 31))
        self.newGroupLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.newGroupLabel.setText(_fromUtf8(""))
        self.newGroupLabel.setPixmap(QtGui.QPixmap(_fromUtf8("bristo_logo.png")))
        self.newGroupLabel.setScaledContents(True)
        self.newGroupLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.newGroupLabel.setObjectName(_fromUtf8("newGroupLabel"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/edit-group.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newGroupTabWidget.addTab(self.groupDescriptionTab, icon1, _fromUtf8(""))
        self.line = QtGui.QFrame(newGroupDialog)
        self.line.setGeometry(QtCore.QRect(10, 200, 611, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.savePushButton = QtGui.QPushButton(newGroupDialog)
        self.savePushButton.setGeometry(QtCore.QRect(520, 610, 99, 27))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/db_add.ico")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.savePushButton.setIcon(icon2)
        self.savePushButton.setObjectName(_fromUtf8("savePushButton"))
        self.cancelPushButton = QtGui.QPushButton(newGroupDialog)
        self.cancelPushButton.setGeometry(QtCore.QRect(415, 610, 99, 27))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/process-stop-5.ico")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.cancelPushButton.setIcon(icon3)
        self.cancelPushButton.setObjectName(_fromUtf8("cancelPushButton"))

        self.retranslateUi(newGroupDialog)
        self.newGroupTabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.savePushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), newGroupDialog.accept)
        QtCore.QObject.connect(self.cancelPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), newGroupDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(newGroupDialog)
        newGroupDialog.setTabOrder(self.cancelPushButton, self.savePushButton)
        newGroupDialog.setTabOrder(self.savePushButton, self.newGroupTabWidget)

    def retranslateUi(self, newGroupDialog):
        newGroupDialog.setWindowTitle(_translate("newGroupDialog", "New Group Dialog", None))
        self.groupLabel.setText(_translate("newGroupDialog", "Group:", None))
        self.newGroupLineEdit.setPlaceholderText(_translate("newGroupDialog", "Group name should not include spaces.", None))
        self.passwordLabel.setText(_translate("newGroupDialog", "Password:", None))
        self.passwordLineEdit.setPlaceholderText(_translate("newGroupDialog", "Password m/b 9 char, upper, lower, number and one special character.", None))
        self.confirmPasswordLabel.setText(_translate("newGroupDialog", "Confirm:", None))
        self.confirmPasswordLineEdit.setPlaceholderText(_translate("newGroupDialog", "Please re-enter the password.", None))
        self.newGroupTabWidget.setTabText(self.newGroupTabWidget.indexOf(self.groupDescriptionTab), _translate("newGroupDialog", "Group Description", None))
        self.savePushButton.setText(_translate("newGroupDialog", "Save", None))
        self.cancelPushButton.setText(_translate("newGroupDialog", "Cancel", None))

import resources_rc
