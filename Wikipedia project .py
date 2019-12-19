#!/usr/bin/env python
# coding: utf-8

# In[42]:


# import libraries
import requests
website_url = requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M').text


# In[43]:


# import beautifulsoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(website_url,'lxml')
print(soup.prettify())


# In[53]:


#Read Data
df = pd.read_html(website_url, header = 0)[0]
df.head()


# In[64]:


# Only process the cells that have an assigned borough. Ignore cells with a borough that is Not assigned.
df=df[df.Borough != 'Not assigned']
# More than one neighborhood can exist in one postal code area. For example, in the table on the Wikipedia page, you will notice that M5A is listed twice and has two
#neighborhoods: Harbourfront and Regent Park. These two rows will be combined into one row with the neighborhoods separated with a comma as shown in row 11 in the above table.
df = df.groupby(['Postcode', 'Borough'])['Neighbourhood'].apply(list).apply(lambda x:', '.join(x)).to_frame().reset_index()
for i, row in df.iterrows():
    if row['Neighbourhood'] == 'Not assigned':
        row['Neighbourhood'] = row['Borough']
df


# In[55]:


df.shape


# In[ ]:





# In[ ]:




