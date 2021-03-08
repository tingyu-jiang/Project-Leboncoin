#!/usr/bin/env python
# coding: utf-8

# In[42]:


from bs4 import BeautifulSoup
import urllib3
import re
import urllib.request
import numpy as np
import time


# In[43]:


#step_1 data collection 


# In[44]:


web= 'https://www.paruvendu.fr/annonces/velo/strasbourg/'
web


# In[45]:


def get_page(urlpage,element ,html_class):
    ''' From an link and a html class that you select by inspecting manually the page
    Return a list with elements that matched this class'''
    
    # Get page in html
    req = urllib3.PoolManager()
    res = req.request('GET', web)
    soup = BeautifulSoup(res.data, 'html.parser')
    
    # Return elements that matched the html class in a list
    content = soup.find_all(element ,class_= html_class)
    
    return content


# In[46]:


content = get_page(web,'div','debarras-annonce')
content
len(content) 


# In[54]:


apercus=re.findall('<p>\r\n(.*?)\r',str(content))
price=re.findall('(.*?)€',str(content))
link=get_page(web,'a','globann')
title=re.findall(r'title="(.*?)\(',str.lower(str(content))) 
## Décalage des titres
title=re.findall('<h3>(.*,?)\r',str.lower(str(content)))
len(title) 


# In[56]:


len(link)


# In[57]:


len(price)


# In[55]:


#step 2 data processing


# In[58]:


import pandas as pd

table = pd.DataFrame({"title":title,"price":price,"link":link})
table


# In[60]:


table.shape


# In[77]:


table.isnull().sum()


# In[80]:


table.isna().sum()


# In[81]:


table.info


# In[104]:


table_sort = table.sort_values(by = ["price"], ascending = False)
table_sort.head(3)


# In[ ]:


#!!!! il faut tous les pages pour ici
final_table = pd.concat(table_sort)


# In[89]:


#save an excle


# In[90]:


import openpyxl
wb = openpyxl. Workbook()
sheet = wb.active
sheet.title = 'projet'
sheet


# In[91]:


table.to_excel('/Users/tia/Documents/data/projet.xlsx',   
            sheet_name='tb1',     
            float_format='%.2f',  
            na_rep='non',index = False)     


# In[138]:


# send an email 


# In[148]:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

message = MIMEMultipart()
message['From'] = 'miaou.test01@gmail.com'
message['To'] = 'tyjiang95@gmail.com'
message['Subject'] = 'A new bicycle link was found on the website' 


# In[154]:



message = 'print(get_infos())'


# In[155]:


msg.attach(MIMEText(message))
mailserver = smtplib.SMTP('smtp.gmail.com', 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login('miaou.test01@gmail.com', '#testing0')
mailserver.sendmail('tyjiang95@gmail.com', 'tyjiang95@gmail.com', msg.as_string())
mailserver.quit()


# In[92]:


import schedule
import time


# In[93]:


pip install shcedule


# In[ ]:




