# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contacts_main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_bristosoftContacts(object):
    def setupUi(self, bristosoftContacts):
        bristosoftContacts.setObjectName("bristosoftContacts")
        bristosoftContacts.resize(630, 733)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(bristosoftContacts.sizePolicy().hasHeightForWidth())
        bristosoftContacts.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/edit-user.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        bristosoftContacts.setWindowIcon(icon)
        bristosoftContacts.setStyleSheet("")
        bristosoftContacts.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(bristosoftContacts)
        self.centralwidget.setStyleSheet("background-color: rgb(178, 193, 241);")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 620, 161, 21))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/icons/bristo_logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        bristosoftContacts.setCentralWidget(self.centralwidget)
        self.contactsStatusBar = QtWidgets.QStatusBar(bristosoftContacts)
        self.contactsStatusBar.setToolTip("")
        self.contactsStatusBar.setAutoFillBackground(False)
        self.contactsStatusBar.setStyleSheet("")
        self.contactsStatusBar.setObjectName("contactsStatusBar")
        bristosoftContacts.setStatusBar(self.contactsStatusBar)
        self.menubar = QtWidgets.QMenuBar(bristosoftContacts)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 25))
        self.menubar.setObjectName("menubar")
        self.menuContacts = QtWidgets.QMenu(self.menubar)
        self.menuContacts.setObjectName("menuContacts")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuMaintenance = QtWidgets.QMenu(self.menubar)
        self.menuMaintenance.setObjectName("menuMaintenance")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuNav = QtWidgets.QMenu(self.menubar)
        self.menuNav.setObjectName("menuNav")
        self.menuGroups = QtWidgets.QMenu(self.menubar)
        self.menuGroups.setObjectName("menuGroups")
        bristosoftContacts.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(bristosoftContacts)
        self.toolBar.setIconSize(QtCore.QSize(22, 22))
        self.toolBar.setObjectName("toolBar")
        bristosoftContacts.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.navToolBar = QtWidgets.QToolBar(bristosoftContacts)
        self.navToolBar.setObjectName("navToolBar")
        bristosoftContacts.addToolBar(QtCore.Qt.TopToolBarArea, self.navToolBar)
        self.groupToolBar = QtWidgets.QToolBar(bristosoftContacts)
        self.groupToolBar.setObjectName("groupToolBar")
        bristosoftContacts.addToolBar(QtCore.Qt.TopToolBarArea, self.groupToolBar)
        self.actionConnect = QtWidgets.QAction(bristosoftContacts)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/network-connect.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConnect.setIcon(icon1)
        self.actionConnect.setObjectName("actionConnect")
        self.actionNew = QtWidgets.QAction(bristosoftContacts)
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.actionQuery = QtWidgets.QAction(bristosoftContacts)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/system-search-3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionQuery.setIcon(icon2)
        self.actionQuery.setObjectName("actionQuery")
        self.actionQuit = QtWidgets.QAction(bristosoftContacts)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/system-shutdown-5.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionQuit.setIcon(icon3)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout_Qt = QtWidgets.QAction(bristosoftContacts)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionAbout_bristoSOFT_Contacts = QtWidgets.QAction(bristosoftContacts)
        self.actionAbout_bristoSOFT_Contacts.setObjectName("actionAbout_bristoSOFT_Contacts")
        self.actionVacuum = QtWidgets.QAction(bristosoftContacts)
        self.actionVacuum.setObjectName("actionVacuum")
        self.actionReIndex = QtWidgets.QAction(bristosoftContacts)
        self.actionReIndex.setObjectName("actionReIndex")
        self.actionDisconnect = QtWidgets.QAction(bristosoftContacts)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/network-connect.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionDisconnect.setIcon(icon4)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.actionFirst_Item = QtWidgets.QAction(bristosoftContacts)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/media-skip-backward-6.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFirst_Item.setIcon(icon5)
        self.actionFirst_Item.setObjectName("actionFirst_Item")
        self.actionPrevious_Item = QtWidgets.QAction(bristosoftContacts)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/media-seek-backward-4.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrevious_Item.setIcon(icon6)
        self.actionPrevious_Item.setObjectName("actionPrevious_Item")
        self.actionNext_Item = QtWidgets.QAction(bristosoftContacts)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/media-seek-forward-4.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNext_Item.setIcon(icon7)
        self.actionNext_Item.setAutoRepeat(True)
        self.actionNext_Item.setObjectName("actionNext_Item")
        self.actionLast_Item = QtWidgets.QAction(bristosoftContacts)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/media-skip-forward-4.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLast_Item.setIcon(icon8)
        self.actionLast_Item.setObjectName("actionLast_Item")
        self.actionSearch = QtWidgets.QAction(bristosoftContacts)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/system-search-4.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSearch.setIcon(icon9)
        self.actionSearch.setObjectName("actionSearch")
        self.actionUpdate = QtWidgets.QAction(bristosoftContacts)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/icons/db_update.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUpdate.setIcon(icon10)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionChangePassword = QtWidgets.QAction(bristosoftContacts)
        self.actionChangePassword.setObjectName("actionChangePassword")
        self.action_Add_Group = QtWidgets.QAction(bristosoftContacts)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/icons/family.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Add_Group.setIcon(icon11)
        self.action_Add_Group.setObjectName("action_Add_Group")
        self.actionSearchGroupsDialog = QtWidgets.QAction(bristosoftContacts)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/icons/system-search-3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSearchGroupsDialog.setIcon(icon12)
        self.actionSearchGroupsDialog.setObjectName("actionSearchGroupsDialog")
        self.action_Print = QtWidgets.QAction(bristosoftContacts)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/icons/document-print-2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Print.setIcon(icon13)
        self.action_Print.setObjectName("action_Print")
        self.menuContacts.addAction(self.actionConnect)
        self.menuContacts.addAction(self.actionDisconnect)
        self.menuContacts.addAction(self.actionNew)
        self.menuContacts.addAction(self.actionQuery)
        self.menuAbout.addAction(self.actionAbout_Qt)
        self.menuAbout.addAction(self.actionAbout_bristoSOFT_Contacts)
        self.menuMaintenance.addSeparator()
        self.menuMaintenance.addAction(self.actionChangePassword)
        self.menuFile.addAction(self.action_Print)
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
        _translate = QtCore.QCoreApplication.translate
        bristosoftContacts.setWindowTitle(_translate("bristosoftContacts", "bristoSOFT Contacts v. 0.1"))
        self.menuContacts.setTitle(_translate("bristosoftContacts", "Contacts"))
        self.menuAbout.setTitle(_translate("bristosoftContacts", "About"))
        self.menuMaintenance.setTitle(_translate("bristosoftContacts", "Maintenance"))
        self.menuFile.setTitle(_translate("bristosoftContacts", "File"))
        self.menuNav.setTitle(_translate("bristosoftContacts", "Nav"))
        self.menuGroups.setTitle(_translate("bristosoftContacts", "Groups"))
        self.toolBar.setWindowTitle(_translate("bristosoftContacts", "Contacts"))
        self.navToolBar.setWindowTitle(_translate("bristosoftContacts", "Navigation"))
        self.groupToolBar.setWindowTitle(_translate("bristosoftContacts", "Groups"))
        self.actionConnect.setText(_translate("bristosoftContacts", "&Connect"))
        self.actionConnect.setShortcut(_translate("bristosoftContacts", "Alt+C"))
        self.actionNew.setText(_translate("bristosoftContacts", "&New"))
        self.actionNew.setShortcut(_translate("bristosoftContacts", "Alt+N"))
        self.actionQuery.setText(_translate("bristosoftContacts", "&Search Dialog"))
        self.actionQuery.setToolTip(_translate("bristosoftContacts", "Search Dialog"))
        self.actionQuery.setShortcut(_translate("bristosoftContacts", "Alt+S"))
        self.actionQuit.setText(_translate("bristosoftContacts", "E&xit"))
        self.actionQuit.setShortcut(_translate("bristosoftContacts", "Alt+X"))
        self.actionAbout_Qt.setText(_translate("bristosoftContacts", "About &Qt"))
        self.actionAbout_Qt.setShortcut(_translate("bristosoftContacts", "Alt+Q"))
        self.actionAbout_bristoSOFT_Contacts.setText(_translate("bristosoftContacts", "About &bristoSOFT Contacts"))
        self.actionAbout_bristoSOFT_Contacts.setShortcut(_translate("bristosoftContacts", "Alt+B"))
        self.actionVacuum.setText(_translate("bristosoftContacts", "&Vacuum"))
        self.actionVacuum.setShortcut(_translate("bristosoftContacts", "Alt+V"))
        self.actionReIndex.setText(_translate("bristosoftContacts", "&ReIndex"))
        self.actionReIndex.setShortcut(_translate("bristosoftContacts", "Alt+R"))
        self.actionDisconnect.setText(_translate("bristosoftContacts", "&Disconnect"))
        self.actionDisconnect.setShortcut(_translate("bristosoftContacts", "Alt+D"))
        self.actionFirst_Item.setText(_translate("bristosoftContacts", "First Item"))
        self.actionFirst_Item.setToolTip(_translate("bristosoftContacts", "First Item"))
        self.actionFirst_Item.setShortcut(_translate("bristosoftContacts", "Ctrl+Up"))
        self.actionPrevious_Item.setText(_translate("bristosoftContacts", "Previous Item"))
        self.actionPrevious_Item.setToolTip(_translate("bristosoftContacts", "Previous Item"))
        self.actionPrevious_Item.setShortcut(_translate("bristosoftContacts", "Ctrl+Shift+Left"))
        self.actionNext_Item.setText(_translate("bristosoftContacts", "Next Item"))
        self.actionNext_Item.setToolTip(_translate("bristosoftContacts", "Next Item"))
        self.actionNext_Item.setShortcut(_translate("bristosoftContacts", "Ctrl+Shift+Right"))
        self.actionLast_Item.setText(_translate("bristosoftContacts", "Last Item"))
        self.actionLast_Item.setToolTip(_translate("bristosoftContacts", "Last Item"))
        self.actionLast_Item.setShortcut(_translate("bristosoftContacts", "Ctrl+Down"))
        self.actionSearch.setText(_translate("bristosoftContacts", "&Search"))
        self.actionSearch.setToolTip(_translate("bristosoftContacts", "Search: click then enter fields then click this icon again."))
        self.actionSearch.setShortcut(_translate("bristosoftContacts", "Ctrl+S"))
        self.actionUpdate.setText(_translate("bristosoftContacts", "&Update"))
        self.actionUpdate.setShortcut(_translate("bristosoftContacts", "Ctrl+U"))
        self.actionChangePassword.setText(_translate("bristosoftContacts", "&Change Password"))
        self.actionChangePassword.setShortcut(_translate("bristosoftContacts", "Alt+C"))
        self.action_Add_Group.setText(_translate("bristosoftContacts", "&Add Group"))
        self.action_Add_Group.setShortcut(_translate("bristosoftContacts", "Alt+A"))
        self.actionSearchGroupsDialog.setText(_translate("bristosoftContacts", "Search Groups Dialog"))
        self.actionSearchGroupsDialog.setShortcut(_translate("bristosoftContacts", "Alt+G"))
        self.action_Print.setText(_translate("bristosoftContacts", "&Print"))
        self.action_Print.setShortcut(_translate("bristosoftContacts", "Alt+P"))

from . import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bristosoftContacts = QtWidgets.QMainWindow()
    ui = Ui_bristosoftContacts()
    ui.setupUi(bristosoftContacts)
    bristosoftContacts.show()
    sys.exit(app.exec_())

