#!/usr/bin/python

# Imports
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from PyQt4.uic import *

# Dynamic gui interface loading during development
contactsdialog = loadUiType('contacts.ui')[0]
# contactsdialog = loadUiType('contacts_combo.ui')[0]
bristologin = loadUiType('login.ui')[0]
bristosearch = loadUiType('search.ui')[0]

class bristoContactsLogin(QDialog,  bristologin):
    '''
    
    bristoContactsLogin is the login dialog used to login
    to a PostgreSQL database.  It captures the test needed
    to build the PostgreSQL connection string.
    
    '''
    def __init__(self,  parent=None):
        '''
        
        This initialization class method initializes
        QDialog and bristoContactsLogin.
        
        '''
        super(bristoContactsLogin,  self).__init__(parent)
        self.setupUi(self)

class bristoContactsDialog(QDialog,  contactsdialog):
    '''
    
    bristoContactsDialog provides a GUI interface for building
    the database INSERT query. 
    
    '''
    def __init__(self,  parent=None):
        '''
        
        This initialization class method initializes
        QDialog and bristoContactsDialog.
        
        '''
        super(bristoContactsDialog,  self).__init__(parent)
        self.setupUi(self)

class bristoContactsSearchDialog(QDialog,  bristosearch):
    '''
    
    bristoContactsSearchDialog is the a dialog for traversing
    the contacts database.
    
    '''
    def __init__(self,  parent=None):
        ''' 
        
        This initialization class method initializes
        QDialog and bristoContactsSearchDialog.
        
        '''
        super(bristoContactsSearchDialog,  self).__init__(parent)
        self.setupUi(self)
        
class bristoMapper(QWebView):
    
    '''
    bristoMapper is a webview of the address provided in a contact.
    '''
    def __init__(self, parent=None):
        super(bristoMapper, self).__init__(parent)

class bristoMailView(QWebView):
    '''
    bristoMailView is a webview of the users web mail service filtered for the
    current contact.
    '''
    def __init__(self,  parent=None):
        super(bristoMailView,  self).__init__(parent)

    
        
if __name__ == '__main__':
    
    # Unit test as needed
    login = bristoContactsLogin()
    login.show()
