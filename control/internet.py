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

class InternetConnection:

    def internet_request(_url):
        '''
        internet_request accepts a url and returns true or false booleans.
        '''
        try:
            urllib2.urlopen(_url,timeout=30)
            return True
        except urllib2.URLError:
            return False

class InternetReliability:
    pass
    
class InternetPerformance:
    pass

