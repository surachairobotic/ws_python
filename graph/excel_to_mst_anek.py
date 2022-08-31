import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def csv_to_list(fpath, fname):
    df = pd.read_csv(fpath + fname)
    #print(df)
    #df.plot()
    #plt.show()
    short = df['Filter Short'].values.tolist()
    long = df['Filter Long'].values.tolist()
    for i in range(len(short)):
        short[i] = float(short[i])
    for i in range(len(long)):
        long[i] = float(long[i])
    
    ns = len(short)
    nl = len(long)
    if ns == 0 or nl == 0 or ns != nl:
        return 0
    
    res = []
    for i in range(len(short)):
        res.append(short[i]-long[i])
    
    fig, axs = plt.subplots(2)
    fig.suptitle(fname)
    axs[0].set_xlabel('Time (s)')
    axs[0].set_ylabel('Force (gF)')
    axs[0].plot(df['RAW'].values.tolist())
    axs[0].plot(short)
    axs[0].plot(long)
    
    axs[1].plot(res)
    axs[1].set_xlabel('Time (s)')
    axs[1].set_ylabel('R.O.C')
    
    line = 0
    p = para(len(short))
    for i in range(300, len(p)):
        if res[i] > p[i]:
            line = i
            break
    #print(p)
    
    df['diff'] = res
    df['equation'] = p
    if fname.find('new') == -1:
        df.to_csv(fpath + "new_" + fname)

    #print(df)
    
    axs[1].plot(p)
    
    axs[1].axvline(x = line, color = 'r', linestyle='dashed')
    axs[1].text(line+10, p[line]+0.1, 'mst = ' + str(line), fontsize=10)
    
    #figure = plt.gcf() # get current figure
    #figure.set_size_inches(8, 7)

    #plt.show()
    plt.savefig(fpath + fname[:-4] + ".png", dpi = 100)
    
    return res

def eq_palabora(i):
    threshold =(1.04167*1e-6 * (i ** 2) ) - (0.002290 * i) + 2.25
    return threshold
    #return  1.04167*1e-6 * ((i ** 2) - (0.002290 * i)) + 2.25

def para(num):
    print(num)
    list_test = np.arange(num)
    plot_list = []
    #print(list_test)

    for j in list_test:
        plot_list.append(eq_palabora(j))
    
    return plot_list

def get_file_lists(mypath):
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and ".csv" in f]
    return onlyfiles

def main():
    fLists = get_file_lists("C:\\MST151821_03_65\\")
    dataList = []
    for i in range(len(fLists)):
        print(fLists[i])
        f = fLists[i]
        data = csv_to_list("C:\\MST151821_03_65\\", f)
        #dataList.append(data)
        #break
    #exit()
    '''
    for d in dataList:
        plt.plot(d)
    plt.show()
    '''

if __name__ == "__main__":
    print(plt.get_backend())
    #exit()
    main()