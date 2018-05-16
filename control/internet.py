#!/usr/bin/python2
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
#
'''
This internet.py module provides testing of the existence, reliability and 
performance of an internet connection.
'''

import urllib2
import socket

class InternetConnection:

    def inet_request(_url):
        '''
        inet_request accepts a url and returns true or false booleans.
        '''
        try:
            urllib2.urlopen(_url,timeout=30)
            return True
        except urllib2.URLError:
            return False
    

    def inet_socket_request(hostname):
        '''
        inet_socket_reuqest accepts a url and returns true or false booleans.
        '''
        try:
            host = socket.gethostbyname(hostname) # resolve hostname
            socket.create_connection((host, 80), 2) # connect
            return True
        except:
            return False

class InternetReliability:
    pass
    
class InternetPerformance:
    pass

