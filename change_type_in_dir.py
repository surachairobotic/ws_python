import sys, os

def main():
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', sys.argv)

    path = sys.argv[1]
    print(path)

    if not os.path.exists(path):
        os.mkdir(path)
    print(os.path.exists(path))
    #if path[-1] != '/':
    #    path += '/'
    #print(path)
    
    change2csv(path)
    
def change2csv(rootdir):
    for it in os.scandir(rootdir):
        #print(it)
        if it.is_file():
            fname = os.path.join(rootdir, it.name)
            if fname.find('.csv') == -1:
                os.rename(fname, fname+'.csv')
            #print(fname)
        if it.is_dir():
            fname = os.path.join(rootdir, it.name)
            change2csv(fname)

if __name__ == '__main__':
    main()
