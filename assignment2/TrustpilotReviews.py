#!/usr/bin/env python
# coding: utf-8

# In[36]:


import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import requests, json
import requests
from lxml.html import fromstring

my_url = 'https://www.trustpilot.com/review/www.bwear.com'

# opening url and grabbing the web page
uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()


# html parsing
page_soup = soup(page_html, 'html.parser')

filename = "trustpilotReviews.csv"
f = open(filename, 'w',encoding="utf-8")

headers = "Name, Headline, Reviews\n"

f.write(headers)

#containers = page_soup.findAll('script', {'type':'application/ld+json'})
parsed_data = json.loads(page_soup.find('script',type='application/ld+json').string)
containers = json.dumps(parsed_data,indent=4)
containers = json.loads(containers)
containers=a[0]['review']

for container in containers:
    name=container['author']['name']
    headline=container['headline']
    reviewBody=container['reviewBody']
    print('Name :',name)
    print('Headline',headline)
    print('Reviews',reviewBody)
    
    f.write(name + ',' + headline + ',' + reviewBody + '\n')

f.close()

#print(containers)



# In[ ]:





# In[ ]:




