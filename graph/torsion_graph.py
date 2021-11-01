#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz
import numpy as np


def main():
  print("Hello !!!")
  
  plt.close('all')

  f_name = 'C:/Users/surachai_probook/Downloads/Torsion_spring_and_Encoder_sensor.xlsx'

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
  #print(df)
  df = df.fillna(0)
  #print(df)
  #print(df.iloc[0])
  t = df['Time MST'].tolist()
  enc1 = df['Encoder1'].tolist()
  enc2 = df['Encoder2'].tolist()
  enc3 = df['Encoder3'].tolist()
  dist1 = df['Distance1'].tolist()
  dist2 = df['Distance2'].tolist()
  dist3 = df['Distance3'].tolist()
  #print(t)
  #print(enc1)
  #print(enc2)
  #print(enc3)
  #print(dist1)
  #print(dist2)
  #print(dist3)

  list_data = [enc1, enc2, enc3, dist1, dist2, dist3]
  for i in range(len(list_data)):
    list_data[i], mx, mn, dt = standardList(list_data[i])
    k = [mx, mn, dt]
    print(k)
  list_filter = []
  list_slope = []
  for x in list_data:
    #f = my_filter(x)
    list_filter.append(my_filter(x))
    m = slope_list(t, my_filter(x), 50)
    list_slope.append(m)
  list_slope_filter = []
  for x in list_slope:
    list_slope_filter.append(low_filter(x))
  
  name = ['encoder1', 'encoder2', 'encoder3', 'distance1', 'distance2', 'distance3']
  for i in range(len(name)):
    fig, axarr = plt.subplots(2, 1, sharex=True)
    #fig.set_size_inches(13, 5)
    cutoff = 0
    for j in range(len(list_slope_filter[i])):
      if list_slope_filter[i][j] > 0.00025:
        cutoff = t[j]
        break
    axarr[0].axvline(x=cutoff)
    axarr[0].plot(t, list_data[i], label=name[i], linewidth=0.2)
    axarr[0].plot(t, list_filter[i], label=name[i]+'_filter')
    axarr[1].axvline(x=cutoff)
    axarr[1].plot(t, list_slope[i], label=name[i]+'_slope', linewidth=0.2)
    axarr[1].plot(t, list_slope_filter[i], label=name[i]+'_slope_filter')
    for j in range(2):
      axarr[j].legend()
    #plt.xticks(rotation=90)
    #plt.tight_layout()
    #plt.show()
    nSave = 'C:/Users/surachai_probook/Downloads/torsion/' + name[i] + '.png'
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
  y = moving_average(data, 20)
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
    d.append((data[i]-mn)/dt)
  return d, mx, mn, dt

if __name__ == "__main__":
  main()

