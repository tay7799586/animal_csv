from select import select
from time import time
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import jieba
import collections
import pandas as pd
import seaborn as sns
from matplotlib.font_manager import FontProperties

url = requests.get("https://news.ltn.com.tw/topic/%E6%9F%AC%E5%9F%94%E5%AF%A8") #, headers=headers
# url.encoding = 'UTF-8'
sp = BeautifulSoup(url.text, 'html.parser')
web = sp.find_all("a",class_="tit")
print(web)
for w in web:

        print(w.get("title").strip(),w.get("href"))

# print(sp)
# web = sp.find_all("div" ,class_="whitecon boxTitle")
# w = sp.find_all(["a"])
# print(w)
# for web in w:
#         print(web.select_one("title"))

# print(w)
# for web in w:
#         print(web.find("a")["href"])