#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import re
import csv
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv('DS full scrape.csv')


# In[4]:


df.shape


# In[5]:


df.info()


# In[6]:


df.head()


# In[ ]:





# In[7]:


df['Title'].value_counts()[:10]


# In[8]:


title = df['Title'].value_counts()[0:10]
title = dict(title)
print(title)


# In[9]:


titles = list(title.values())
labels = list(title.keys())

labels.reverse()
titles.reverse()
plt.barh(labels, titles, animated=True)
plt.title("Top 10 Job Titles for 'Data Scientist' in Job Listings")
plt.xlabel("Frequency")
plt.show()


# In[12]:


titles = df['Title'].values.tolist() #convert dataframe to list
string=Counter(titles)
wordcloud = WordCloud(width = 1600, height = 800,max_words=50,background_color='black').generate_from_frequencies(string)
plt.figure(figsize=(40,30))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()


# In[166]:


df['Company'].value_counts()


# In[172]:


company = df['Company'].value_counts()[0:10]
company = dict(company)

companies = list(company.values())
labels = list(company.keys())

labels.reverse()
companies.reverse()
plt.barh(labels, companies, color = 'green',animated=True)
plt.title("Top 10 Companies Posting 'Data Scientist' Job Listings ")
plt.xlabel("Frequency")
plt.show()


# In[23]:


df2 = pd.read_csv('locations.csv')


# In[168]:


df2.head()


# In[107]:


df2["city"]=df2.Location.str.split(',',expand=True).iloc[:,0] #splitting the location column to city and state
df2["state"]=df2.Location.str.split(', ',expand=True).iloc[:,1]


# In[108]:


df2


# In[109]:


df2['state'].value_counts()[:10]


# In[181]:


s = df2['state'].value_counts()[0:10]
s = dict(s)
print(s)


# In[182]:


states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


# In[184]:


slices = list(s.values())
labels = list(s.keys())
labels = [l.replace(l,states[l]) for l in labels] #Replacing abbreviation like CA, NY with California, New York etc.


labels.reverse()
slices.reverse()
plt.barh(labels, slices, color='red',animated=True)
plt.title("Top 10 States for 'Data Scientist' Job Listings")
plt.xlabel("Frequency")
plt.tight_layout()
plt.show()


# In[171]:


slices = list(s.values())
labels = list(s.keys())

labels = [l.replace(l,states[l]) for l in labels] #Replacing abbreviation like CA, NY with California, New York etc.
explode = [0.1,0,0,0,0]
plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=90, autopct="%1.1f%%",
       wedgeprops={'edgecolor':'black'})
plt.title("Top States for 'Data Scientist' Job Listings")
plt.tight_layout()
plt.show()


# In[120]:


df2['city'].value_counts()[:10]


# In[121]:


df2['Location'].value_counts()[:20]


# In[175]:


l = df2['city'].value_counts()[0:10]

d = dict(l)
print(d)


# In[174]:


slices = list(d.values())
labels = list(d.keys())


plt.pie(slices, labels=labels, shadow=True, startangle=90, autopct="%1.1f%%",
       wedgeprops={'edgecolor':'black'})
plt.title("Top Cities for 'Data Scientist' Job listings")
plt.tight_layout()
plt.show()


# In[ ]:





# In[180]:


slices = list(d.values())
labels = list(d.keys())
labels.reverse()
slices.reverse()
plt.barh(labels, slices, color='orange',animated=True)
plt.title("Top 10 Cities for 'Data Scientist' Job Listings")
plt.xlabel("Frequency")
plt.tight_layout()
plt.show()


# In[ ]:





# In[200]:


details = df['Description'].values.tolist() #convert dataframe to list
len(details)


# In[201]:


text = ' '.join(details) #joining all the strings in the list separated by ' '
len(text)


# In[198]:


pattern = re.compile(r'\d{1,2}\+?\syears?')
matches = pattern.findall(text)
print(matches[0:5])

