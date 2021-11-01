import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import yfinance as yf

total_buy = 0
total_num = 0
back_buy = 0
back_num = 0
me_buy = 0
me_num = 0

def main():
    global total_buy, total_num, me_buy, me_num, back_buy, back_num
    start = "2010-01-01"
    end = '2021-01-01'
    #tcs = yf.download('TCS',start,end)
    #infy = yf.download('INFY',start,end)
    #wipro = yf.download('WIPRO.NS',start,end)
    infy = yf.download('^SET.BK',start,end)
    #print(type(infy))
    #print(infy['Open'])
    #print(type(infy['Open']))
    list_buy = infy.copy()
    list_price = infy.copy()
    list_b_buy = infy.copy()
    list_b_price = infy.copy()
    l_me_buy = infy.copy()
    l_me_price = infy.copy()
    diff = infy.copy()
    z = infy.copy()
    fz = infy.copy()
    
    base = 1000
    x = base
    y = base
    _z = 0
    nn=0
    gg=-1
    ii=[]
    for i in range(len(infy['Open'])):
        back=0
        if i%30==0:
            if i == 0:
                me_buy_f(y, infy['Open'][i])
            elif infy['Open'][i-30]-infy['Open'][i] > 0.5:
                me_buy_f(y, infy['Open'][i])
                y = base
                #print(i)
            else:
                me_buy_f(0, infy['Open'][i])
                y = y + base

            list_buy['Open'][i] = total_buy
            list_price['Open'][i] = (total_num*infy['Open'][i])
            if list_price['Open'][i]/total_buy > 1.07 and back_buy > base*12 and i%30==0:
                _num = back_num*0.01
                back_num = back_num-_num
                back = _num*infy['Open'][i]
                back_buy = back_buy-back
                nn=nn+1
                if gg==-1:
                    gg=i
                ii.append(i)
            else:
                buy(x, infy['Open'][i])

        #print(type(list_buy['Open']))
        #print(type(list_buy['Open'][i]))
        #print(type(total_buy))
        
        _z = _z+back
        z['Open'][i] = _z+back
        fz['Open'][i] = back
        list_buy['Open'][i] = total_buy
        list_price['Open'][i] = (total_num*infy['Open'][i])

        list_b_buy['Open'][i] = back_buy
        list_b_price['Open'][i] = (back_num*infy['Open'][i])

        #l_me_buy['Open'][i] = me_buy
        #l_me_price['Open'][i] = ((me_num*infy['Open'][i])-me_buy)/me_buy
        
        #diff['Open'][i] = l_me_price['Open'][i] - list_price['Open'][i]

    #tcs['Open'].plot(label = 'TCS', figsize = (15,7))
    
    infy['Open'].plot(label = "Infosys", color='blue', linewidth=0.5)
    list_buy['Open'].plot(label = "list_buy", color='green', linewidth=0.5)
    list_b_buy['Open'].plot(label = "list_b_buy", color='blue', linewidth=0.5)
    list_price['Open'].plot(label = "list_price", color='green', linewidth=0.5)
    list_b_price['Open'].plot(label = "list_price", color='blue', linewidth=0.5)
    z['Open'].plot(label = "back", color='red', linewidth=0.5)

    #fz['Open'].plot(label = "back", color='black', linewidth=0.5)
    #diff['Open'].plot(label = "list_price", color='red', linewidth=0.5)
    #l_me_buy['Open'].plot(label = "me_buy")
    #l_me_price['Open'].plot(label = "me_price", color='red')
    #wipro['Open'].plot(label = 'Wipro')
    #plt.plot(infy['Open']['Date'], list_buy)
    #plt.plot(list_price)
    plt.title('Stock Prices.')
    print('nn = ' + str(nn) + '/' + str(len(infy['Open'])))
    print('gg = ' + str(gg))
    print('z = ' + str(z['Open'][-1]) + "/" + str(total_buy))
    print('port = ' + str(list_b_price['Open'][-1]))
    per = z['Open'][-1]/total_buy/len(infy['Open'])*36500
    print("per : " + str(per))
    print(ii)
    plt.show()

def buy(money, price):
    global total_buy, total_num, back_buy, back_num
    total_buy = total_buy + money
    total_num = total_num + (float(money)/price)
    back_buy = back_buy + money
    back_num = back_num + (float(money)/price)

def me_buy_f(money, price):
    global me_buy, me_num
    if money == 0:
        return 0
    me_buy = me_buy + money
    k = (float(money)/price)
    me_num = me_num + k

if __name__ == '__main__':
    main()