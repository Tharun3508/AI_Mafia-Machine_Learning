#!/usr/bin/env python
# coding: utf-8

# In[277]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import Series,DataFrame


# In[278]:


url = 'https://www.flipkart.com/samsung-galaxy-m31s-mirage-blue-128-gb/p/itmad022b9abd4b6?pid=MOBFUYMQUW5EKE7R&lid=LSTMOBFUYMQUW5EKE7RLIUFCT&marketplace=FLIPKART&srno=b_1_1&otracker=browse&fm=neo%2Fmerchandising&iid=a69cb587-9ddc-428c-98ee-dd0b90efd351.MOBFUYMQUW5EKE7R.SEARCH&ppt=sp&ppn=sp&ssid=5cvu8r7vog0000001599490591857'


# In[279]:


result = requests.get(url)


# In[280]:


soup = BeautifulSoup(result.content, 'lxml')
print(soup)


# In[281]:


content = soup.findAll('div')
print(content)


# In[282]:


print(content[1])


# In[283]:


summary = content[1].findAll(class_='_4f8Q22 _2y_FdK')
print(summary)


# In[284]:


content = soup.find(class_='_4f8Q22 _2y_FdK')
print(content)

