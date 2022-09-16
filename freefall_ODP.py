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
       return  print(f"kecepatan benda jatuh bebas pada saat detik ke-{self.waktu} adalah {v} m/s.")
    
    def tinggi(self,tinggi_awal):
        h = tinggi_awal - 0.5*self.percepatan_gravitasi*self.waktu**2
        if h<0:
            t = np.sqrt(2*tinggi_awal/self.percepatan_gravitasi)
            print(f'benda sampai ke tanah sebelum {self.waktu} detik, yaitu pada t={t}s')
        else:
            print(f"ketinggian benda jatuh bebas pada saat detik ke-{self.waktu} adalah {h} m.")
        return


tes1 = free_fall(1,9.8,0,4)
print(tes1.kecepatan())
