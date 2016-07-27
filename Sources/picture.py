#encoding:utf-8

#============map并行生成缩略图程序

import os
import PIL

from multiprocessing import Pool
from PIL import Image

SIZE = (75,75)
SAVE_DIRECTORY = 'thumbs'

def get_image_paths(folder):
    return (os.path.join(folder, f)
            for f in os.listdir(folder)
            if 'jpeg' in f)

def create_thumbnail(filename):
    im = Image.open(filename)
    im.thumbnail(SIZE, Image.ANTIALIAS)
    base, fname = os.path.split(filename)
    save_path = os.path.join(base, SAVE_DIRECTORY, fname)
    im.save(save_path)

if __name__ == '__main__':
    folder = os.path.abspath(
        '作品')


    folder='D:\PythonProjects\数据分析\pydata-book\Sources\Picture\作品'
    folder = unicode(folder,'utf-8')
    os.mkdir(os.path.join(folder, SAVE_DIRECTORY))

    images = get_image_paths(folder)

    pool = Pool()
    pool.map(create_thumbnail, images)
    pool.close()
    pool.join()