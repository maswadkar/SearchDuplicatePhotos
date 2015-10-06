from PIL import Image
import os
import pandas as pd


def get_jpgs(dirpath):
    count = 0
    photo_list=pd.DataFrame(columns=['filename','exif_information'])
    for root,dirs,files in os.walk(dirpath):
        print('found total %d photos ' %count)
        for names in files:
            fullpath = os.path.join(root,names)
            fname,extension = os.path.splitext(fullpath)
            temp={}
            if extension.upper() == '.JPG':
                count = count+1
                try:
                    temp.update({'filename':fullpath,'exif_information':Image.open(fullpath)._getexif()})
                    photo_list.loc[photo_list.__len__()+1] = temp
                except Exception as e:
                    print(e)
                    print(fullpath)


    return photo_list

#Main program starts here. 
complete_list = get_jpgs('/Users/mbp/Pictures')
print('there are total %d photos' %len(complete_list))

#Compare the exif information of each photo with the other photos in the list. 
for firstloop in range(1,len(complete_list)):
    left = complete_list.get_value(firstloop,'exif_information')
    # print('processing %s' %left)
    if left:
        for secondloop in range(firstloop+1,len(complete_list)):
            right= complete_list.get_value(secondloop,'exif_information')
            if right:
                if left == right:
                    print(complete_list.get_value(firstloop,'filename') + ' is duplicate of  '+ complete_list.get_value(secondloop,'filename'))

print('program completed')
