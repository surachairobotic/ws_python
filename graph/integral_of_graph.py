#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

def main():
  print("Hello !!!")
  
  plt.close('all')

<<<<<<< HEAD
  f_name = 'C:/Users/surachai_probook/Downloads/P1951578_12 samples_8092564_(Averag 5 records).xls'
  f_name = 'C:/Users/surachai_probook/Downloads/Particle size of HA latex from east and south.xlsx'

  n1 = f_name.rfind('/') + 1
  n2 = f_name.rfind('.')
  ffname = f_name[n1:n2]
  ffpath = f_name[:n1]

=======
  f_name = '/home/probook/Downloads/P1951578_15 samples_8072564_(Averag 5 records).xls'
>>>>>>> 0a0bed63219dc0d33cc53d8c1a14acf328f58355
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
  print(df)
  #print(df.iloc[0])
  t = df.iloc[0]
  y = []
  #print(df.shape[0])
  for i in range(1, df.shape[0]):
    y.append(df.iloc[i])
    #print(len(y[i-1]))

  for i in range(len(t)):
<<<<<<< HEAD
    if t[i] > 16:
=======
    if t[i] > 20:
>>>>>>> 0a0bed63219dc0d33cc53d8c1a14acf328f58355
      break_indx = i
      for j in range(len(y)):
        y[j] = y[j][:i]
      t = t[:i]
      break
  #df['speed'] = df['speed']*-100/255
  z=[]
  avg=[]
<<<<<<< HEAD
  m=[]
  vx=[]
  w1=[]
  w2=[]
  for i in range(len(y)):
    _sum=0
    tmp=[0]
    _m=[]
    b_line=True
    for j in range(len(t)-1):
      if t[j] > 1 and t[j] < 4:
        _y = y[i][j+1]-y[i][j]
        if _y > 0:
          _y = 6
          if b_line and _m[-1] == 0:
            b_line = False
            vx.append(t[j])
            w1.append(_sum)
        elif _y < 0:
          _y = 0
        else:
          _y = 3
        _m.append(_y)
      else:
        _m.append(0)

      dt=t[j+1]-t[j]
      area=(y[i][j]+y[i][j+1])/2.0*dt
      _sum=_sum+area
      tmp.append(area)

    avg.append(_sum)
    z.append(tmp)
    _m.append(0)
    m.append(_m)
    #w2.append(_sum-w1[-1])
=======
  m = []
  w1 = []
  w2 = []
  for i in range(len(y)):
    _sum=0
    tmp=[0]
    _m=[3]
    _w1=0
    _w2=0
    for j in range(1,len(t)):
      if t[j] > 1 and t[j] < 4:
        if y[i][j-1]-y[i][j] > 0:
          _m.append(0)
        elif y[i][j-1]-y[i][j] < 0:
          _m.append(6)
        elif y[i][j-1]-y[i][j] == 0:
          _m.append(3)
      else:
        _m.append(3)
      if _m[j]-_m[j-1] == 6:
         _w1 = _sum
      dt=t[j]-t[j-1]
      area=(y[i][j]+y[i][j-1])/2.0*dt
      _sum=_sum+area
      tmp.append(area)
    _w2 = _sum-_w1
    w1.append(_w1)
    w2.append(_w2)
    avg.append(_sum)
    z.append(tmp)
    m.append(_m)
>>>>>>> 0a0bed63219dc0d33cc53d8c1a14acf328f58355

  #for i in range(len(name)):
  #   name[i]=name[i][3:-10]
  print("name : ")
  print(name)


  fig, axarr = plt.subplots(1, 1, sharex=True)
  fig.set_size_inches(13, 5)
  axarr.plot(name, avg, label='Area value all files')
  axarr.legend()
  plt.xticks(rotation=90)
  plt.tight_layout()
<<<<<<< HEAD
  plt.savefig(ffpath + ffname + '.png')
=======
  plt.savefig('/home/probook/Downloads/P1951578_15 samples_8072564_(Averag 5 records).png')
>>>>>>> 0a0bed63219dc0d33cc53d8c1a14acf328f58355
  #plt.plot()
  #plt.show()
  #exit()

  pattern=2
  fig2, axarr2 = plt.subplots(1, 1, sharex=True)
  fig2.set_size_inches(13, 5)
  for i in range(len(y)):
    fig, axarr = plt.subplots(1, 1, sharex=True)
    fig.set_size_inches(13, 5)
    _a = "{:.2f}".format(round(avg[i], 2))
<<<<<<< HEAD
    #_w1 = "{:.2f}".format(round(w1[i], 2))
    #_w2 = "{:.2f}".format(round(w2[i], 2))
=======
    _w1 = "{:.2f}".format(round(w1[i], 2))
    _w2 = "{:.2f}".format(round(w2[i], 2))
>>>>>>> 0a0bed63219dc0d33cc53d8c1a14acf328f58355
    if pattern is 1:
      axarr.plot(t, y[i], label=name[i]+": "+_a+"\nw1: "+_w1+"\nw2: "+_w2)
      axarr.plot(t, m[i])
      axarr.legend()
      fig.savefig("/home/probook/Downloads/savefig/clean/"+name[i]+".png")
    elif pattern is 2:
      #axarr.plot(t, m[i], label='slope')
      #axarr.axvline(x=vx[i], color='k', linestyle='--')
      axarr.plot(t, y[i], label=name[i])
<<<<<<< HEAD
      #axarr.plot(t, z[i], label='Average area : '+_a+'\nw1 : '+_w1+'\nw2 : '+_w2)
      axarr.plot(t, z[i], label='Average area : '+_a)
      axarr.legend()
      plt.savefig(ffpath+"savefig/lot3/"+name[i]+".png")
=======
      axarr.plot(t, z[i], label='Average area : '+_a+"\nw1: "+_w1+"\nw2: "+_w2)
      axarr.plot(t, m[i])
      axarr.legend()
      fig.savefig("/home/probook/Downloads/savefig/with_area/"+name[i]+".png")
      axarr2.plot(t, y[i], label=name[i])
      axarr2.plot(t, m[i])
>>>>>>> 0a0bed63219dc0d33cc53d8c1a14acf328f58355
    #print("name : " + name[i])
    #break
  fig2.tight_layout()
  fig2.savefig("/home/probook/Downloads/savefig/xxx.png")


  #axarr.scatter(df['speed'], df['calculate'], marker='.', color='blue')

  #plt.gca().invert_xaxis()
  #plt.plot()
  #plt.show()
    
if __name__ == "__main__":
  main()

