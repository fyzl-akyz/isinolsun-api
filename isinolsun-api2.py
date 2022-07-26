#!/usr/bin/env python
# coding: utf-8

# In[11]:


import requests
import pandas as pd
from bs4 import BeautifulSoup
city = str(input("Which city you want ? "))
position = str(input("Which position you want ? "))
c = str(input("Which time you want ? (all = press enter , fulltime = 1 , parttime = 2)"))
a=1
c=0
while(True):
    adress = "https://isinolsun.com/is-ilanlari?kw=%s&lc=%s&pn=%s" % (position,city,c)
    r = requests.get(adress)
    soup = BeautifulSoup(r.content,"lxml")
    details = soup.find_all("div",attrs={"data-test":"job-list-item"})
    if(details):
        for i in details:
            title = i.find("h3", attrs={"class":"card-title"}).text
            coorp = i.find("p", attrs={"class":"card-text"}).text
            location = i.find("em", attrs={"class":"card-city"}).text
            date = i.find("em",attrs={"class":"duration"}).text
            print(a,"  ","Job:",title ,", Company name :", coorp, "Date:",date ,", Location: ",location)
            a = a+1
        c = c+1
    else:
        break


# In[ ]:





# In[ ]:





# In[ ]:




