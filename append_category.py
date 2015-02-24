# -*- coding: utf-8 -*-
import requests, time, re, os, logging, traceback
from bs4 import BeautifulSoup
from random import randint
from requests.exceptions import ConnectionError
from datetime import datetime

file = 'item_detail/0218/布、紙面膜/items_page_1_505_interval1.csv'
f = open(file, 'r')
mod_file = open('item_detail/0218/布、紙面膜/items_page_1_505_interval1_mod.csv', 'w')
for line in f.readlines():
    mod_line = line.replace('\n', ',面膜,布、紙面膜\n')
    mod_file.write(mod_line)
mod_file.close()
f.close()