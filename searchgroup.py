# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchgroup.ui'
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

class Ui_searchGroupDialog(object):
    def setupUi(self, searchGroupDialog):
        searchGroupDialog.setObjectName(_fromUtf8("searchGroupDialog"))
        searchGroupDialog.resize(632, 655)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/edit-user.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        searchGroupDialog.setWindowIcon(icon)
        searchGroupDialog.setWindowOpacity(1.0)
        searchGroupDialog.setStyleSheet(_fromUtf8(""))
        self.credentialsFrame = QtGui.QFrame(searchGroupDialog)
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
        self.searchGroupLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.searchGroupLineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 250, 217)"))
        self.searchGroupLineEdit.setObjectName(_fromUtf8("searchGroupLineEdit"))
        self.gridLayout.addWidget(self.searchGroupLineEdit, 0, 1, 1, 1)
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
        self.newGroupTabWidget = QtGui.QTabWidget(searchGroupDialog)
        self.newGroupTabWidget.setGeometry(QtCore.QRect(10, 220, 611, 401))
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
        self.newGroupLabel.setGeometry(QtCore.QRect(380, 320, 211, 31))
        self.newGroupLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.newGroupLabel.setText(_fromUtf8(""))
        self.newGroupLabel.setPixmap(QtGui.QPixmap(_fromUtf8("bristo_logo.png")))
        self.newGroupLabel.setScaledContents(True)
        self.newGroupLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.newGroupLabel.setObjectName(_fromUtf8("newGroupLabel"))
        self.picPushButton = QtGui.QPushButton(self.groupDescriptionTab)
        self.picPushButton.setGeometry(QtCore.QRect(330, 330, 38, 27))
        self.picPushButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/document-open-2.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.picPushButton.setIcon(icon1)
        self.picPushButton.setObjectName(_fromUtf8("picPushButton"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/edit-group.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newGroupTabWidget.addTab(self.groupDescriptionTab, icon2, _fromUtf8(""))
        self.line = QtGui.QFrame(searchGroupDialog)
        self.line.setGeometry(QtCore.QRect(10, 200, 611, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        self.retranslateUi(searchGroupDialog)
        self.newGroupTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(searchGroupDialog)

    def retranslateUi(self, searchGroupDialog):
        searchGroupDialog.setWindowTitle(_translate("searchGroupDialog", "Search Group Dialog", None))
        self.groupLabel.setText(_translate("searchGroupDialog", "Group:", None))
        self.searchGroupLineEdit.setPlaceholderText(_translate("searchGroupDialog", "Search: Groups  and Group Name should not include spaces.", None))
        self.passwordLabel.setText(_translate("searchGroupDialog", "Password:", None))
        self.passwordLineEdit.setPlaceholderText(_translate("searchGroupDialog", "Password m/b 9 char, upper, lower, number and one special character.", None))
        self.confirmPasswordLabel.setText(_translate("searchGroupDialog", "Confirm:", None))
        self.confirmPasswordLineEdit.setPlaceholderText(_translate("searchGroupDialog", "Please re-enter the password.", None))
        self.picPushButton.setToolTip(_translate("searchGroupDialog", "Add Picture", None))
        self.newGroupTabWidget.setTabText(self.newGroupTabWidget.indexOf(self.groupDescriptionTab), _translate("searchGroupDialog", "Group Description", None))

import resources_rc
