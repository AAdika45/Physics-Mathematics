# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 05:28:56 2022

@author: Aslamic Adika
"""

import numpy as np

class free_fall:
    def __init__(self, massa, percepatan_gravitasi , v_0, waktu):
        self.massa = massa
        self.percepatan_gravitasi = percepatan_gravitasi
        self.waktu = waktu
    
    def kecepatan(self):
        v = self.percepatan_gravitasi*self.waktu
        return v
    


tes1 = free_fall(1,9.8,0,4)
print(tes1.kecepatan())
