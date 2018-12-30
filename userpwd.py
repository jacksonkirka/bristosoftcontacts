#!/usr/bin/python

import uuid
import hashlib

def hashpwd(_pwd):
        
    '''
    hashpwd hashes a password by NSA Secure Hash Algorithm 2 
    sha256 algorithm and adds a uuid prefix salt.
    '''
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() +\
        _pwd.encode()).hexdigest() + ':' + salt

passwd = input('Please enter password to hash: ')

print(passwd)
print(hashpwd(passwd))
