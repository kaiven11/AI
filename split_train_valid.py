'''
Author: Oaktree.AI
Date: 2021-12-22 14:06:18
LastEditors: Oaktree.AI
LastEditTime: 2021-12-22 14:23:44
Description: 
'''
# coding:utf-8

import os
import random
import argparse


current_path = os.getcwd()

parser = argparse.ArgumentParser()
#xml文件的地址，根据自己的数据进行修改 xml一般存放在Annotations下
parser.add_argument('--xml_path', default=current_path+'/labels', type=str, help='input xml label path')
#数据集的划分，地址选择自己数据下的ImageSets/Main
parser.add_argument('--txt_path', default=current_path, type=str, help='output txt label path')
opt = parser.parse_args()

trainval_percent = 0.9 #test=0.2 train=0.8*0.75= 0.6 val=0.8*0.25=0.2  6:2:2
train_percent = 1
xmlfilepath = opt.xml_path
txtsavepath = opt.txt_path
total_xml = os.listdir(xmlfilepath)
if not os.path.exists(txtsavepath):
    os.makedirs(txtsavepath)

num = len(total_xml)
list_index = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list_index, tv)
train = random.sample(trainval, tr)

#file_trainval = open(txtsavepath + '/trainval.txt', 'w')
file_test = open(txtsavepath + '/test.txt', 'w')
file_train = open(txtsavepath + '/train.txt', 'w')
#file_val = open(txtsavepath + '/val.txt', 'w')

for i in list_index:
    name =current_path + '/images/' +total_xml[i][:-4] +".jpeg"+ '\n'
    if i in trainval:
        #file_trainval.write(name)
        if i in train:
            file_train.write(name)
        #else:
            #file_val.write(name)
    else:
        file_test.write(name)

#file_trainval.close()
file_train.close()
#file_val.close()
file_test.close()
