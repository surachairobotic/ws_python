#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

def main():
  print("Hello !!!")
  
  plt.close('all')

  f_name = '/home/probook/Downloads/P1951578_15 samples_8072564_(Averag 5 records).xls'
  df = pd.read_excel(f_name)
  #with pd.option_context('display.max_rows', None, 'display.max_columns', None):
  print(df)
  name = df.iloc[2:,0].tolist()
  print(name)
  x = [x for x in range(7)]
  print(df.columns[x])
  df.drop(df.columns[x], axis = 1, inplace = True)
  df.drop([0], inplace = True)
  df = df.fillna(0)
  #print(df)
  #print(df.iloc[0])
  t = df.iloc[0]
  y = []
  #print(df.shape[0])
  for i in range(1, df.shape[0]):
    y.append(df.iloc[i])
    #print(len(y[i-1]))

  for i in range(len(t)):
    if t[i] > 90:
      break_indx = i
      for j in range(len(y)):
        y[j] = y[j][:i]
      t = t[:i]
      break
  #df['speed'] = df['speed']*-100/255
  z=[]
  avg=[]
  for i in range(len(y)):
    _sum=0
    tmp=[0]
    for j in range(len(t)-1):
      dt=t[j+1]-t[j]
      area=(y[i][j]+y[i][j+1])/2.0*dt
      _sum=_sum+area
      tmp.append(area)
    avg.append(_sum)
    z.append(tmp)

  for i in range(len(name)):
     name[i]=name[i][3:-10]
  print("name : ")
  print(name)


  fig, axarr = plt.subplots(1, 1, sharex=True)
  axarr.plot(name, avg, label='Area value all files')
  axarr.legend()
  plt.xticks(rotation=90)
  plt.tight_layout()
  plt.savefig("/home/probook/Downloads/savefig/all_area.png")
  #plt.plot()
  #plt.show()
  exit()

  pattern=2
  for i in range(len(y)):
    fig, axarr = plt.subplots(1, 1, sharex=True)
    _a = "{:.2f}".format(round(avg[i], 2))
    if pattern is 1:
      axarr.plot(t, y[i], label=name[i]+" : "+_a)
      axarr.legend()
      plt.savefig("/home/probook/Downloads/savefig/clean/"+name[i]+".png")
    elif pattern is 2:
      axarr.plot(t, y[i], label=name[i])
      axarr.plot(t, z[i], label='Average area : '+_a)
      axarr.legend()
      plt.savefig("/home/probook/Downloads/savefig/with_area/"+name[i]+".png")
    #print("name : " + name[i])
    #break


  #axarr.scatter(df['speed'], df['calculate'], marker='.', color='blue')

  #plt.gca().invert_xaxis()
  #plt.plot()
  #plt.show()
    
if __name__ == "__main__":
  main()

