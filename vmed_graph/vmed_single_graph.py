import pandas as pd
from xlsx import XLSX
import matplotlib.pyplot as plt


def getFiles(mypath):
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [mypath+f for f in listdir(mypath) if isfile(join(mypath, f)) and f.find('.xlsx') != -1]
    return onlyfiles

if __name__ == "__main__":
    
    PATH = 'C:/heart_data/'
    files = getFiles(PATH)
    print(files)
    #exit()

    X = []
    Y = []
    
    for file in files:
        xlsx = XLSX(file)
        data = xlsx.read('sheet1')
    
        x = data['A'].tolist()
        #x = x[1000:]
        mmax = float(x[-1])/10000.0
        y = data['B'].tolist()
        #y = y[1000:]
    
        for i in range(len(x)):
            x[i] = mmax - (float(x[i])/10000.0)

        for i in range(len(y)):
            y[i] = float(y[i])

        X.append(x)
        Y.append(y)

    num = len(X)
    #num = 3
    ax_list = []
    for i in range(num):
        ax_list.append(plt.subplot(num, 1, i+1))
        ax_list[i].axes.get_xaxis().set_visible(False)
        ax_list[i].plot(X[i], Y[i])

    ax_list[-1].axes.get_xaxis().set_visible(True)

    #ax_list[0].get_shared_x_axes().join(ax_list[0], *ax_list)
    ax_list[0].get_shared_y_axes().join(ax_list[0], *ax_list)

    plt.suptitle('Patient 4-6', fontsize=14, fontweight='bold')
    plt.show()