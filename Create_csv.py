# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 21:27:01 2020

@author: Darshan.Sangani
"""

import pandas as pd
import h5py
import os
import matplotlib.pyplot as plt
import numpy as np
import time

from scipy.stats import pearsonr

args = 'C:/Users/darshan.sangani/Documents/2020_Challenge_IOT_Analytics/competitionfiles'
input_files = [os.path.join(args, file) for file in os.listdir(args)]


for i in range(len(input_files)):
    dataset = list()
    print('first loop: ' + str(i))
    file_name = h5py.File(input_files[175], 'r')
    channel_ids = file_name['DYNAMIC DATA']
    channel_names = list(channel_ids.keys())
    for j in range(len(channel_names)):
        print('second loop: ' + str(j))
        dataset1 = channel_ids[channel_names[j]]['MEASURED']
        print(time.localtime())
        actual_data = pd.DataFrame(dataset1)
        print(time.localtime())
        actual_data.columns = (channel_names[j],)
        dataset.append(actual_data)
    x = input_files[175].split(sep='/')
    y = x[-1].split(sep='\\')
    filename = str(y[-1]) + '.csv'
    dataframe = pd.DataFrame(dataset[0])
    for i in range(len(channel_names)):
        dataframe[channel_names[i]] = dataset[i]
    dataframe.to_csv(filename)
    del dataset
    
