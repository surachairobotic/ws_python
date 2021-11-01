#!/usr/bin/env python

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz
import numpy as np


def main(_fname):
    print("Hello !!!")

    plt.close('all')

    #f_name = 'C:/Users/surachai_probook/Downloads/sample/EX4.xlsx'
    f_name = _fname

    n1 = f_name.rfind('/') + 1
    n2 = f_name.rfind('.')
    ffname = f_name[n1:n2]
    ffpath = f_name[:n1]
    print(n1)
    print(n2)
    print(ffname)
    print(ffpath)

    df = pd.read_excel(f_name)
    #with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)
    df = df.fillna(0)
    print(df)
    #print(df.iloc[0])
    t = df['Time MST'].tolist()
    enc = df['Distance'].tolist()
    print(t)
    print(enc)

    list_data = enc
    '''
    for i in range(len(list_data)):
        list_data[i], mx, mn, dt = standardList(list_data[i])
        k = [mx, mn, dt]
        print(k)
    '''
    list_data, mx, mn, dt = standardList(list_data)
    k = [mx, mn, dt]
    print(k)
    list_filter = my_filter(list_data)
    m = slope_list(t, my_filter(list_data), 50)
    list_slope = m
    list_slope_filter = low_filter(list_slope)
    
    '''
    #my_data = [0, 0]
    for i in range(1, len(list_data)):

        #print(list_data[:i])
        #print(len(list_data[:i]))
        k = standardList(list_data[:i])
        #print(k)
        my_data = [0] + k
        list_filter = my_filter(my_data)

        m = slope_list(t, my_filter(my_data), min(50,len(my_data)))
        list_slope = m
        list_slope_filter = low_filter(list_slope)


        fig, axarr = plt.subplots(2, 1, sharex=True)
        axarr[0].plot(t[:i+1], my_data, label=ffname+"_"+str(i), linewidth=0.2)
        nSave = 'C:/Users/surachai_probook/Downloads/sample/all_step/' + ffname+"_"+str(i) + '.png'
        print(nSave)
        plt.savefig(nSave)

    '''

    #print(my_data)
    #list_data = my_data

    name = ffname
    fig, axarr = plt.subplots(2, 1, sharex=True)
    #fig.set_size_inches(13, 5)

    cutoff = 0
    for j in range(len(list_slope_filter)):
        if list_slope_filter[j] > 0.00025:
            cutoff = t[j]
            break

    #axarr[0].axvline(x=cutoff)
    axarr[0].plot(t, list_data, label=name, linewidth=0.2)
    axarr[0].plot(t, list_filter, label=name+'_filter')
    axarr[1].axvline(x=cutoff)
    axarr[1].plot(t, list_slope, label=name+'_slope', linewidth=0.2)
    axarr[1].plot(t, list_slope_filter, label=name+'_slope_filter')
    for j in range(2):
        axarr[j].legend()

    #plt.xticks(rotation=90)
    plt.tight_layout()
    #plt.show()
    nSave = 'C:/Users/surachai_probook/Downloads/sample/' + ffname + '.png'
    #print(nSave)
    plt.savefig(nSave)

    #plt.savefig(ffpath + ffname + '.png')

    #plt.plot()
    #plt.show()
    #exit()

def low_filter(data):
    order = 2
    fs = 1000.0
    cutoff = 3.667  
    y = butter_lowpass_filter(data, cutoff, fs, order)
    return y
def my_filter(data):
    y = moving_average(data, min(20,len(data)))
    return y

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def moving_average(x, w):
    #return np.convolve(x, np.ones(w), 'valid') / w
    return np.convolve(x, np.ones((w,))/w, mode='same')

def slope(x1,y1,x2,y2):
    e = m = -1
    if (x2-x1) != 0:
        m = (y2-y1)/(x2-x1)
        e = 0
    return m, e
def slope_list(x, y, w):
    z = []
    for i in range(len(x)-w):
        if x[i] < 100:
            z.append(0)
        else:
            m,e = slope(x[i],y[i],x[i+w],y[i+w])
            if e != 0:
                k = [i,x[i],y[i],x[i+w],y[i+w]]
                #print(k)
            #m = y[i+w]-y[i]
            if m < 0:
                m = 0
            z.append(m)
    for i in range(w):
        z.append(0)
    return z
def standardList(data):
    mx = max(data)
    mn = min(data)
    dt = mx-mn
    d = []
    for i in range(len(data)):
        if dt == 0:
            d.append(0)
        else:
            d.append((data[i]-mn)/dt)
    return d, mx, mn, dt

if __name__ == '__main__':  
  print('Number of arguments: ' + str(len(sys.argv)))
  print('Argument List: ' + str(sys.argv))
  
  if len(sys.argv) > 1:
    dd = [x for x in os.listdir(sys.argv[1]) if x.find('xlsx') != -1]
    print(dd)
    for ff in dd:    
      _fname = sys.argv[1]+ff
      print("fname: " + _fname)
      main(_fname)
  else:
    print("if len(sys.argv) > 1 is FALSE")

