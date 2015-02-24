# -*- coding: utf-8 -*-
import requests, time, re, os, logging, traceback
from bs4 import BeautifulSoup
from random import randint
from requests.exceptions import ConnectionError
from datetime import datetime

file = 'item_detail/0218/其他/items_page_1_514_interval1_mod.csv'
f = open(file, 'r')
text = f.read()
all = open('item_detail/0218/itemDetails_all.csv', 'a')
all.write(text)
all.close()
f.close()