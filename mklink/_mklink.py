# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 19-10-2012

@author: mkurzawa
'''

class mklink():
    
    def __init__(self, src_path, dst_path):
        self._sp = src_path
        self._dp = dst_path
    
    def mklink(self):
        '''
        1. check src dir
        2. check dst dir
            2. check if exist
                y. if empty
                    y. del path
                    n. exit
        3. create relative dst dir path
        
        //subprocess.Popen(r'path to program', cwd=r'path to working directory')
        5. call mklink via subprocess
        '''
        return False
