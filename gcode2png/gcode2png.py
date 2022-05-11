#!/usr/bin/python3

import sys
import re
import numpy
from PIL import Image

class Information:
    def __init__(self, _layer, _xy):
        self.layer = _layer # int
        self.xy = _xy # [ [int, int], ... ]

    def toPng(self):
        pic = numpy.zeros((1300, 1300, 3), dtype=numpy.uint8)
        pic[::] = [255,255,255]
        for _xy in self.xy:
            pic[int(_xy[0]*10.0)][int(_xy[1]*10.0)] = [0,0,0]

        image = Image.fromarray(pic)
        image.save("layer_"+f"{self.layer:03d}"+".bmp", format="bmp")

def main():
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', sys.argv)

    f = open(sys.argv[1], "r", encoding="utf8")

    f_path = sys.argv[1][:sys.argv[1].rfind('/')+1]
    print(f_path)
    
    all_data = []
    for x in f.readlines():
        all_data.append(x)
    
    f_save = open(f_path+'ear.gcode', "w", encoding="utf8")
    cnt=0
    b_start=False
    xy = []
    xy_min = [9999, 9999]
    xy_max = [-999, -999]
    informations = []
    layer=-1
    for data in all_data:
        cnt+=1
        f_save.writelines(data)
        if data.find('X') != -1 and data.find('Y') != -1:
            tmp = split([" "], data)
            x_indx = y_indx = -1
            for i in range(len(tmp)):
                if tmp[i].find('X') != -1:
                    x_indx = i
                if tmp[i].find('Y') != -1:
                    y_indx = i
            x = re.search(r'\d+\.\d+',tmp[x_indx])
            y = re.search(r'\d+\.\d+',tmp[y_indx])
            if x != None and y != None:
                x = float( x.group() )
                y = float( y.group() )
                xy_min = [min(xy_min[0], x), min(xy_min[1], y)]
                xy_max = [max(xy_max[0], x), max(xy_max[1], y)]
                xy.append([x, y])
                #print(str(data) +" : " + str(x) + ", " + str(y))
        if b_start and data.find('LAYER:') != -1:
            info = Information(layer, xy)
            info.toPng()
            informations.append(info)
            layer = int(data[data.find('LAYER:')+6:])
            print(layer)
            xy = []
        if data.find('LAYER:0') != -1:
            print(str(cnt) + ' : ' + data)
            layer=0
            b_start=True
            #break
    info = Information(layer, xy)
    info.toPng()
    informations.append(info)

    f.close()
    f_save.close()

    #print(xy)
    #print(xy_min)
    #print(xy_max)

def split(delimiters, string, maxsplit=0):
    import re
    regexPattern = '|'.join(map(re.escape, delimiters))
    return re.split(regexPattern, string, maxsplit)

if __name__ == '__main__':
    main()
