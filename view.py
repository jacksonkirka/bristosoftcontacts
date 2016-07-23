#!/usr/bin/python

# Imports
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from PyQt4.uic import *
from contacts import *
from login import *
from search import *

class bristoContactsLogin(QDialog,  Ui_loginDialog):
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

class bristoContactsDialog(QDialog,  Ui_contactsDialog):
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

class bristoContactsSearchDialog(QDialog,  Ui_contactsSearchDialog):
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
        self.setZoomFactor(.75)
