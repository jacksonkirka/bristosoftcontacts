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
messages.py is the module for bristoSOFT Contacts v. 0.1 that provides resources
for messaging.  The module is based on centralized querying for message sending
and receiving as well as archiving.  Currently it has only one class Messages.
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Messages:
    '''
    The Messages class provides methods to add, check and display messages system wide.
    '''
    
    def check_messages(self):
        '''
        check_messages displays all messages in the bristo_contacts_messages
        database table that were sent by the current user to the current contact
        and that were sent by the current contact to the current user.
        '''
        self.block_signals()
        self.reset_timer()
        # Query the database to create list of messages returned by psycopg2
        # driver from the PostgreSQL database.
        _user = self._user
        _contct_email = self.fetch_results[self._ITEM][self._OEMAIL]
        _contct_usrnm = self.get_contact_username(_contct_email)
        if _contct_usrnm:
            self._cursor = self._conn.cursor()
            self._cursor.execute("""SELECT * FROM bristo_contacts_messages WHERE
                    bristo_contacts_messages_sender = %s AND 
                    bristo_contacts_messages_receiver = %s OR
                    bristo_contacts_messages_sender = %s AND 
                    bristo_contacts_messages_receiver = %s
                    ORDER by bristo_contacts_messages_stamp 
                    LIMIT %s;""",
                    (_user, _contct_usrnm, _contct_usrnm, _user, self._limit))
            self.fetch_msg = self._cursor.fetchall() # Get messages
            self.display_messages(self.fetch_msg) # Display messages
            self.contactsStatusBar.showMessage('Messages updated .......', 4000)
            self.db_close()
            self.unblock_signals()
            
        else:
            self.contactsStatusBar.showMessage('User not found.....', 4000)
            self.db_close()

    def get_contact_username(self,  _contact_email):
        '''
        get_contact_username accepts the contact email address and
        returns the contact username in bristo_contacts_users for a user
        email match.
        '''
        self.db_login()
        if self._connected:
            # Get username for current contact email address
            self._cursor = self._conn.cursor()
            self._cursor.execute("SELECT * FROM bristo_contacts_users WHERE \
            bristo_contacts_users_email = %s LIMIT %s", (
                _contact_email, self._limit))
            if not self._cursor.rowcount:
                self.contactsStatusBar.showMessage('User not found.....', 4000)
                self.db_close()
            else:
                _usr = self._cursor.fetchone()
                return _usr[self._USERNM]
                
    def display_messages(self, _messages):
        '''
        display_messages accepts a message list returned by psycopg2 form a
        PostgreSQL database and displays these messages in the message
        table widget.
        '''
        _user = self._user
        # Display the messages in msgTableWidget and make user sent messages
        # distinct (blue or dark or highlighted) while contact sent message are
        # displayed normally.
        self.bristo_search.msgTableWidget.clearContents()
        _tblwgt_row = 0  # Changes each record
        _tblwgt_stamp = 2 # static
        _tblwgt_sender = 3 # static
        _tblwgt_msg = 5 # static
        for _msg in range(len(_messages)):
            
            _stamp = self.fetch_msg[_msg][_tblwgt_stamp].strftime(
            "%m/%d/%y %I:%M%p")
            _qwitem = QTableWidgetItem(_stamp)
            self.bristo_search.msgTableWidget.setItem(_tblwgt_row, 
                _tblwgt_stamp, _qwitem)
                
            _sender = self.fetch_msg[_msg][_tblwgt_sender]
            _qwitem = QTableWidgetItem(_sender)
            self.bristo_search.msgTableWidget.setItem(_tblwgt_row,
                _tblwgt_sender, _qwitem)
                
            _message = self.fetch_msg[_msg][_tblwgt_msg]
            _qwitem = QTableWidgetItem(_message)
            if _sender == _user:
                _qwitem.setForeground(QColor(65,105,225))
            self.bristo_search.msgTableWidget.setItem(_tblwgt_row,
                _tblwgt_msg, _qwitem)
            _tblwgt_row += 1
