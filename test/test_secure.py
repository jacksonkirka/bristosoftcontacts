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
#
# Note: Testing can be done using perhaps unitest and other test that do not
# require database connection.

"""
This test_secure module is the testing module for bristoSOFT Contacts v. 0.1
secure module in the control package.
"""
import unittest
from control.secure import Security

class TestSecurity(unittest.TestCase):
    
    def test_minimumcomplex(self):
        
        _digit = Security().mincomplex('Bmw$tieow')
        self.assertFalse(_digit)

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
