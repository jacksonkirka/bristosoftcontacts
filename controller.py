#!/usr/bin/python

# Imports
import sip # Needed for conversion to Python types
sip.setapi('QString', 2)
import datetime
import ntpath
import hashlib
import uuid
import os
from bristo_exceptions import *
import platform
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
# from PyQt4.uic import *
import psycopg2
from view import *
import contactsmain

# Version assignment
__version__ = '0.1'

# contactsdialog = loadUiType('contacts_combo.ui')[0]
#bristocontacts = loadUiType('contacts_main.ui')[0]
        
# class Controller(QMainWindow,  bristocontacts):
class Controller(QMainWindow, contactsmain.Ui_bristosoftContacts):
    '''
    
    Controller is the Main Application window with
    all the menus, toolbars, statusbar and more.
    
    '''

    def __init__(self, parent=None):
        '''
        
        This initialization class method initializes
        QMainWindow and the bristocontacts.
        
        '''
        super(Controller, self).__init__(parent)
        self.setupUi(self)
        
        # users
        self._user = None
        self._user_email = None
        self._user_webmail = None
        
        # Database constants cursor list return
        self._CONTACT = 0
        self._FIRSTCONTACT = 0
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
        
        # Table Rows
        self._table_rows_count = 2000
        
        # Notes
        self._stamp = 1
        self._note = 3
        self._notes_ct = 2
        self._note_column = 1
        
        self._displayed_apptsbydate = False

        # Image
        self._image = QPixmap()
        self._image_bin = None
        self._image_bytea = None
        self._image_buffer = None
        
        # File
        self._file_bin = None
        self._file_id = 0
        self._file_stamp = 1
        self._file_ct = 2
        self._file_name = 3
        self._file_file = 4
        
        #Calls
        self._calls_id = 0
        self._calls_ct_id = 1
        self._calls_stamp = 2
        self._calls_phone = 3
        self._calls_in = 4
        self._calls_results = 5
        self.live_set = False
        
        # Appointment
        self._appt_id = 0
        self._appt_ct_id = 1
        self._appt_stamp = 2
        self._appt_time = 3
        self._appt_complete = 4
        self._appt_purpose = 5
        self._display_appts_set = False
        
        # Calendar
        self._calendar_activated = False
        self._qcal_date = None
        
        #Date and Time
        self._DATE = datetime.datetime.now()
        self._TODAY = self._DATE.strftime("%m/%d/%y %I:%M%p")
        
        # Next/Prev
        self._NEXT = 0
        self._PREV = 0
        self._LASTCONTACT = 0
        
        
        # Set connected to false
        self.disconnected = False
        self.connected = False

        
        # Main Signals
        self.actionConnect.triggered.connect(self.db_connect)
        self.actionAbout_Qt.triggered.connect(self.aboutqt)
        self.actionAbout_bristoSOFT_Contacts.triggered.connect(
            self.aboutbristocontacts)
        self.actionConnect.triggered.connect(self.db_connect)
        self.actionNew.triggered.connect(self.db_contact_new)
        self.actionVacuum.triggered.connect(self.db_full_vacuum)
        self.actionReIndex.triggered.connect(self.db_reindex)
        self.actionDisconnect.triggered.connect(self.db_close)
        self.actionQuery.triggered.connect(self.db_contacts_fetch)
        self.actionQuit.triggered.connect(self.close_contacts)
        self.actionFirst_Contact.triggered.connect(self.db_contact_fetch_first)
        self.actionPrevious_Contact.triggered.connect(self.db_contact_prev)
        self.actionNext_Contact.triggered.connect(self.db_contact_next)
        self.actionLast_Contact.triggered.connect(self.db_contact_fetch_last)
        self.actionSearch.triggered.connect(self.db_fetch_contact)
        self.actionUpdate.triggered.connect(self.db_update_contact)
        
        
        # set contactsStatusBar to red
        self.contactsStatusBar.setStyleSheet("background-color: \
                                              rgb(230, 128, 128);")
    
        # Settings
        settings = QSettings()
        size = settings.value("MainWindow/Size",
                              QVariant(QSize(630, 735))).toSize()
        self.resize(size)
        position = settings.value("MainWindow/Position",
                                  QVariant(QPoint(320, 140))).toPoint()
        self.move(position)
        self.restoreState(settings.value("MainWindow/State").toByteArray())

        # Set Main Window Icon
        self.setWindowIcon(QIcon(":icons/family.ico"))
    
    # About class methods
    def aboutqt(self):
        '''
        
        aboutqt is the standard About Qt dialog built in to QT.
        
        '''
        mesg = QMessageBox()
        mesg.aboutQt(self,  'About Qt')
    
    def aboutbristocontacts(self):
        '''
        
        aboutbristocontacts QMessageBox displays information about
        bristoSOFT Contacts v. 0.1.
        
        '''
        QMessageBox.about(self, "About bristoSOFT Contacts v. 0.1",
        """ <b>About bristoSOFT Contacts</b> v %s
        <p>Copyright &copy; 2016 bristoSOFT 
        All rights reserved.
        <p>This is a PostgreSQL database contacts management system.  It is
        based on the PyQt frontend GUI.
        <p>Python %s - Qt %s - PyQt %s on %s""" % (
        __version__, platform.python_version(),
        QT_VERSION_STR, PYQT_VERSION_STR, platform.system()))
    
    # class Database Methods
    def db_connect(self):
        '''
        
        db_connect displays the login dialog and catches the signal accept()
        from the OK button then calls self.db_login.
        
        '''
        self.login = bristoContactsLogin()
        self.login.show()
        self.connect(self.login, SIGNAL('accepted()'),  self.db_login)

    def db_login(self):
        ''' 
        
        db_login establishes a connection to a PostgreSQL database on port 
        5423 with the standard connection string.
        
       
        
        '''
        
         # Step 1 owner authentication security string
        con = "host='ec2-54-221-225-43.compute-1.amazonaws.com' \
        dbname='dtg1rerulrimn' user='atvefqxquovzsq' \
        password='IJuYKnkKd6qwE08WSTpi5-RMEk' sslmode='require'"
        
        self._host = 'ec2-54-221-225-43.compute-1.amazonaws.com'
        self._db = 'dtg1rerulrimn'
         
        if self.login.userNameLineEdit.text() and \
            self.login.passwordLineEdit.text():
                
            self.conn = psycopg2.connect(con) # Authenticate and login owner
            self.connected = True # Set connection to True
            
        # Step 2 User database authentication
            
            # Save login credentials
            self._user = self.login.userNameLineEdit.text() # User Name
            _usr_nm = self._user # Set Text for User Name
            _usr_pwd = self.login.passwordLineEdit.text() # Set Text for pasword
            
            # Verify user name
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT bristo_contacts_users_name FROM \
            bristo_contacts_users WHERE bristo_contacts_users_name = %s", (
                self._user, ))
            _db_usrnm = self.cursor.fetchone()[0]
            self.cursor.close()
            if _usr_nm == _db_usrnm:
                _usr_nm_match = True
            else:
                _usr_nm_match = False
                
            # Verify user password
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT bristo_contacts_users_pwd FROM \
            bristo_contacts_users WHERE bristo_contacts_users_name = %s", (
                self._user, ))
            _db_usrpwdhash = self.cursor.fetchone()[0]
            _usr_pwd_match = self.authenticatepwd(_db_usrpwdhash,  _usr_pwd)
            
            if _usr_nm_match and _usr_pwd_match:
            
                # get user webmail link for contact filter
                self.cursor = self.conn.cursor()
                self.cursor.execute("SELECT bristo_contacts_users_webmail FROM \
                bristo_contacts_users WHERE bristo_contacts_users_name = %s", (
                    self._user, ))
                self._user_webmail_tuple = self.cursor.fetchone()
                self._user_webmail = self._user_webmail_tuple[0]
                self.cursor.close()
                
                if self.disconnected:
                    self.contactsStatusBar.removeWidget(self.conn_msg)
                self._date = datetime.datetime.now()
                self.conn_msg = QLabel("ssl:"+self._user +"@"+
                                        self._host+
                                      '/'+ self._db +'.')
                self.contactsStatusBar.setStyleSheet("background-color: \
                                                     rgb(179, 255, 188);")
                
                self.contactsStatusBar.addWidget(self.conn_msg)
    
    def hashpwd(self, _pwd):
        
        '''
        hashpwd hashes a password by NSA Secure Hash Algorithm 2 
        sha256 algorithm and adds a uuid prefix salt.
        '''
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() +\
            _pwd.encode()).hexdigest() + ':' + salt
            
        
    def authenticatepwd(self, _dbhashpwd, _usrpwd):
        
        '''
        authenticatepwd authenticates the password entered by the user by
        comparing the database hash with a hash of the user entered
        password.
        '''
        dbpwd, salt = _dbhashpwd.split(':')
        return dbpwd == hashlib.sha256(salt.encode() +\
            _usrpwd.encode()).hexdigest()
    
    def db_contact_new(self):
        
        '''
        
        db_record_new displays the new contact dialog and catches the signal accept()
        from the OK button then runs self.db_insert.
        
        '''
        # set contactsDialog in cetralWidget
        self.bristo = bristoContactsDialog()
        self.setCentralWidget(self.bristo)
        self.cursor = self.conn.cursor()
        self.bristo.accepted.connect(self.db_insert)
    
    
    def db_insert(self):
        '''
        
        db_insert inserts one new contact into the PostgreSQL database table with
        bytea picture.
        
        '''
        _company = self.bristo.companyLineEdit.text()
        _mrmrs = self.bristo.mrmrsLineEdit.text()
        _fname = self.bristo.firstNameLineEdit.text()
        _middle = self.bristo.middleNameLineEdit.text()
        _lname = self.bristo.lastNameLineEdit.text()
        _cred = self.bristo.credLineEdit.text()
        _addr = self.bristo.addressLineEdit.text()
        _suite = self.bristo.suiteLineEdit.text()
        _city = self.bristo.cityLineEdit.text()
        _st = self.bristo.stateLineEdit.text()
        _postal = self.bristo.postalLineEdit.text()
        _oph = self.bristo.officePhoneLineEdit.text()
        _cell = self.bristo.cellPhoneLineEdit.text()
        _fax = self.bristo.officeFaxLineEdit.text()
        _hph = self.bristo.homePhoneLineEdit.text()
        _oemail = self.bristo.officeEmailLineEdit.text()
        _pemail = self.bristo.personalEmailLineEdit.text()
        _oweb = self.bristo.officeWebLineEdit.text()
        _pweb = self.bristo.personalWebLineEdit.text()
        
        self.cursor.execute("""INSERT INTO bristo_contacts_ct
                (bristo_contacts_ct_co, bristo_contacts_ct_title,
                bristo_contacts_ct_fname, bristo_contacts_ct_middle,
                bristo_contacts_ct_lname, bristo_contacts_ct_cred,
                bristo_contacts_ct_addr1, bristo_contacts_ct_addr2,
                bristo_contacts_ct_city, bristo_contacts_ct_state,
                bristo_contacts_ct_postal, bristo_contacts_ct_ph_office,
                bristo_contacts_ct_ph_cell, bristo_contacts_ct_fax,
                bristo_contacts_ct_home,bristo_contacts_ct_email1,
                bristo_contacts_ct_email2, bristo_contacts_ct_web,
                bristo_contacts_ct_web2) VALUES (%s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""", 
                (_company,_mrmrs,_fname,_middle,_lname,
                _cred, _addr, _suite,_city,_st, _postal,_oph,_cell, _fax
                ,_hph,_oemail,_pemail,_oweb,_pweb))
        self.conn.commit()
        self.contactsStatusBar.showMessage('New Contact Inserted.', 3000)
    
    def db_contacts_fetch(self):
        '''
        
        db_record_fetch fetches all contacts at one time.
        self.fetch_result[0][1] is First contact, company name
        self.fetch_result is a python list returned by psycopg2 driver
        The list is then traversed in memory on the list python object.
        
        '''
        self.bristo_search = bristoContactsSearchDialog()
        
        # Hide columns on calls and appointments
        self.bristo_search.fileTableWidget.setColumnHidden(self._file_id,True)
        self.bristo_search.callsTableWidget.setColumnHidden(self._calls_id,  True)
        self.bristo_search.callsTableWidget.setColumnHidden(self._calls_ct_id,
            True)
        self.bristo_search.apptTableWidget.setColumnHidden(self._appt_id,  True)
        self.bristo_search.apptTableWidget.setColumnHidden(self._appt_ct_id,  True)
        self.bristo_search.apptTableWidget.setColumnHidden(self._appt_stamp,  True)
        self.live_set = False # Prevents Duplicate Live Widgets
        self._calendar_activated = False # User double clicked date on calendar
        self._displayed_apptsbydate = False # Appointments by date display once
        
        # set bristoMapper class
        self.google_com = bristoMapper()
        layout = QHBoxLayout()
        layout.addWidget(self.google_com)
        self.bristo_search.mapTabFrame.setLayout(layout)
        
        # set bristoMailFrame
        self.google_mail_com = bristoMailView()
        mail_layout = QHBoxLayout()
        mail_layout.addWidget(self.google_mail_com)
        self.bristo_search.emailFrame.setLayout(mail_layout)
        
        # Notes
        self.bristo_search.notesTableWidget.setHorizontalHeaderLabels(
            ['Time Stamp', 'Notes'])
            
        # Documents
        self.bristo_search.fileTableWidget.setHorizontalHeaderLabels(
            ['Id','Time Stamp', 'File Name'])
            
        self.active_dlg = 'search'
        self.setCentralWidget(self.bristo_search)
        
        # Phone Calls
        self.bristo_search.callsTableWidget.setHorizontalHeaderLabels(
            ['ID', 'CTID', 'Time Stamp', 'Phone/CID', 'IO', 'Results'])

        self.bristo_search.callsTableWidget.horizontalHeader().resizeSection(
            self._calls_stamp, 140)
        self.bristo_search.callsTableWidget.horizontalHeader().resizeSection(
            self._calls_phone, 140)
        self.bristo_search.callsTableWidget.horizontalHeader().resizeSection(
            self._calls_in, 22)
        
        # Appointments
        self.bristo_search.apptTableWidget.setHorizontalHeaderLabels(
            ['ID', 'CTID', 'Time Stamp', 'Date/Time', 'CO', 'Purpose'])

        self.bristo_search.apptTableWidget.horizontalHeader().resizeSection(
            self._appt_time, 150)
        self.bristo_search.apptTableWidget.horizontalHeader().resizeSection(
            self._appt_complete, 28)
        
        # Fetch Data from tables --> Python lists
        if self.connected:
            self.cursor = self.conn.cursor()
            _query = "SELECT * FROM bristo_contacts_ct ORDER by \
                bristo_contacts_ct_co, bristo_contacts_ct_lname"
            self.cursor.execute(_query)
            self.fetch_results = self.cursor.fetchall() # Gets all contacts from db
            _query = "SELECT * FROM bristo_contacts_notes ORDER by \
                bristo_contacts_notes_ct, bristo_contacts_notes_stamp"
            self.cursor.execute(_query)
            self.fetch_notes = self.cursor.fetchall() # Get all notes
            _query = "SELECT bristo_contacts_files_id,\
                bristo_contacts_files_stamp, bristo_contacts_files_ct,\
                bristo_contacts_files_name FROM\
                bristo_contacts_files ORDER by\
                bristo_contacts_files_ct, bristo_contacts_files_stamp"
            self.cursor.execute(_query)
            self.fetch_files = self.cursor.fetchall() # Get all files
            _query = "SELECT * FROM bristo_contacts_calls ORDER by \
                bristo_contacts_calls_ct_id, bristo_contacts_calls_stamp"
            self.cursor.execute(_query)
            self.fetch_calls = self.cursor.fetchall() # Get all calls
            _query = "SELECT * FROM bristo_contacts_appt ORDER by \
                bristo_contacts_appt_ct_id, bristo_contacts_appt_stamp"
            self.cursor.execute(_query)
            self.fetch_appts = self.cursor.fetchall() # Get all appointments
            self.update_fetch_results()
            _msg = 'All data fetched from database.  Click red x to clear memory.'
            self.contactsStatusBar.showMessage(_msg, 7000)
            
    def update_fetch_results(self):
        '''
        
        update_fetch_results reassigns the entire contact list during an
        update.
        
        '''
        
        self._LASTCONTACT = len(self.fetch_results) - 1
        self.bristo_search_dlg = False
        
        # Seach and update Signals
        self.bristo_search.picPushButton.clicked.connect(
            self.update_pic)
        self.bristo_search.notesTableWidget.cellChanged.connect(
                self.db_insert_contact_note)
        self.bristo_search.callsTableWidget.cellChanged.connect(
            self.db_insert_contact_call)
        self.bristo_search.apptTableWidget.cellChanged.connect(
            self.db_insert_update_appt)
        self.bristo_search.notesDetailPushButton.clicked.connect(
            self.resize_notes)
        self.bristo_search.callsDetailPushButton.clicked.connect(
            self.resize_calls)
        self.bristo_search.apptDetailPushButton.clicked.connect(
            self.resize_appts)
        self.bristo_search.filePushButton.clicked.connect(
            self.db_insert_contact_file)
        self.bristo_search.fileTableWidget.doubleClicked.connect(
            self.get_contact_file)
        self.bristo_search.refreshMapPushButton.clicked.connect(self.refresh_map)
        self.bristo_search.emailRefreshPushButton.clicked.connect(self.refresh_email)
        self.bristo_search.callsTableWidget.clicked.connect(self.live_call_widgets)
        self.bristo_search.apptTableWidget.clicked.connect(self.live_appt_widgets)
        self.bristo_search.calendarWidget.activated.connect(self.display_appts_bydate)
        
        self._CONTACT = self._FIRSTCONTACT
        self.display_data()
        
        
    def db_contact_fetch_first(self):
        '''
        
        db_contact_fetch_first fetches the first contact in the bristo_contacts_ct table.
        
        '''
        self._CONTACT = self._FIRSTCONTACT
        self.display_data()
    
    def db_contact_fetch_last(self):
        '''
        
        db_contact_fetch_first fetches the first contact in the bristo_contacts_ct table.
        
        '''
        self._CONTACT = self._LASTCONTACT
        self.display_data()


    def db_contact_prev(self):
        '''
        db_contact_prev fetches the previous contact before the current contact base on
        index in the python list self.fetch_results.
        '''
        if not self._CONTACT <= self._FIRSTCONTACT:
            self._CONTACT -= 1
            self.display_data()

    def db_contact_next(self):
        '''
        db_contact_next fetches the next contact after the current contact based on
        index in the python list self.fetch_results.
        '''
        if not self._CONTACT >= self._LASTCONTACT:
            self._CONTACT += 1
            self.display_data()
            
    def db_fetch_contact(self):
        '''
        
        db_fetch_contact fetches the first occurence of the company name
        entered in the company search field.  The database is already
        sorted by Company and then by Last name of contact.
        
        '''
        for _company_idx in range(self._LASTCONTACT):
            if self.fetch_results[_company_idx][self._COMPANY].find(
                self.bristo_search.companyLineEdit.text()) > -1:
                self._CONTACT = _company_idx
                self.display_data()
                return
        
        _msg = 'Pattern ' +"'"+self.bristo_search.companyLineEdit.text() + \
                       "'"+' not found.'
        self.contactsStatusBar.showMessage(_msg, 3000)
    
    def db_update_contact(self):
        '''

        db_update_contact updates the currently displayed contact in the
        the database.
        
        '''
        
        if self.connected:
            _current_id = str(self.fetch_results[self._CONTACT][self._ID])
            _company = self.bristo_search.companyLineEdit.text()
            _mrmrs = self.bristo_search.mrmrsLineEdit.text()
            _fname = self.bristo_search.firstNameLineEdit.text()
            _middle = self.bristo_search.middleNameLineEdit.text()
            _lname = self.bristo_search.lastNameLineEdit.text()
            _cred = self.bristo_search.credLineEdit.text()
            _addr = self.bristo_search.addressLineEdit.text()
            _suite = self.bristo_search.suiteLineEdit.text()
            _city = self.bristo_search.cityLineEdit.text()
            _st = self.bristo_search.stateLineEdit.text()
            _postal = self.bristo_search.postalLineEdit.text()
            _oph = self.bristo_search.officePhoneLineEdit.text()
            _cell = self.bristo_search.cellPhoneLineEdit.text()
            _fax = self.bristo_search.officeFaxLineEdit.text()
            _hph = self.bristo_search.homePhoneLineEdit.text()
            _oemail = self.bristo_search.officeEmailLineEdit.text()
            _pemail = self.bristo_search.personalEmailLineEdit.text()
            _oweb = self.bristo_search.officeWebLineEdit.text()
            _pweb = self.bristo_search.personalWebLineEdit.text()
            
            self.cursor.execute("""UPDATE bristo_contacts_ct SET
                (bristo_contacts_ct_co, bristo_contacts_ct_title,
                bristo_contacts_ct_fname, bristo_contacts_ct_middle,
                bristo_contacts_ct_lname, bristo_contacts_ct_cred,
                bristo_contacts_ct_addr1, bristo_contacts_ct_addr2,
                bristo_contacts_ct_city, bristo_contacts_ct_state,
                bristo_contacts_ct_postal, bristo_contacts_ct_ph_office,
                bristo_contacts_ct_ph_cell, bristo_contacts_ct_fax,
                bristo_contacts_ct_home, bristo_contacts_ct_email1,
                bristo_contacts_ct_email2, bristo_contacts_ct_web,
                bristo_contacts_ct_web2) = (%s,%s,%s,%s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s) WHERE
                bristo_contacts_ct_id = %s;""", (_company,_mrmrs,
                _fname,_middle,_lname,_cred, _addr, _suite,_city,_st,_postal,
                _oph,_cell,_fax, _hph,_oemail,_pemail,_oweb,_pweb, _current_id))
                
            self.conn.commit()
            self.contactsStatusBar.showMessage('Contact Updated.', 3000)
  
        
    def display_data(self):
        '''
        
        display_data simply displays a contact based on the contact
        index integer value in self_CONTACT.
        
        '''
        self.resize_mode_zero()
        self.block_signals()
        self.display_contact()
        self.display_notes()
        self.display_files()
        self.display_calls()
        self.display_appts()
        self.display_msg()
        self.unblock_signals()
        
    def display_data_not_appts(self):
        
        '''
        display_data_not_appts displays all info on contact without updating the
        contact appointments.  This is needed to allow appoints selected by the
        calendar date to display a contact without overwriting the calendar list
        of appointments for that day.
        '''
        self.resize_mode_zero()
        self.block_signals()
        self.display_contact()
        self.display_notes()
        self.display_files()
        self.display_calls()
        self.display_msg()
        self.unblock_signals()
        
        
    def resize_mode_zero(self):
        '''
        resize_mode_zero sets the resize mode to zero for the Table Widgets to
        zero.  There after they may be reset by clicking the resize buttons.
        '''
        
        self.bristo_search.notesTableWidget.verticalHeader().setResizeMode(0)
        self.bristo_search.callsTableWidget.verticalHeader().setResizeMode(0)
        self.bristo_search.apptTableWidget.verticalHeader().setResizeMode(0) 
    
    def block_signals(self):
        '''
        block_signals blocks all signals during the loading of data to widgets.
        This needed to prevent cellChanged signals from being activated during
        programatic loading of data to the widgets.
        '''
        
        self.bristo_search.notesTableWidget.blockSignals(True) # block during load
        self.bristo_search.callsTableWidget.blockSignals(True)
        self.bristo_search.apptTableWidget.blockSignals(True)
        
    def display_contact(self):
        '''
        display_contact displays contact information to the contact and address tabs.
        '''

        self.bristo_search.companyLineEdit.setText(
            self.fetch_results[self._CONTACT][self._COMPANY])
        self.bristo_search.mrmrsLineEdit.setText(
            self.fetch_results[self._CONTACT][self._MRMRS])
        self.bristo_search.firstNameLineEdit.setText(
            self.fetch_results[self._CONTACT][self._FNAME])
        self.bristo_search.middleNameLineEdit.setText(
            self.fetch_results[self._CONTACT][self._MIDDLE])
        self.bristo_search.lastNameLineEdit.setText(
            self.fetch_results[self._CONTACT][self._LNAME])
        self.bristo_search.credLineEdit.setText(
            self.fetch_results[self._CONTACT][self._CRED])
        self.bristo_search.addressLineEdit.setText(
            self.fetch_results[self._CONTACT][self._ADDR])
        self.bristo_search.suiteLineEdit.setText(
            self.fetch_results[self._CONTACT][self._SUITE])
        self.bristo_search.cityLineEdit.setText(
            self.fetch_results[self._CONTACT][self._CITY])
        self.bristo_search.stateLineEdit.setText(
            self.fetch_results[self._CONTACT][self._ST])
        self.bristo_search.postalLineEdit.setText(
            self.fetch_results[self._CONTACT][self._POSTAL])
        self.bristo_search.officePhoneLineEdit.setText(
            self.fetch_results[self._CONTACT][self._OPHONE])
        self.bristo_search.cellPhoneLineEdit.setText(
            self.fetch_results[self._CONTACT][self._CELL])
        self.bristo_search.officeFaxLineEdit.setText(
            self.fetch_results[self._CONTACT][self._FAX])
        self.bristo_search.homePhoneLineEdit.setText(
            self.fetch_results[self._CONTACT][self._HPHONE])
        self.bristo_search.officeEmailLineEdit.setText(
            self.fetch_results[self._CONTACT][self._OEMAIL])
        self.bristo_search.personalEmailLineEdit.setText(
            self.fetch_results[self._CONTACT][self._PEMAIL])
        self.bristo_search.officeWebLineEdit.setText(
            self.fetch_results[self._CONTACT][self._OWEB])
        self.bristo_search.personalWebLineEdit.setText(
            self.fetch_results[self._CONTACT][self._PWEB])
        self._image_bytea = self.fetch_results[self._CONTACT][self._PIC]
        self.display_pic(self._image_bytea)
        
    def display_notes(self):
        
        '''
        display_notes display notes in the notes tab.
        '''
        self.bristo_search.notesTableWidget.clearContents()
        _tblwgt_row = 0  # Changes each record
        _tblwgt_date = 0 # static
        _tblwgt_note_col = 1 # static
        for _contact_note in range(len(self.fetch_notes)):
            if self.fetch_notes[_contact_note][self._notes_ct] ==\
                self.fetch_results[self._CONTACT][self._OPHONE]:
                _date_row = self.fetch_notes[_contact_note][self._stamp].strftime(
                "%m/%d/%y %I:%M%p")
                _qwitem = QTableWidgetItem(_date_row)
                self.bristo_search.notesTableWidget.setItem(_tblwgt_row, 
                    _tblwgt_date, _qwitem)
                _notes_row = self.fetch_notes[_contact_note][self._note]
                _qwitem = QTableWidgetItem(_notes_row)
                self.bristo_search.notesTableWidget.setItem(_tblwgt_row,
                    _tblwgt_note_col, _qwitem)
                _tblwgt_row += 1
                
    def display_files(self):
        
        '''
        disply_files displays files in the files tab.
        '''
        self.bristo_search.fileTableWidget.clearContents()
        _tblwgt_file_row = 0  # Changes each record
        _tblwgt_file_id = 0
        _tblwgt_date = 1 # static
        _tblwgt_filename_col = 2 # static
        for _contact_file in range(len(self.fetch_files)):
            if self.fetch_files[_contact_file][self._file_ct] ==\
                self.fetch_results[self._CONTACT][self._OPHONE]:
                _id_row = str(self.fetch_files[_contact_file][self._file_id])
                _qwitem = QTableWidgetItem(_id_row)
                self.bristo_search.fileTableWidget.setItem(_tblwgt_file_row,
                    _tblwgt_file_id, _qwitem)
                _date_row = self.fetch_files[_contact_file][self._file_stamp].strftime(
                "%m/%d/%y %I:%M%p")
                _qwitem = QTableWidgetItem(_date_row)
                self.bristo_search.fileTableWidget.setItem(_tblwgt_file_row, 
                    _tblwgt_date, _qwitem)
                _file_row = self.fetch_files[_contact_file][self._file_name]
                _qwitem = QTableWidgetItem(_file_row)
                self.bristo_search.fileTableWidget.setItem(_tblwgt_file_row,
                    _tblwgt_filename_col, _qwitem)
                _tblwgt_file_row += 1
                
    def display_calls(self):
        
        '''
        display calls displays telephone calls in the calls tab.
        '''
        self.bristo_search.callsTableWidget.clearContents()
        _tblwgt_calls_row = 0  # dynamic
        _tblwgt_calls_date = 2 # static
        _tblwgt_phone_col = 3 #static
        _tblwgt_in_col = 4 # static
        _tblwgt_results_col = 5 # static
        
        for _contact_call in range(len(self.fetch_calls)):
            if self.fetch_calls[_contact_call][self._calls_ct_id] ==\
                self.fetch_results[self._CONTACT][self._ID]:
                _date_row = self.fetch_calls[_contact_call][self._calls_stamp].strftime(
                "%m/%d/%y %I:%M%p")
                _qwitem = QTableWidgetItem(_date_row)
                self.bristo_search.callsTableWidget.setItem(_tblwgt_calls_row, 
                    _tblwgt_calls_date, _qwitem)
                _phone_row = self.fetch_calls[_contact_call][self._calls_phone]
                _qwitem = QTableWidgetItem(_phone_row)
                self.bristo_search.callsTableWidget.setItem(_tblwgt_calls_row,
                    _tblwgt_phone_col, _qwitem)
                _in_row = self.fetch_calls[_contact_call][self._calls_in]
                if _in_row:
                    _in_row = 'I'
                else:
                    _in_row = 'O'
                _qwitem = QTableWidgetItem(_in_row)
                self.bristo_search.callsTableWidget.setItem(_tblwgt_calls_row,
                    _tblwgt_in_col, _qwitem)
                _results_row = self.fetch_calls[_contact_call][self._calls_results]
                _qwitem = QTableWidgetItem(_results_row)
                self.bristo_search.callsTableWidget.setItem(_tblwgt_calls_row,
                    _tblwgt_results_col, _qwitem)
                _tblwgt_calls_row += 1
                
    def display_appts_by_date(self):

        '''
        display_appts displays appointments in the appointments tab.
        '''
        _tblwgt_appt_row = 0  # dynamic
        _tblwgt_id_col = 0 # static
        _tblwgt_ct_id = 1 # static
        _tblwgt_appt_date = 3 # static
        _tblwgt_complete_col = 4 #static
        _tblwgt_purpose_col = 5 # static
        self.bristo_search.apptTableWidget.clearContents()
        for _contact_appt in range(len(self.fetch_appts)):
            if (self._calendar_activated and\
                self.fetch_appts[_contact_appt][self._appt_time].date().isoformat()\
                 == self._qcal_date.toPyDate().isoformat()):
                _id_row = str(self.fetch_appts[_contact_appt][self._appt_id])
                _qwitem = QTableWidgetItem(_id_row)
                self.bristo_search.apptTableWidget.setItem(_tblwgt_appt_row,
                    _tblwgt_id_col, _qwitem)
                _ct_id_row = str(self.fetch_appts[_contact_appt][self._appt_ct_id])
                _qwitem = QTableWidgetItem(_ct_id_row)
                self.bristo_search.apptTableWidget.setItem(_tblwgt_appt_row,
                    _tblwgt_ct_id,  _qwitem)
                _date_row = self.fetch_appts[_contact_appt][self._appt_time].strftime(
                "%m/%d/%y %I:%M%p")
                _qwitem = QTableWidgetItem(_date_row)
                self.bristo_search.apptTableWidget.setItem(_tblwgt_appt_row, 
                    _tblwgt_appt_date, _qwitem)
                _complete_row = self.fetch_appts[_contact_appt][self._appt_complete]
                if _complete_row:
                    _complete_row = 'C'
                else:
                    _complete_row = 'O'
                _qwitem = QTableWidgetItem(_complete_row)
                self.bristo_search.apptTableWidget.setItem(_tblwgt_appt_row,
                    _tblwgt_complete_col, _qwitem)
                _purpose_row = self.fetch_appts[_contact_appt][self._appt_purpose]
                _qwitem = QTableWidgetItem(_purpose_row)
                self.bristo_search.apptTableWidget.setItem(_tblwgt_appt_row,
                    _tblwgt_purpose_col, _qwitem)
                _tblwgt_appt_row += 1
        self._calendar_activated = False
        self._display_appts_set = False
        
    def display_appts(self):

        '''
        display_appts displays appointments in the appointments tab.
        '''
        _tblwgt_appt_row = 0  # dynamic
        _tblwgt_id_col = 0 # static
        _tblwgt_ct_id = 1 # static
        _tblwgt_appt_date = 3 # static
        _tblwgt_complete_col = 4 #static
        _tblwgt_purpose_col = 5 # static
        self.bristo_search.apptTableWidget.clearContents()
        for _contact_appt in range(len(self.fetch_appts)):
            if self.fetch_appts[_contact_appt][self._appt_ct_id] ==\
                self.fetch_results[self._CONTACT][self._ID]:
                _id_row = str(self.fetch_appts[_contact_appt][self._appt_id])
                _qwitem = QTableWidgetItem(_id_row)
                self.bristo_search.apptTableWidget.setItem(_tblwgt_appt_row,
                    _tblwgt_id_col, _qwitem)
                _ct_id_row = str(self.fetch_appts[_contact_appt][self._appt_ct_id])
                _qwitem = QTableWidgetItem(_ct_id_row)
                self.bristo_search.apptTableWidget.setItem(_tblwgt_appt_row,
                    _tblwgt_ct_id,  _qwitem)
                _date_row = self.fetch_appts[_contact_appt][self._appt_time].strftime(
                "%m/%d/%y %I:%M%p")
                _qwitem = QTableWidgetItem(_date_row)
                self.bristo_search.apptTableWidget.setItem(_tblwgt_appt_row, 
                    _tblwgt_appt_date, _qwitem)
                _complete_row = self.fetch_appts[_contact_appt][self._appt_complete]
                if _complete_row:
                    _complete_row = 'C'
                else:
                    _complete_row = 'O'
                _qwitem = QTableWidgetItem(_complete_row)
                self.bristo_search.apptTableWidget.setItem(_tblwgt_appt_row,
                    _tblwgt_complete_col, _qwitem)
                _purpose_row = self.fetch_appts[_contact_appt][self._appt_purpose]
                _qwitem = QTableWidgetItem(_purpose_row)
                self.bristo_search.apptTableWidget.setItem(_tblwgt_appt_row,
                    _tblwgt_purpose_col, _qwitem)
                _tblwgt_appt_row += 1
        self._display_appts_set = True

    def display_msg(self):
        
        '''
        display_msg displays a message in the status bar after update of information.
        '''
        _msg = 'Contact, notes, files, calls '+str(self._CONTACT+1)+" of "\
        +str(self._LASTCONTACT+1)+" and map url fetched and loaded."
        self.contactsStatusBar.showMessage(_msg, 3000)
    
    def unblock_signals(self):
        
        '''
        unblock_signals unblocks all signals after information has been loaded.
        '''
        
        self.bristo_search.notesTableWidget.blockSignals(False) #unblock for update
        self.bristo_search.callsTableWidget.blockSignals(False) 
        self.bristo_search.apptTableWidget.blockSignals(False)
        
    
    def refresh_map(self):
        
        '''
        refresh_map refreshes the google map page when the user clicks the refresh
        button.
        '''
        _map_addr = self.fetch_results[self._CONTACT][self._ADDR]
        _map_zip = self.fetch_results[self._CONTACT][self._POSTAL]
        _google = 'https://www.google.com/maps/place/'
        _loc = _google+_map_addr+_map_zip
        self.google_com.load(QUrl(_loc))

    def refresh_email(self):
    
        '''
        refresh_map refreshes the google map page when the user clicks the refresh
        button.
        '''
       
        _email_addr_filter = self.fetch_results[self._CONTACT][self._OEMAIL]
        _mail_search = self._user_webmail
        if self._calendar_activated:
            _date = self._qcal_date.toPyDate().strftime("%A %B %d, %Y")
            _loc = _mail_search + _date
        else:
            _loc = _mail_search + _email_addr_filter
        self.google_mail_com.load(QUrl(_loc))
        
    def db_insert_contact_note(self):
        
        '''
        db_insert inserts one new contact note into the PostgreSQL database table
        bristo_contacts_notes.  The serial ID, Time Date Stamp are automatically
        generated.  Only the foreign key office phone primary key for 
        bristo_contacts_ct lookup value and notice itself need be entered.
        
        '''
        _crow = self.bristo_search.notesTableWidget.currentRow()
        _ccol = self.bristo_search.notesTableWidget.currentColumn()
        _oph = self.bristo_search.officePhoneLineEdit.text()
        _note = self.bristo_search.notesTableWidget.cellWidget(
                                            _crow,_ccol ).text()
        
        self.cursor.execute("""INSERT INTO bristo_contacts_notes
                (bristo_contacts_notes_ct, bristo_contacts_notes_note)
                VALUES (%s,%s);""", (_oph,_note))
        self.conn.commit()
        self.contactsStatusBar.showMessage('New Contact Note Inserted.', 3000)
    
    def resize_notes(self):
        
        '''
        resize_notes resets the table widget resize mode to resize to contents.
        '''
        
        self.bristo_search.notesTableWidget.verticalHeader().setResizeMode(3)
    
    def resize_calls(self):
        
        '''
        resize_calls resets the table widget resize mode to resize to contents.
        '''
        
        self.bristo_search.callsTableWidget.verticalHeader().setResizeMode(3) 
        
    def resize_appts(self):
        
        '''
        resize_appts resets the table widget resize mode to resize to contents.
        '''
        
        self.bristo_search.apptTableWidget.verticalHeader().setResizeMode(3) 
        
    def db_insert_contact_file(self):
        
        '''
        db_insert_contact_file inserts one file into the PostgreSQL database table
        bristo_contacts_files.  The serial ID, Time Date Stamp are automatically
        generated.  Only the foreign key office phone primary key for 
        bristo_contacts_ct lookup value, file name and file need be entered.
        
        '''
        _oph = self.bristo_search.officePhoneLineEdit.text()
        fdlg = QFileDialog()                               
        filename = fdlg.getOpenFileName(self, 'Open file', 
                   "Image files (*.jpg *.gif *.png)")       # Get Filename Path
        _fnm = self.get_path_filename(filename)             # Get name to write
        self._file_bin = open(filename, 'rb').read()        # Read > pointer
        if self.connected:
            self.cursor.execute("""INSERT INTO bristo_contacts_files
               (bristo_contacts_files_ct, bristo_contacts_files_name,
                   bristo_contacts_files_file)
               VALUES (%s, %s, %s); """, 
               (_oph, _fnm, psycopg2.Binary(self._file_bin)))
            self.conn.commit()
            self.contactsStatusBar.showMessage('New contact file inserted.', 3000)
    
    def get_contact_file(self):
        
        '''
        get_contact_file retrieves binary files from the database and saves them to
        the users desktop.
        '''
        
        _crow = self.bristo_search.fileTableWidget.currentRow() # Critical tested
        _ccol = self._file_id
        _file_id = self.bristo_search.fileTableWidget.item(_crow, _ccol).text()
        self.cursor.execute("SELECT * FROM\
            bristo_contacts_files WHERE bristo_contacts_files_id = %s", (_file_id,))
        _file_row = self.cursor.fetchone()
        _file_row_name = _file_row[self._file_name]
        _file = _file_row[self._file_file] # binary file
        path = os.path.join(os.path.expanduser("~"), "Desktop", _file_row_name)
        with open(path, 'wb') as f:
            f.write(_file) # writes file to desktop
            f.close()      # close file
        self.contactsStatusBar.showMessage(_file_row_name+' '\
                                           +'saved on Desktop.', 2000)
    
    def get_path_filename(self,  _path):
        
        '''
        get_path_filename extracts linux/windows/mac 
        filenames from a path and returns them.
        '''
        
        head, tail = ntpath.split(_path)
        return tail

    def update_pic(self):
    
        '''
        update_pic opens a picture provided by the PostgreSQL database user
        and displays it then returns self._image_bin to the caller dialog.
        '''
        
        fdlg = QFileDialog()                               
        fname = fdlg.getOpenFileName(self, 'Open file', 
                   "Image files (*.jpg *.gif *.png)")       # Get Filename
        self._image = QPixmap(fname)                        # Get Pixmap
        self._image_bin = open(fname, 'rb').read()          # Read > pointer
        self.bristo_search.picLabel.setPixmap(self._image)  # Display
        if self.connected:
            _company = self.bristo_search.companyLineEdit.text()
            _fname = self.bristo_search.firstNameLineEdit.text()
            _lname = self.bristo_search.lastNameLineEdit.text()
       
            self.cursor.execute("""UPDATE bristo_contacts_ct SET
               (bristo_contacts_ct_picture)
               = (%s) WHERE bristo_contacts_ct_co = %s 
               AND bristo_contacts_ct_fname = %s AND
               bristo_contacts_ct_lname =%s;""", 
               (psycopg2.Binary(self._image_bin), _company,
               _fname,_lname ))
            self.conn.commit()
            self.contactsStatusBar.showMessage('Contact picture updated.', 3000)
            
    def display_pic(self,  _buffer):
        '''
        
        display_pic accepts a buffer returned by a psycopg2 driver from a
        PostgreSQL database and displays a QPixmap to a widget ie QDialog.
        
        '''
        picture = bytes(_buffer)                            # Unpack to bytes
        p = QPixmap()                                       # Create QPixmap
        p.loadFromData(picture)                             # Load Picture
        self.bristo_search.picLabel.setPixmap(p)            # Display Picture
        
    def live_call_widgets(self):
        '''
        live_widgets is a bristosoft native abstract idea.  It postulates that
        resources should be allocated just in time.  This class method creates
        live widgets where they are needed at dataentry time on the fly ie
        live.  The live widgets require a boolean object for control set/not set.
        '''
        if not self.live_set:
            _crow = self.bristo_search.callsTableWidget.currentRow()
            self.live_combobox = QComboBox()
            self.bristo_search.callsTableWidget.setCellWidget(
                   _crow, self._calls_phone, self.live_combobox)
            self.live_combobox.setFrame(False)
            self.live_combobox.setEditable(True)
            self.live_combobox.addItem(self.fetch_results[self._CONTACT][self._OPHONE])
            self.live_combobox.addItem(self.fetch_results[self._CONTACT][self._CELL])
            self.live_combobox.addItem(self.fetch_results[self._CONTACT][self._HPHONE])
            self.live_chkbox = QCheckBox()
            self.bristo_search.callsTableWidget.setCellWidget(
                   _crow, self._calls_in, self.live_chkbox)
            self.live_set = True # Prevents Dupes on selection
    
    def db_insert_contact_call(self):
        
        '''
        db_insert_contact_call inserts one new contact call into the PostgreSQL 
        database table bristo_contacts_calls.  The serial ID, Time Date Stamp 
        are automatically generated.  Only the phone number called, inbound or 
        or outbound and results need be entered.
        
        '''
        _id = 0
        _crow = self.bristo_search.callsTableWidget.currentRow()
        _id_ct = str(self.fetch_results[self._CONTACT][_id])
        _ph = self.live_combobox.currentText()
        _in = self.live_chkbox.isChecked()
        _results = self.bristo_search.callsTableWidget.cellWidget(
            _crow, self._calls_results).text()
        
        self.cursor.execute("""INSERT INTO bristo_contacts_calls
                (bristo_contacts_calls_ct_id, bristo_contacts_calls_phone,
                bristo_contacts_calls_type, bristo_contacts_calls_results)
                VALUES (%s,%s, %s, %s);""", (_id_ct, _ph,_in, _results))
        self.conn.commit()
        self.live_set = False
        self.contactsStatusBar.showMessage('New Contact Call Inserted.', 5000)
        
    def appt_display_contact(self):
        
        _ccol = self._appt_ct_id
        _crow = self.bristo_search.apptTableWidget.currentRow()
        if self.bristo_search.apptTableWidget.item(
               _crow,  self._appt_id) is None:
                   return
        _contact_id = int(self.bristo_search.apptTableWidget.item(_crow,
            _ccol).text())
        for _index in range(len(self.fetch_results)):
            if self.fetch_results[_index][self._ID] == _contact_id:
                break
        self._CONTACT = _index
        self.display_data_not_appts()
    

    def live_appt_widgets(self):
        '''
        live_appt_widgets displays live Date and checkbox widgets to use live.
        '''
        if not self._display_appts_set:
            self.appt_display_contact()  
        if not self.live_set:
            _crow = self.bristo_search.apptTableWidget.currentRow()
            self.live_chkbox = QCheckBox()
            self.bristo_search.apptTableWidget.setCellWidget(
                   _crow, self._appt_complete, self.live_chkbox)
            if self.bristo_search.apptTableWidget.item(
               _crow,  self._appt_id) is None:
                self.live_dtimeedit = QDateTimeEdit()
                self.live_dtimeedit.setCalendarPopup(True)
                self.bristo_search.apptTableWidget.setCellWidget(
                       _crow, self._appt_time, self.live_dtimeedit)
            self.live_set = True # Prevents Dupes on selection
              

            
    def db_insert_update_appt(self):
        '''
        db_insert_update_appt calls either insert or update appointment methods
        dependent on whether the current row is empty or not.
        '''
        _crow = self.bristo_search.apptTableWidget.currentRow()
        if self.bristo_search.apptTableWidget.item(
                _crow,  self._appt_id) is None:
            self.db_insert_contact_appt()
        else:
            self.db_update_contact_appt()

    
    def db_insert_contact_appt(self):
        
        '''
        db_insert_contact_appt inserts one new contact appointment into the 
        PostgreSQL database table bristo_contacts_appt.  The serial ID, 
        Time Date Stamp are automatically generated.  Only the date/time of
        the appointment, open or closed and purpose need be entered.
        
        '''
        
        _crow = self.bristo_search.apptTableWidget.currentRow()
        _id_ct = str(self.fetch_results[self._CONTACT][self._ID])
        _qtime = self.live_dtimeedit.dateTime()
        _time = _qtime.toPyDateTime()
        _closed = self.live_chkbox.isChecked()
        _purpose = self.bristo_search.apptTableWidget.cellWidget(
            _crow, self._appt_purpose).text()
        
        self.cursor.execute("""INSERT INTO bristo_contacts_appt
                (bristo_contacts_appt_ct_id, bristo_contacts_appt_time,
                bristo_contacts_appt_complete, bristo_contacts_appt_purpose)
                VALUES (%s,%s, %s, %s);""", (_id_ct, _time,_closed, _purpose))
        self.conn.commit()
        self.live_set = False
        self.contactsStatusBar.showMessage('New Contact Appointment Inserted.', 5000)
        
    def db_update_contact_appt(self):
        
        '''
        db_update_contact_appt updates a contact appointment in the 
        PostgreSQL database table bristo_contacts_appt.  Only the
        complete/open checkbox and purpose can be updated.
        
        '''
        
        _crow = self.bristo_search.apptTableWidget.currentRow()
        _appt_id = self.bristo_search.apptTableWidget.item(
            _crow,  self._appt_id).text()
        _closed = self.live_chkbox.isChecked()
        _purpose = self.bristo_search.apptTableWidget.cellWidget(
            _crow, self._appt_purpose).text()
        
        self.cursor.execute("""UPDATE bristo_contacts_appt SET
                (bristo_contacts_appt_complete, bristo_contacts_appt_purpose)
                = (%s,%s) WHERE bristo_contacts_appt_id = %s;""", (_closed,
                _purpose, _appt_id))
        self.conn.commit()
        self.live_set = False
        self.contactsStatusBar.showMessage('Contact Appointment Updated.', 5000)
    
    def display_appts_bydate(self):
        
        '''
        display_appts_bydate accepts the date double clicked by the calendar.
        It then displays all scheduled items for that date.
        '''
        
        self._calendar_activated = True
        self._displayed_apptsbydate = False
        self._qcal_date = self.bristo_search.calendarWidget.selectedDate()
        self.contactsStatusBar.showMessage('Calendar date activated.', 5000)
        self.block_signals()
        self.display_appts_by_date()
        self.unblock_signals()
       
    
    def db_full_vacuum(self):
        '''
        
        db_full_vacuum does a complete vacuum of the database.
        
        '''
        if self.connected:
            self.cursor = self.conn.cursor()
            old_isolation_level = self.conn.isolation_level
            self.conn.set_isolation_level(0)
            self.query = "VACUUM FULL"
            self._doQuery(self.query)
            self.conn.set_isolation_level(old_isolation_level)
            _msg ='Vacumming Database '+self._db+' complete.'
            self.contactsStatusBar.showMessage(_msg, 5000)
            self.cursor.close()
        else:
            _msg = 'Please connect to the database to vacuum.'
            self.contactsStatusBar.showMessage(_msg, 5000)
            
    def db_reindex(self):
        '''
        
        db_reindex reindexes the database bristo_contacts_ct.
        
        '''
        if self.connected:
            self.cursor = self.conn.cursor()
            old_isolation_level = self.conn.isolation_level
            self.conn.set_isolation_level(0)
            self.query = 'REINDEX DATABASE bristocontacts'
            self._doQuery(self.query)
            self.conn.set_isolation_level(old_isolation_level)
            _msg = 'Reindexing '+self._db+' is complete.'
            self.contactsStatusBar.showMessage(_msg,  5000)
            self.cursor.close()
        else:
            _msg = 'Please connect to the database to reindex.'
            self.contactsStatusBar.showMessage(_msg, 5000)

    def _doQuery(self, query):
        '''
        
        _doQuery performs a query with a cursor and then commits the
        transaction.
        
        '''
        self.cursor.execute(query)
        self.conn.commit()
    
    def db_close(self):
        '''
        
        db_close closing the current cursor if any and database connection.  It
        then turns the status bar red.
        
        '''
        self.conn.close()
        self.connected = False
        self.contactsStatusBar.setStyleSheet("background-color: \
                                              rgb(230, 128, 128);")
        self.contactsStatusBar.removeWidget(self.conn_msg)
        self.conn_msg = QLabel(self._host+
                                  '/'+ self._db+'.')
        self.contactsStatusBar.addWidget(self.conn_msg)
        self.disconnected = True
    
    def close_contacts(self):
        '''
        
        close_contacts close closes the current database connection
        and closes bristoSOFT Contacts.
        
        '''
        if self.connected:
            self.conn.close()
            self.contactsStatusBar.setStyleSheet("background-color: \
                                              rgb(230, 128, 128);")
            self.contactsStatusBar.removeWidget(self.conn_msg)
            self.conn_msg = QLabel(self._host+
                                  '/'+ self._db+'.')
            self.contactsStatusBar.addWidget(self.conn_msg)
                                              
        self.close()
