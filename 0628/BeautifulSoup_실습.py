# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 08:59:43 2024

@author: campus4D037
"""

import requests
from bs4 import BeautifulSoup
url = 
res = requests.get() 
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")