from fractions import Fraction

def main1():
  s = input("Enter equation : ")
  if '+' in s:
    indx = s.find('+')
  elif '-' in s:
    indx = s.find('-')
  x = s[:indx]
  y = s[indx+1:]
  op = s[indx]
  print(x)
  print(y)
  print(op)
  x = x.split('/')
  y = y.split('/')
  x = [int(x[0]), int(x[1])]
  y = [int(y[0]), int(y[1])]
  print(x)
  print(y)
  z = [0, x[1] * y[1]]
  if op == '+':
    z[0] = z[1]/x[1]*x[0] + z[1]/y[1]*y[0]
  elif op == '-':
    z[0] = z[1]/x[1]*x[0] - z[1]/y[1]*y[0]
  z = [int(z[0]), int(z[1])]
  print(str(z[0])+'/'+str(z[1]))
  b=True
  while b:
    mm = int(min(z[0], z[1])-1)
    b=False
    for k in range(2, mm):
      if z[0]%k==0 and z[1]%k==0:
        z[0]=int(z[0]/k)
        z[1]=int(z[1]/k)
        b=True
        break
  print(str(int(z[0]))+'/'+str(int(z[1])))

def main2():
  s = input("Enter equation : ")
  if '+' in s:
    indx = s.find('+')
  elif '-' in s:
    indx = s.find('-')
  x = Fraction(s[:indx])
  y = Fraction(s[indx+1:])
  op = s[indx]
  print(x)
  print(y)
  print(op)
  if op == '+':
    print(x+y)
  elif op == '-':
    print(x-y)

if __name__ == '__main__':
  main2()