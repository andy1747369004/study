import os
import random

trainval_percent = 1
train_percent = 0.7
imagefilepath = 'G:/Hyperspectral/deeplabv3_preprocess/data_dataset_voc/SegmentationClassPNG/'
txtsavepath = 'G:/Hyperspectral/deeplabv3_preprocess/data_dataset_voc/save/'
total_file = os.listdir(imagefilepath)

num = len(total_file)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open(txtsavepath + '/trainval.txt', 'w')
ftest = open(txtsavepath + '/test.txt', 'w')
ftrain = open(txtsavepath + '/train.txt', 'w')
fval = open(txtsavepath + '/val.txt', 'w')

for i in list:
    name = total_file[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()