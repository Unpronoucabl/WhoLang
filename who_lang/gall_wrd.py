# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 11:34:12 2022

@author: natha
"""
from gall_cir import Gall_cir as cir
from diction import Diction

class G_word(cir):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'diction' in kwargs:
            self.diction = kwargs['diction']
        else:
            self.diction = Diction()
        if self.children == {}:
            syllables = self.diction.str_to_sylDict(self.text)
            for (k,v) in syllables.items():
                self.children[k] = 
        
    