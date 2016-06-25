#!/usr/bin/python

# Imports
import sip
sip.setapi('QString', 2)
import sys
# import os
from bristo_exceptions import *
import platform
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.uic import *
import psycopg2

__version__ = '0.1'

contactsdialog = loadUiType('contacts.ui')[0]
bristocontacts = loadUiType('contacts_main.ui')[0]
bristologin = loadUiType('login.ui')[0]
bristosearch = loadUiType('search.ui')[0]


class bristoContactsLogin(QDialog,  bristologin):
    def __init__(self,  parent=None):
        super(bristoContactsLogin,  self).__init__(parent)
        self.setupUi(self)

class bristoContactsDialog(QDialog,  contactsdialog):
    def __init__(self,  parent=None):
        super(bristoContactsDialog,  self).__init__(parent)
        self.setupUi(self)

class bristoContactsSearchDialog(QDialog,  bristosearch):
    def __init__(self,  parent=None):
        super(bristoContactsSearchDialog,  self).__init__(parent)
        self.setupUi(self)


class bristosoftContacts(QMainWindow,  bristocontacts):

    def __init__(self, parent=None):
        super(bristosoftContacts, self).__init__(parent)
        self.setupUi(self)
        
        # set contactsDialog in cetralWidget
        #self.bristo = bristoContactsDialog()
        #self.setCentralWidget(self.bristo)
        
        # Set connected to false
        self.disconnected = False
        
        self.login = bristoContactsLogin()
        
        # about menu connections
        self.connect(self.actionAbout_Qt, SIGNAL('triggered()'), self.aboutqt)
        self.connect(self.actionAbout_bristoSOFT_Contacts, SIGNAL('triggered()'),
                     self.aboutbristocontacts)
        self.connect(self.actionConnect, SIGNAL('triggered()'),  self.db_connect)
        self.connect(self.actionNew, SIGNAL('triggered()'),  self.db_record_new)
        self.connect(self.login, SIGNAL('accepted()'),  self.db_login)
        self.connect(self.actionVacuum,  SIGNAL('triggered()'),  self.db_full_vacuum)
        self.connect(self.actionDisconnect,  SIGNAL('triggered()'), self.db_close)
        self.connect(self.actionQuery,  SIGNAL('triggered()'),  self.db_record_fetch)
        
        # set contactsStatusBar to red
        self.contactsStatusBar.setStyleSheet("background-color: \
                                              rgb(230, 128, 128);")
    
        # Settings
        settings = QSettings()
        size = settings.value("MainWindow/Size",
                              QVariant(QSize(630, 774))).toSize()
        self.resize(size)
        position = settings.value("MainWindow/Position",
                                  QVariant(QPoint(320, 140))).toPoint()
        self.move(position)
        self.restoreState(
                settings.value("MainWindow/State").toByteArray())
    
    # About class methods
    def aboutqt(self):
        mesg = QMessageBox()
        mesg.aboutQt(self,  'About Qt')
    
    def aboutbristocontacts(self):
        QMessageBox.about(self, "About bristoSOFT Contacts v. 0.1",
        """ <img src='bristo_logo.png' /><br />
        <b>About bristoSOFT Contacts</b> v %s
        <p>Copyright &copy; 2016 bristoSOFT 
        All rights reserved.
        <p>This is a PostgreSQL database contacts management system.  It is
        based on the PyQt frontend GUI.
        <p>Python %s - Qt %s - PyQt %s on %s""" % (
        __version__, platform.python_version(),
        QT_VERSION_STR, PYQT_VERSION_STR, platform.system()))
    
    # class Database Methods
    def db_connect(self):
        self.login.show()
    

    def db_login(self):
        if self.login.userNameLineEdit.text() and self.login.hostLineEdit.text() \
            and self.login.databaseLineEdit.text() and \
            self.login.passwordLineEdit.text():
            con = "host='"+ self.login.hostLineEdit.text() + "' dbname='" + \
                   self.login.databaseLineEdit.text() + "' user='" + \
                   self.login.userNameLineEdit.text() + "' password='" + \
                   self.login.passwordLineEdit.text() + "'"
            self.conn = psycopg2.connect(con)
            self.connected = True
            if self.disconnected:
                self.contactsStatusBar.removeWidget(self.conn_msg)
            self.conn_msg = QLabel('Connected to host: '+ 
                                    self.login.userNameLineEdit.text() +"@"+
                                    self.login.hostLineEdit.text()+
                                  '/'+ self.login.databaseLineEdit.text()+'.')
            self.contactsStatusBar.setStyleSheet("background-color: \
                                                 rgb(179, 255, 188);")
            
            self.contactsStatusBar.addWidget(self.conn_msg)
            self.cursor = self.conn.cursor()
                              
    def db_record_remove(self):
        pass
    
    def db_record_new(self):
        # set contactsDialog in cetralWidget
        self.bristo = bristoContactsDialog()
        self.setCentralWidget(self.bristo)
        self.connect(self.bristo,  SIGNAL('accepted()'), self.db_insert)

    
    def db_insert(self):
        
        self.query = "INSERT INTO bristo_contacts_ct"+ \
                     "(bristo_contacts_ct_co, bristo_contacts_ct_title,"+ \
                     "bristo_contacts_ct_fname, bristo_contacts_ct_middle,"+ \
                     "bristo_contacts_ct_lname, bristo_contacts_ct_cred,"+ \
                     "bristo_contacts_ct_addr1, bristo_contacts_ct_addr2,"+ \
                     "bristo_contacts_ct_city, bristo_contacts_ct_state,"+ \
                     "bristo_contacts_ct_postal, bristo_contacts_ct_ph_office,"+ \
                     "bristo_contacts_ct_ph_cell, bristo_contacts_ct_home,"+ \
                     "bristo_contacts_ct_email1, bristo_contacts_ct_email2,"+ \
                     "bristo_contacts_ct_web, bristo_contacts_ct_web2, "+ \
                     "bristo_contacts_ct_notes) "+"VALUES (" +\
                     "'"+self.bristo.companyLineEdit.text()+"'"+","+ \
                     "'"+self.bristo.mrmrsLineEdit.text()+" '"+","+ \
                     "'"+self.bristo.firstNameLineEdit.text()+" '"+","+  \
                     "'"+self.bristo.middleNameLineEdit.text()+" '"+","+  \
                     "'"+self.bristo.lastNameLineEdit.text()+" '"+","+  \
                     "'"+self.bristo.credLineEdit.text()+" '"+","+  \
                     "'"+self.bristo.addressLineEdit.text()+" '"+","+  \
                     "'"+self.bristo.suiteLineEdit.text()+" '"+","+  \
                     "'"+self.bristo.cityLineEdit.text()+" '"+","+  \
                     "'"+self.bristo.stateLineEdit.text()+" '"+","+  \
                     "'"+self.bristo.postalLineEdit.text()+" '"+","+  \
                     "'"+self.bristo.officePhoneLineEdit.text()+" '"+","+  \
                     "'"+self.bristo.cellPhoneLineEdit.text()+" '"+","+  \
                     "'"+self.bristo.homePhoneLineEdit.text()+" '"+","+  \
                     "'"+self.bristo.officeEmailLineEdit.text()+" '"+","+  \
                     "'"+self.bristo.personalEmailLineEdit.text()+" '"+","+  \
                     "'"+self.bristo.officeWebLineEdit.text()+" '"+","+  \
                     "'"+self.bristo.personalWebLineEdit.text()+" '"+","+  \
                     "'"+self.bristo.notesTextEdit.toPlainText()+" '"+")"
                     
        self._doQuery(self.query)
        # self.bristo.destroy()
        self.contactsStatusBar.showMessage('New Contact Inserted.', 3000)

    
    def db_record_fetch(self):
        self.bristo_search = bristoContactsSearchDialog()
        self.setCentralWidget(self.bristo_search)
        
        # self._doQuery(self.query)
        # self.contactsStatusBar.showMessage('Contact Fetched.', 3000)
    
    def db_full_vacuum(self):
        
        old_isolation_level = self.conn.isolation_level
        self.conn.set_isolation_level(0)
        self.query = "VACUUM FULL"
        self._doQuery(self.query)
        self.conn.set_isolation_level(old_isolation_level)
        self.contactsStatusBar.showMessage('Vacuuming Database Complete.', 5000)

    def _doQuery(self, query):
        self.cursor.execute(query)
        self.conn.commit()
    
    def db_close(self):
        self.cursor.close()
        self.conn.close()
        self.connected = False
        self.contactsStatusBar.setStyleSheet("background-color: \
                                              rgb(230, 128, 128);")
        self.contactsStatusBar.removeWidget(self.conn_msg)
        self.conn_msg = QLabel('Disconnected from host: '+ 
                                    self.login.hostLineEdit.text()+
                                  '/'+ self.login.databaseLineEdit.text()+'.')
        self.contactsStatusBar.addWidget(self.conn_msg)
        self.disconnected = True
        


def main():
    app = QApplication(sys.argv)
    contacts = bristosoftContacts()
    contacts.show()
    app.exec_()

if __name__ == '__main__':
    main()
