# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contacts_main.ui'
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

class Ui_bristosoftContacts(object):
    def setupUi(self, bristosoftContacts):
        bristosoftContacts.setObjectName(_fromUtf8("bristosoftContacts"))
        bristosoftContacts.resize(630, 733)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(bristosoftContacts.sizePolicy().hasHeightForWidth())
        bristosoftContacts.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/edit-user.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        bristosoftContacts.setWindowIcon(icon)
        bristosoftContacts.setStyleSheet(_fromUtf8(""))
        bristosoftContacts.setTabShape(QtGui.QTabWidget.Triangular)
        self.centralwidget = QtGui.QWidget(bristosoftContacts)
        self.centralwidget.setStyleSheet(_fromUtf8("background-color: rgb(178, 193, 241);"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 620, 161, 21))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/bristo_logo.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        bristosoftContacts.setCentralWidget(self.centralwidget)
        self.contactsStatusBar = QtGui.QStatusBar(bristosoftContacts)
        self.contactsStatusBar.setToolTip(_fromUtf8(""))
        self.contactsStatusBar.setAutoFillBackground(False)
        self.contactsStatusBar.setStyleSheet(_fromUtf8(""))
        self.contactsStatusBar.setObjectName(_fromUtf8("contactsStatusBar"))
        bristosoftContacts.setStatusBar(self.contactsStatusBar)
        self.menubar = QtGui.QMenuBar(bristosoftContacts)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuContacts = QtGui.QMenu(self.menubar)
        self.menuContacts.setObjectName(_fromUtf8("menuContacts"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuMaintenance = QtGui.QMenu(self.menubar)
        self.menuMaintenance.setObjectName(_fromUtf8("menuMaintenance"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuNav = QtGui.QMenu(self.menubar)
        self.menuNav.setObjectName(_fromUtf8("menuNav"))
        self.menuGroups = QtGui.QMenu(self.menubar)
        self.menuGroups.setObjectName(_fromUtf8("menuGroups"))
        bristosoftContacts.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(bristosoftContacts)
        self.toolBar.setIconSize(QtCore.QSize(22, 22))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        bristosoftContacts.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.navToolBar = QtGui.QToolBar(bristosoftContacts)
        self.navToolBar.setObjectName(_fromUtf8("navToolBar"))
        bristosoftContacts.addToolBar(QtCore.Qt.TopToolBarArea, self.navToolBar)
        self.groupToolBar = QtGui.QToolBar(bristosoftContacts)
        self.groupToolBar.setObjectName(_fromUtf8("groupToolBar"))
        bristosoftContacts.addToolBar(QtCore.Qt.TopToolBarArea, self.groupToolBar)
        self.actionConnect = QtGui.QAction(bristosoftContacts)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/network-connect.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConnect.setIcon(icon1)
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.actionNew = QtGui.QAction(bristosoftContacts)
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionQuery = QtGui.QAction(bristosoftContacts)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/system-search-3.ico")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionQuery.setIcon(icon2)
        self.actionQuery.setObjectName(_fromUtf8("actionQuery"))
        self.actionQuit = QtGui.QAction(bristosoftContacts)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/system-shutdown-5.ico")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionQuit.setIcon(icon3)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionAbout_Qt = QtGui.QAction(bristosoftContacts)
        self.actionAbout_Qt.setObjectName(_fromUtf8("actionAbout_Qt"))
        self.actionAbout_bristoSOFT_Contacts = QtGui.QAction(bristosoftContacts)
        self.actionAbout_bristoSOFT_Contacts.setObjectName(_fromUtf8("actionAbout_bristoSOFT_Contacts"))
        self.actionVacuum = QtGui.QAction(bristosoftContacts)
        self.actionVacuum.setObjectName(_fromUtf8("actionVacuum"))
        self.actionReIndex = QtGui.QAction(bristosoftContacts)
        self.actionReIndex.setObjectName(_fromUtf8("actionReIndex"))
        self.actionDisconnect = QtGui.QAction(bristosoftContacts)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/network-connect.ico")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionDisconnect.setIcon(icon4)
        self.actionDisconnect.setObjectName(_fromUtf8("actionDisconnect"))
        self.actionFirst_Item = QtGui.QAction(bristosoftContacts)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/media-skip-backward-6.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFirst_Item.setIcon(icon5)
        self.actionFirst_Item.setObjectName(_fromUtf8("actionFirst_Item"))
        self.actionPrevious_Item = QtGui.QAction(bristosoftContacts)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/media-seek-backward-4.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrevious_Item.setIcon(icon6)
        self.actionPrevious_Item.setObjectName(_fromUtf8("actionPrevious_Item"))
        self.actionNext_Item = QtGui.QAction(bristosoftContacts)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/media-seek-forward-4.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNext_Item.setIcon(icon7)
        self.actionNext_Item.setAutoRepeat(True)
        self.actionNext_Item.setObjectName(_fromUtf8("actionNext_Item"))
        self.actionLast_Item = QtGui.QAction(bristosoftContacts)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/media-skip-forward-4.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLast_Item.setIcon(icon8)
        self.actionLast_Item.setObjectName(_fromUtf8("actionLast_Item"))
        self.actionSearch = QtGui.QAction(bristosoftContacts)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/system-search-4.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSearch.setIcon(icon9)
        self.actionSearch.setObjectName(_fromUtf8("actionSearch"))
        self.actionUpdate = QtGui.QAction(bristosoftContacts)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/db_update.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUpdate.setIcon(icon10)
        self.actionUpdate.setObjectName(_fromUtf8("actionUpdate"))
        self.actionChangePassword = QtGui.QAction(bristosoftContacts)
        self.actionChangePassword.setObjectName(_fromUtf8("actionChangePassword"))
        self.action_Add_Group = QtGui.QAction(bristosoftContacts)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/family.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Add_Group.setIcon(icon11)
        self.action_Add_Group.setObjectName(_fromUtf8("action_Add_Group"))
        self.actionSearchGroupsDialog = QtGui.QAction(bristosoftContacts)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/system-search-3.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSearchGroupsDialog.setIcon(icon12)
        self.actionSearchGroupsDialog.setObjectName(_fromUtf8("actionSearchGroupsDialog"))
        self.menuContacts.addAction(self.actionConnect)
        self.menuContacts.addAction(self.actionDisconnect)
        self.menuContacts.addAction(self.actionNew)
        self.menuContacts.addAction(self.actionQuery)
        self.menuAbout.addAction(self.actionAbout_Qt)
        self.menuAbout.addAction(self.actionAbout_bristoSOFT_Contacts)
        self.menuMaintenance.addAction(self.actionVacuum)
        self.menuMaintenance.addAction(self.actionReIndex)
        self.menuMaintenance.addSeparator()
        self.menuMaintenance.addAction(self.actionChangePassword)
        self.menuFile.addAction(self.actionQuit)
        self.menuNav.addAction(self.actionFirst_Item)
        self.menuNav.addAction(self.actionPrevious_Item)
        self.menuNav.addAction(self.actionNext_Item)
        self.menuNav.addAction(self.actionLast_Item)
        self.menuNav.addAction(self.actionSearch)
        self.menuNav.addAction(self.actionUpdate)
        self.menuGroups.addAction(self.action_Add_Group)
        self.menuGroups.addAction(self.actionSearchGroupsDialog)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuContacts.menuAction())
        self.menubar.addAction(self.menuGroups.menuAction())
        self.menubar.addAction(self.menuNav.menuAction())
        self.menubar.addAction(self.menuMaintenance.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.actionQuit)
        self.toolBar.addAction(self.actionConnect)
        self.toolBar.addAction(self.actionDisconnect)
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionQuery)
        self.navToolBar.addAction(self.actionFirst_Item)
        self.navToolBar.addAction(self.actionPrevious_Item)
        self.navToolBar.addAction(self.actionNext_Item)
        self.navToolBar.addAction(self.actionLast_Item)
        self.navToolBar.addAction(self.actionSearch)
        self.navToolBar.addAction(self.actionUpdate)
        self.groupToolBar.addAction(self.action_Add_Group)
        self.groupToolBar.addAction(self.actionSearchGroupsDialog)

        self.retranslateUi(bristosoftContacts)
        QtCore.QMetaObject.connectSlotsByName(bristosoftContacts)

    def retranslateUi(self, bristosoftContacts):
        bristosoftContacts.setWindowTitle(_translate("bristosoftContacts", "bristoSOFT Contacts v. 0.1", None))
        self.menuContacts.setTitle(_translate("bristosoftContacts", "Contacts", None))
        self.menuAbout.setTitle(_translate("bristosoftContacts", "About", None))
        self.menuMaintenance.setTitle(_translate("bristosoftContacts", "Maintenance", None))
        self.menuFile.setTitle(_translate("bristosoftContacts", "File", None))
        self.menuNav.setTitle(_translate("bristosoftContacts", "Nav", None))
        self.menuGroups.setTitle(_translate("bristosoftContacts", "Groups", None))
        self.toolBar.setWindowTitle(_translate("bristosoftContacts", "toolBar", None))
        self.navToolBar.setWindowTitle(_translate("bristosoftContacts", "toolBar_2", None))
        self.groupToolBar.setWindowTitle(_translate("bristosoftContacts", "toolBar_2", None))
        self.actionConnect.setText(_translate("bristosoftContacts", "&Connect", None))
        self.actionConnect.setShortcut(_translate("bristosoftContacts", "Alt+C", None))
        self.actionNew.setText(_translate("bristosoftContacts", "&New", None))
        self.actionNew.setShortcut(_translate("bristosoftContacts", "Alt+N", None))
        self.actionQuery.setText(_translate("bristosoftContacts", "&Search Dialog", None))
        self.actionQuery.setToolTip(_translate("bristosoftContacts", "Search Dialog", None))
        self.actionQuery.setShortcut(_translate("bristosoftContacts", "Alt+S", None))
        self.actionQuit.setText(_translate("bristosoftContacts", "E&xit", None))
        self.actionQuit.setShortcut(_translate("bristosoftContacts", "Alt+X", None))
        self.actionAbout_Qt.setText(_translate("bristosoftContacts", "About &Qt", None))
        self.actionAbout_Qt.setShortcut(_translate("bristosoftContacts", "Alt+Q", None))
        self.actionAbout_bristoSOFT_Contacts.setText(_translate("bristosoftContacts", "About &bristoSOFT Contacts", None))
        self.actionAbout_bristoSOFT_Contacts.setShortcut(_translate("bristosoftContacts", "Alt+B", None))
        self.actionVacuum.setText(_translate("bristosoftContacts", "&Vacuum", None))
        self.actionVacuum.setShortcut(_translate("bristosoftContacts", "Alt+V", None))
        self.actionReIndex.setText(_translate("bristosoftContacts", "&ReIndex", None))
        self.actionReIndex.setShortcut(_translate("bristosoftContacts", "Alt+R", None))
        self.actionDisconnect.setText(_translate("bristosoftContacts", "&Disconnect", None))
        self.actionDisconnect.setShortcut(_translate("bristosoftContacts", "Alt+D", None))
        self.actionFirst_Item.setText(_translate("bristosoftContacts", "First Item", None))
        self.actionFirst_Item.setToolTip(_translate("bristosoftContacts", "First Item", None))
        self.actionFirst_Item.setShortcut(_translate("bristosoftContacts", "Ctrl+Up", None))
        self.actionPrevious_Item.setText(_translate("bristosoftContacts", "Previous Item", None))
        self.actionPrevious_Item.setToolTip(_translate("bristosoftContacts", "Previous Item", None))
        self.actionPrevious_Item.setShortcut(_translate("bristosoftContacts", "Ctrl+Shift+Left", None))
        self.actionNext_Item.setText(_translate("bristosoftContacts", "Next Item", None))
        self.actionNext_Item.setToolTip(_translate("bristosoftContacts", "Next Item", None))
        self.actionNext_Item.setShortcut(_translate("bristosoftContacts", "Ctrl+Shift+Right", None))
        self.actionLast_Item.setText(_translate("bristosoftContacts", "Last Item", None))
        self.actionLast_Item.setToolTip(_translate("bristosoftContacts", "Last Item", None))
        self.actionLast_Item.setShortcut(_translate("bristosoftContacts", "Ctrl+Down", None))
        self.actionSearch.setText(_translate("bristosoftContacts", "&Search", None))
        self.actionSearch.setToolTip(_translate("bristosoftContacts", "Search: click then enter fields then click this icon again.", None))
        self.actionSearch.setShortcut(_translate("bristosoftContacts", "Ctrl+S", None))
        self.actionUpdate.setText(_translate("bristosoftContacts", "&Update", None))
        self.actionUpdate.setShortcut(_translate("bristosoftContacts", "Ctrl+U", None))
        self.actionChangePassword.setText(_translate("bristosoftContacts", "&Change Password", None))
        self.actionChangePassword.setShortcut(_translate("bristosoftContacts", "Alt+C", None))
        self.action_Add_Group.setText(_translate("bristosoftContacts", "&Add Group", None))
        self.action_Add_Group.setShortcut(_translate("bristosoftContacts", "Alt+A", None))
        self.actionSearchGroupsDialog.setText(_translate("bristosoftContacts", "Search Groups Dialog", None))
        self.actionSearchGroupsDialog.setShortcut(_translate("bristosoftContacts", "Alt+G", None))

import resources_rc
