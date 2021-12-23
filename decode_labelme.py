'''
Author: Oaktree.AI
Date: 2021-12-22 11:57:52
LastEditors: Oaktree.AI
LastEditTime: 2021-12-22 15:12:57
Description: 
'''

import json
import os
import numpy  as np

def convert(img_size, box):
    # dw = 1. / (img_size[0])
    # dh = 1. / (img_size[1])
    # x = (box[0] + box[2]) / 2.0 - 1
    # y = (box[1] + box[3]) / 2.0 - 1
    # w = box[2] - box[0]
    # h = box[3] - box[1]
    # x = x * dw
    # w = w * dw
    # y = y * dh
    # h = h * dh
    #box = [x1,y1,x2,y2]
    dw = 1. / (img_size[0])
    dh = 1. / (img_size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh

    
    # x1 = box[0]
    # y1 = box[1]
    # x2 = box[2]
    # y2 = box[3]
    return (x, y, w, h)


def decode_json(json_floder_path, json_name):
    txt_name = r'C:/Users/Admin/Desktop/image-Downloader/download_images/vertical/' + json_name[0:-5] + '.txt'
    txt_file = open(txt_name, 'w',encoding='utf-8')

    json_path = os.path.join(json_floder_path, json_name)
    data = json.load(open(json_path, 'r', encoding='utf-8'))

    img_w = data['imageWidth']
    img_h = data['imageHeight']

    for i in data['shapes']:

        if (i['shape_type'] == 'rectangle' and i['label'] == '电瓶车'):
            points = np.array(i["points"])
            xmin = min(points[:, 0]) if min(points[:, 0]) > 0 else 0
            xmax = max(points[:, 0]) if max(points[:, 0]) > 0 else 0
            ymin = min(points[:, 1]) if min(points[:, 1]) > 0 else 0
            ymax = max(points[:, 1]) if max(points[:, 1]) > 0 else 0
            label = i["label"]
            if xmax <= xmin:
                pass
            elif ymax <= ymin:
                pass
            else:
                
                b = (float(xmin), float(xmax), float(ymin), float(ymax))

            bbox = convert((img_w, img_h), b)
            txt_file.write( '0' + " " + " ".join([str(a) for a in bbox]) + '\n')


if __name__ == "__main__":

    json_floder_path = r'C:/Users/Admin/Desktop/image-Downloader/download_images/vertical/'
    json_names = os.listdir(json_floder_path)
    for json_name in json_names:
        file_type = json_name.split('.')[1]
        print(json_name,file_type,"file type")
        if file_type != "json":
            continue
        decode_json(json_floder_path, json_name)

