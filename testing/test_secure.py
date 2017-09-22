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
try:
    saved = _curpath.index('/media/jacksonkirka/63BF-2E47/workspace/bristosoftcontacts')
except ValueError:
    sys.path.insert(2,'/media/jacksonkirka/63BF-2E47/workspace/bristosoftcontacts')    
    
import unittest
import control.secure

class TestSecurity(unittest.TestCase):
    '''
    TestSecurity is a class test case unit test designed to test whether the
    Security class in the module secure.py provides validated security.
    '''
    def setUp(self):
        '''
        setUp overrides the default setUp to initialize the fixture
        self.security instance.
        '''
        self.sec = control.secure.Security()
        
    def test_minimumcomplex(self):
        '''
        test_minimumcomplex test the Security classes mincomplex()
        method to ensure it requires a complex password.
        '''
        # Tests
        _digit = self.sec.mincomplex('Bmw$tieow')
        _upper = self.sec.mincomplex('bmw$tie1w')
        _lower = self.sec.mincomplex('BMW$TIE1W')
        _special = self.sec.mincomplex('Bmw535is')
        _eight = self.sec.mincomplex('Bmw$535')
        _complex = self.sec.mincomplex('A3$902abM')
        
        # Assertions
        self.assertFalse(_digit)
        self.assertFalse(_upper)
        self.assertFalse(_lower)
        self.assertFalse(_special)
        self.assertFalse(_eight)
        self.assertTrue(_complex)

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
