#!/usr/bin/python

# Imports
import sys
# import os
# import exceptions
import platform
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.uic import *
from psycopg2 import *

__version__ = '0.1'

bristocontacts = loadUiType('contacts_main.ui')[0]

class bristosoftContacts(QMainWindow,  bristocontacts):

    def __init__(self, parent=None):
        super(bristosoftContacts, self).__init__(parent)
        self.setupUi(self)
        
        # about menu connections
        self.connect(self.actionAbout_Qt, SIGNAL('triggered()'), self.aboutqt)
        self.connect(self.actionAbout_bristoSOFT_Contacts, SIGNAL('triggered()'),
                     self.aboutbristocontacts)
        

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
        pass
    
    def db_record_remove(self):
        pass
    
    def db_record_new(self):
        pass
    
    def db_record_fetch(self):
        pass
    

    

def main():
    app = QApplication(sys.argv)
    contacts = bristosoftContacts()
    contacts.show()
    app.exec_()

if __name__ == '__main__':
    main()
