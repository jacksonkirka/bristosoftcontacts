#!/usr/bin/python
#
#
# Copyright 2016 Kirk A Jackson DBA bristoSOFT all rights reserved.  All methods,
# techniques, algorithms are confidential trade secrets under Ohio and U.S. 
# Federal law owned by bristoSOFT.
#
# Kirk A Jackson dba bristoSOFT
# 4100 Executive Park Drive
# Suite 11
# Cincinnati, OH  45241
# Phone (513) 401-9114
# email jacksonkirka@bristosoft.com
# 
# The trade name bristoSOFT is a registered trade name with the State of Ohio
# document No. 201607803210. 

'''
This bristoprint module enables contacts to print to printers, plotters and
other devices via QPrintDialog.
'''

# Imports
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import datetime


class PrintServices:
    
    '''
    The PrintServices class in contacts provides all the resources required
    for print information in contacts.
    '''
    def __init__(self, parent=None):
        '''
        This initialization class method initializes
        contacts fields.
        '''
        #Date and Time
        self._DATE = datetime.datetime.now()
        self._TODAY = self._DATE.strftime("%m/%d/%y %I:%M%p")
        
        self._ITEM = 0
        self._FIRSTITEM = 0
        self._ID = 0
        self._COMPANY = 1
        self._MRMRS = 2
        self._FNAME = 3
        self._MIDDLE = 4
        self._LNAME = 5
        self._CRED = 6
        self._ADDR = 7
        self._SUITE = 8
        self._CITY = 9
        self._ST = 10
        self._POSTAL = 11
        self._OPHONE = 12
        self._CELL = 13
        self._HPHONE = 14
        self._OEMAIL = 15
        self._PEMAIL = 16
        self._OWEB = 17
        self._PWEB = 18
        self._PIC = 19
        self._FAX = 20
        self._OWNER = 21
        self._AVAIL = 22
        self._GROUP = 23
        
    def print_users_contacts(self,  _contacts, _grprpt):
        
        '''
        print_users_contacts prints all the contacts in memory within
        the query limit.
        
        _contacts - python list of contacts to print queried from db
        _grprpt - group name is group query or if null then skipped.
        '''
        
        if _contacts:
            if len(_contacts) > 0:
                
                # Setup printer
                doc = ''
                bristoprint = QPrintDialog()
                if bristoprint.exec_() == QDialog.Accepted:
                    # begin printing to printer line by line
                    qtxtedit = QTextEdit()
                    qtxtedit.setFontPointSize(12.0)
                    doc = 'bristoSOFT Contacts v. 0.1    ' +self._TODAY+'\n\r'
                    if _grprpt:
                        doc = doc + _grprpt+'\n\r'
                    for x in range(len(_contacts)):
                        if not _contacts[x][self._SUITE]:
                            doc = doc + _contacts[x][self._FNAME]\
                            + ' '+ _contacts[x][self._LNAME]+'\n'\
                            + _contacts[x][self._CRED]+'\n'\
                            + _contacts[x][self._COMPANY]+'\n'\
                            + _contacts[x][self._ADDR]+'\n'\
                            + _contacts[x][self._CITY]\
                            + ', '+ _contacts[x][self._ST]\
                            + '  '+ _contacts[x][self._POSTAL]+'\n'\
                            + _contacts[x][self._OPHONE]+'\n'\
                            + _contacts[x][self._OEMAIL]+'\n\r'
                        else:
                            doc = doc + _contacts[x][self._FNAME]\
                            + ' '+ _contacts[x][self._LNAME]+'\n'\
                            + _contacts[x][self._CRED]+'\n'\
                            + _contacts[x][self._COMPANY]+'\n'\
                            + _contacts[x][self._ADDR]+'\n'\
                            + _contacts[x][self._SUITE]+'\n'\
                            + _contacts[x][self._CITY]\
                            + ', '+ _contacts[x][self._ST]\
                            + '  '+ _contacts[x][self._POSTAL]+'\n'\
                            + _contacts[x][self._OPHONE]+'\n'\
                            + _contacts[x][self._OEMAIL]+'\n\r'
                    qtxtedit.setText(doc)
                    qtxtedit.print_(bristoprint.printer())
