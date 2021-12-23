'''
Author: Oaktree.AI
Date: 2021-12-22 10:54:21
LastEditors: Oaktree.AI
LastEditTime: 2021-12-22 11:38:12
Description: 
'''


import os
import shutil

from cv2 import CAP_PROP_OPENNI_MAX_TIME_DURATION

img_path = r'C:/Users/Admin/Desktop/image-Downloader/download_images/电动车/'

img_list = os.listdir(img_path)

for name in img_list:
    filename = name.split('.')[0]
    json_file_name =  filename+'.json'
    print(json_file_name,"json file name")
    img_file_name = filename+".jpeg"
    img_file_name_2 = filename+".png"
    print(img_file_name,"image file name ")
    
    
    json_file_path = os.path.join(img_path, json_file_name)
    img_file_path  = os.path.join(img_path, img_file_name)
    png_file_path = os.path.join(img_path,img_file_name_2)
    
    if os.path.exists(png_file_path):
        os.remove(png_file_path)
    
    
    if  os.path.exists(json_file_path):
        
        if not os.path.exists(img_file_path):
        
            try:
                os.remove(json_file_path)
            except Exception as e:
                print(e)
           
           
    if  os.path.exists(img_file_path):
        
        if not os.path.exists(json_file_path):
        
            try:
                os.remove(img_file_path)
            except Exception as e:
                print(e)       
    
        

