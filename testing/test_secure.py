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
# Note: Testing can be done using perhaps unittest and other test that do not
# require database connection.

"""
This test_secure module is the testing module for bristoSOFT Contacts v. 0.1
secure module in the control package.
"""

# sys.path must be updated for the project directory when running tests.
# Limit usage of relative imports and use absolute dotted imports.
import sys
_curpath = sys.path 
if _curpath[1] != '/media/jacksonkirka/MSDOS/workspace/bristosoftcontacts':
    sys.path.append('/media/jacksonkirka/MSDOS/workspace/bristosoftcontacts')    
    
import unittest
import control.secure

class TestSecurity(unittest.TestCase):
    
    def test_minimumcomplex(self):
        '''
        test_minimumcomplex test the Security classes mincomplex()
        method to ensure it requires a complex password.
        '''
        _digit = control.secure.Security().mincomplex('Bmw$tieow')
        self.assertFalse(_digit)

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
