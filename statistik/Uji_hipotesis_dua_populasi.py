# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 23:37:47 2022

@author: Aslamic Adika
"""
import numpy as np
import pandas as pd
import seaborn  as sns
import matplotlib.pyplot as plt


class deskriptif_stat:
        
    def __init__(self):
        'Ini adalah metode cepat agar dalam analisis data tidak perlu \\'
        'repot-repot menulis ulang code statistik yang umum muncul'
        'code ini juga akan dilengkapi data visualisasi yang umum muncul'
        
    def avg(self,data):
        self.data = data
        total_i = 0
        if len(data) == 0:
            print('tidak ada data')
        else:
            for i in data:
                total_i += i
                avg = total_i/len(data)
                avg = float("{:.3f}".format(avg))
        return avg
    
    def std_sampel(self,data):
        sigma = 0
        self.data = data
        if len(data) == 0:
            print('tidak ada data')
            pass
        else:
            total_i = 0
        if len(data) == 0:
            pass
        else:
            for i in data:
                total_i += i
                avg = total_i/len(data)
                avg = float("{:.3f}".format(avg))
        for i in data:
            sigma += (i - avg)**2
            std = np.sqrt(sigma/len(data)-1)
        std = float("{:.3f}".format(std))
        return std
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
