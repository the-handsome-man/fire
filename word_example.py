# -*- coding: utf-8 -*-
#! use\env\bin\python 3

import wordcloud
import jieba, os
import imageio

path = r'D:\临时文件\马上删除的\词云'
os.chdir(path)
mask_1 = imageio.imread(r'中国地图.jpg')
words = open(r'D:\学术文件\练习\人机工程学\work_3\file_1.txt','r', encoding='utf-8').read()
ls = jieba.lcut(words)
text = ' '.join(ls)
w = wordcloud.WordCloud(mask=mask_1, font_path="msyh.ttc")
w.generate(text)
w.to_file('job_2.png')
