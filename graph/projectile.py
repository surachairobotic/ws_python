#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

def main():
  print("Hello !!!")
  
  plt.close('all')

  file_errors_location = 'reformat.xlsx'
  df = pd.read_excel(file_errors_location)
  #with pd.option_context('display.max_rows', None, 'display.max_columns', None):
  print (df)
  df['speed'] = df['speed']*-100/255
  
  fig, axarr = plt.subplots(1, 1, sharex=True)
  axarr.scatter(df['speed'], df['real'], marker='.', color='red')
  axarr.scatter(df['speed'], df['calculate'], marker='.', color='blue')

  #plt.gca().invert_xaxis()
  plt.plot()
  plt.show()
    
if __name__ == "__main__":
  main()

