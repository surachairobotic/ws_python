#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

def main():
  print("Hello !!!")
  
  plt.close('all')

  ff = ['C:/Users/surachai_probook/Downloads/TEST770.xlsx',
        'C:/Users/surachai_probook/Downloads/TEST710.xlsx',
        'C:/Users/surachai_probook/Downloads/TEST650.xlsx',
        'C:/Users/surachai_probook/Downloads/TEST6501.xlsx']
  f_name = ff[3]
  df = pd.read_excel(f_name)
  #with pd.option_context('display.max_rows', None, 'display.max_columns', None):
  print(df)
  df.drop(df.columns[[0,1]], axis = 1, inplace = True)
  print(df)
  t = df['Time MST'].tolist()
  dist = df['Distance'].tolist()
  load = df['Load cell'].tolist()
  #print(df.shape[0])

  z = [0]
  for i in range(1,len(dist)):
    area = (dist[i-1]+dist[i]) / 2.0 * (t[i]-t[i-1])
    z.append(area)

  fig, axarr = plt.subplots(1, 1, sharex=True)
  axarr.plot(t, dist, label='Distance')
  axarr.plot(t, z, label='Area')
  #axarr.plot(t, load, label='Load cell')
  axarr.legend()
  #plt.xticks(rotation=90)
  plt.tight_layout()
  #plt.savefig('C:/Users/surachai_probook/Downloads/TEST770.png')
  plt.plot()
  plt.show()
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

