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
from controller import Controller


class Messages:
    '''
    The Messages class provides methods to add, check and display messages system wide.
    '''
    
    # Messages
    self._msg_id = 0
    self._msg_uuid = 1
    self._msg_stamp = 2
    self._msg_sender = 3
    self._msg_receiver =4
    self._msg_text = 5
    # self._msg_chk_wait = 30000
    self.fetch_msg = None
    
    # Controller module
    self._cntrl = Controller()

    def db_insert_contact_msg(self):

        '''
        db_insert_contact_msg inserts one new contact message into the PostgreSQL
        database table bristo_contacts_messages after contact/user availability 
        has been verified.  The serial ID, Time Date Stamp, Sender and Receiver
        are automatically generated.  Only the message need be entered.
        
        Need to set up thread with wait time for check messages after sending.
        '''
        self._cntrl.db_login()
        if self._cntrl._connected:
            self._cntrl.reset_timer()
            _sender = self._cntrl._user
            # Get username for current contact email address
            _usr_email = self._cntrl.fetch_results[self._cntrl._ITEM][self._cntrl._OEMAIL]
            _receiver = self.get_contact_username(_usr_email)
            _crow = self._cntrl.bristo_search.msgTableWidget.currentRow()
            _ccol = self._cntrl.bristo_search.msgTableWidget.currentColumn()
            _msg = self._cntrl.bristo_search.msgTableWidget.cellWidget(
                                                _crow,_ccol ).text()
            self._cntrl._cursor.execute("""INSERT INTO bristo_contacts_messages
                    (bristo_contacts_messages_sender,
                    bristo_contacts_messages_receiver,
                    bristo_contacts_messages_msg)
                    VALUES (%s,%s,%s);""", (_sender,  _receiver,  _msg))
            self._cntrl._conn.commit()
            self._cntrl.contactsStatusBar.showMessage('Message sent.......', 4000)
            self._cntrl.db_close()
    
    def check_messages(self):
        '''
        check_messages displays all messages in the bristo_contacts_messages
        database table that were sent by the current user to the current contact
        and that were sent by the current contact to the current user.
        '''
        self._cntrl.block_signals()
        self._cntrl.reset_timer()
        # Query the database to create list of messages returned by psycopg2
        # driver from the PostgreSQL database.
        _user = self_cntl._user
        _contct_email = self._cntrl.fetch_results[self._cntrl._ITEM][self._cntrl._OEMAIL]
        _contct_usrnm = self.get_contact_username(_contct_email)
        if _contct_usrnm:
            self._cntrl._cursor = self._conn.cursor()
            self._cntrl._cursor.execute("""SELECT * FROM bristo_contacts_messages WHERE
                    bristo_contacts_messages_sender = %s AND 
                    bristo_contacts_messages_receiver = %s OR
                    bristo_contacts_messages_sender = %s AND 
                    bristo_contacts_messages_receiver = %s
                    ORDER by bristo_contacts_messages_stamp 
                    LIMIT %s;""",
                    (_user, _contct_usrnm, _contct_usrnm, _user, self._cntrl._limit))
            self.fetch_msg = self._cntrl._cursor.fetchall() # Get messages
            self.display_messages(self.fetch_msg) # Display messages
            self._cntrl.contactsStatusBar.showMessage('Messages updated .......', 4000)
            self._cntrl.db_close()
            self._cntrl.unblock_signals()
            
        else:
            self._cntrl.contactsStatusBar.showMessage('User not found.....', 4000)
            self._cntrl.db_close()

    def get_contact_username(self,  _contact_email):
        '''
        get_contact_username accepts the contact email address and
        returns the contact username in bristo_contacts_users for a user
        email match.
        '''
        self._cntrl.db_login()
        if self._cntrl._connected:
            # Get username for current contact email address
            self._cntrl._cursor = self._conn.cursor()
            self._cntrl._cursor.execute("SELECT * FROM bristo_contacts_users WHERE \
            bristo_contacts_users_email = %s LIMIT %s", (
                _contact_email, self._limit))
            if not self._cntrl._cursor.rowcount:
                self._cntrl.contactsStatusBar.showMessage('User not found.....', 4000)
                self._cntrl.db_close()
            else:
                _usr = self._cntrl._cursor.fetchone()
                return _usr[self._cntrl._USERNM]
                
    def display_messages(self, _messages):
        '''
        display_messages accepts a message list returned by psycopg2 form a
        PostgreSQL database and displays these messages in the message
        table widget.
        '''
        _user = self._cntrl._user
        # Display the messages in msgTableWidget and make user sent messages
        # distinct (blue or dark or highlighted) while contact sent message are
        # displayed normally.
        self._cntrl.bristo_search.msgTableWidget.clearContents()
        _tblwgt_row = 0  # Changes each record
        _tblwgt_stamp = 2 # static
        _tblwgt_sender = 3 # static
        _tblwgt_msg = 5 # static
        for _msg in range(len(_messages)):
            
            _stamp = self.fetch_msg[_msg][_tblwgt_stamp].strftime(
            "%m/%d/%y %I:%M%p")
            _qwitem = QTableWidgetItem(_stamp)
            self._cntrl.bristo_search.msgTableWidget.setItem(_tblwgt_row, 
                _tblwgt_stamp, _qwitem)
                
            _sender = self.fetch_msg[_msg][_tblwgt_sender]
            _qwitem = QTableWidgetItem(_sender)
            self._cntrl.bristo_search.msgTableWidget.setItem(_tblwgt_row,
                _tblwgt_sender, _qwitem)
                
            _message = self.fetch_msg[_msg][_tblwgt_msg]
            _qwitem = QTableWidgetItem(_message)
            if _sender == _user:
                _qwitem.setForeground(QColor(65,105,225))
            self._cntrl.bristo_search.msgTableWidget.setItem(_tblwgt_row,
                _tblwgt_msg, _qwitem)
            _tblwgt_row += 1
