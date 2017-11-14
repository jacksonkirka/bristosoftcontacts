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
This secure module provides security for bristoSOFT Contacts v. 0.1.
It uses Python's hashlib, uuid and re modules.  A one way salted
hash is used to encrypt the user password.  The actual password is
not stored in the database.
'''
import hashlib
import uuid
import re

class Security:
    
    '''
    The Security class provides resources to maintain secure communication
    and authentication in contacts.
    '''
    def mincomplex(self, _pwd):
        r'''
        mincomplex evaluates a plain text password and returns true if the
        password evaluated contains 1) uppercase letter, 2) lowercase letter,
        3) a digit 0 - 9, 4) a special character and 5) is at least 8 characters.
        
        >>> sec = Security()
        >>> testone = sec.mincomplex('Bmw$4839')
        >>> testone
        True
        >>> testtwo = sec.mincomplex('bmw$28l4')
        >>> testtwo
        False
        >>> testthree = sec.mincomplex('2938clq;')
        >>> testthree
        False
        >>> 
        '''
        _digit = re.search('[0-9]', _pwd)
        _lower = re.search('[a-z]', _pwd)
        _upper = re.search('[A-Z]', _pwd)
        _special = re.search('.[!@#$%^&*()_~-]',_pwd)

        if len(_pwd) > 7 and _digit and _lower and _upper and _special:
            return True
        else:
            return False

    def hashpwd(self, _pwd):

        '''
        hashpwd hashes a password by NSA Secure Hash Algorithm 2 
        sha256 algorithm and adds a uuid prefix salt.
        
        >>> sec = Security()
        >>> hashed_password = sec.hashpwd('Bmw$535is')
        >>> match = sec.authenticatepwd(hashed_password,'Bmw$535is')
        >>> match
        True
        >>> 
        '''
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() +
            _pwd.encode()).hexdigest() + ':' + salt
            
    def authenticatepwd(self, _dbhashpwd, _usrpwd):

        '''
        authenticatepwd authenticates the password entered by the user by
        comparing the database hash with a hash of the user entered
        password.
        
        >>> sec = Security()
        >>> _usrpwd = 'Guest$123'
        >>> _dbhashpwd = sec.hashpwd('Guest$123')
        >>> match = sec.authenticatepwd(_dbhashpwd,_usrpwd)
        >>> match
        True
    
        '''
        dbpwd, salt = _dbhashpwd.split(':')
        return dbpwd == hashlib.sha256(salt.encode() +\
            _usrpwd.encode()).hexdigest()

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

        
