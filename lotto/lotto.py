#!/usr/bin/env python

class Data:
  def __init__(self):
    self.day = -1
    self.month = -1
    self.year = -1
    self.first = -1
    self.f2 = -1
    self.f3 = -1
    self.l2 = -1
    self.l3 = -1
    

def main():
  print("Hello !!!")
  f = open("data.txt", "r", encoding="utf8")

  state = 0
  all_data = []
  d = Data()
  for x in f.readlines():
      if state is 0:
        d.day = x[:-1]
      elif state is 1:
        d.month = x[:-1]
      elif state is 2:
        d.year = x[:-1]
      elif state is 3:
        d.first = x[:-1]
      elif state is 4:
        d.f2 = x[:-1]
      elif state is 5:
        d.f3 = x[:-1]
      elif state is 6:
        d.l2 = x[:-1]
      elif state is 7:
        d.l3 = x[:-1]
        all_data.append(d)
        d = Data()
      state = (state+1)%8

  f2={}
  f2a={}
  f2b={}
  for x in all_data:
    #print(x.__dict__)
    if not f2.get(x.f2):
      f2[x.f2] = 1
    else:
      f2[x.f2] = f2[x.f2] + 1
    a=x.f2[0]
    b=x.f2[1]
    if not f2a.get(a):
      f2a[a] = 1
    else:
      f2a[a] = f2a[a] + 1
    if not f2b.get(b):
      f2b[b] = 1
    else:
      f2b[b] = f2b[b] + 1

  #print(sorted(f2.values()))
  #print(sorted(f2, key=f2.get))
  s = sum(f2b.values())
  for k, v in f2b.items():
    pct = v * 100.0 / s
    print(k, pct)
  #print(f2a.items())
  #print(sorted(f2.items(), key=lambda x:x[1]))
  #print(sorted(f2a.items(), key=lambda x:x[1]))
  #print(sorted(f2b.items(), key=lambda x:x[1]))
      
if __name__ == "__main__":
  main()

