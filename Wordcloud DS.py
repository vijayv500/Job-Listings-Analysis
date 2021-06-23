#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt


companies = []
with open('companies.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        companies.append(row[0])

print(companies[0:11])


# In[3]:


word_could_dict=Counter(companies)
wordcloud = WordCloud(width = 1600, height = 800,max_words=50,background_color='white').generate_from_frequencies(word_could_dict)
plt.figure(figsize=(40,30))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()


# In[4]:


word_could_dict


# In[ ]:




