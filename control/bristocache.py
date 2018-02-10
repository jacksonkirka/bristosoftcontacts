'''
bristoSOFT cache module that implements a comprehensive cache system based on time
other factors.
'''

import datetime

class bristoCache(dict):
    
    def __init__(self):
        '''
        Constructor for class.
        '''
        self.cache = {}
    
