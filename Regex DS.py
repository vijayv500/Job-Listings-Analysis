#!/usr/bin/env python
# coding: utf-8

# In[4]:


import csv
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re


descs = []
with open('500 descriptions.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        descs.append(row[0])

len(descs)
        
 


# In[5]:


text = ' '.join(descs)


# In[6]:


len(text)


# In[7]:


pattern = re.compile(r'\d{1,2}\+?\syears?')
matches = pattern.findall(text)

print(matches[0:5])
len(matches)


# In[8]:


exp = Counter(matches)


# In[9]:


exp = dict(sorted(exp.items(), reverse=True,key=lambda item: item[1])) #sorting dict in descending order of values
exp
# experience=[1,2,3,4,5,6,7,8,9,10,11,12] #hardcoded
# times = [51,116,104,46,78,18,23,9,1,10,1,4]


# In[167]:


experience=[1,2,3,4,5,6,7,8,9,10,11,12]
Frequency = [51,116,104,46,78,18,23,9,1,10,1,4]
plt.bar(experience,Frequency,color='black')
plt.legend()
plt.title("Job Experience Sought in 'Data Scientist' Job Listings")
plt.xlabel("Years of experience")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:





# In[40]:


pattern = re.compile(r'\bR\b')
matches = pattern.findall(text)
len(matches)


# In[41]:


pattern = re.compile(r'(Python|python)')
matches = pattern.findall(text)
len(matches)


# In[60]:


pattern = re.compile(r'(SQL|sql|Sql)')
matches = pattern.findall(text)
len(matches)


# In[63]:


pattern = re.compile(r'(Java|java)')
matches = pattern.findall(text)
len(matches)


# In[50]:


pattern = re.compile(r'C\+\+')
matches = pattern.findall(text)
len(matches)


# In[99]:


pattern = re.compile(r'(Matlab|matlab)')
matches = pattern.findall(text)
len(matches)


# In[87]:


pattern = re.compile(r'(JavaScript|Javascript|javascript)')
matches = pattern.findall(text)
len(matches)


# In[168]:


labels= ['Python','SQL','R','Java','C++','Matlab','JavaScript']
freq= [482,364,350,97,48,25,15]
labels.reverse()
freq.reverse()
plt.barh(labels, freq, animated=True)
plt.title("Programming Languages sought for 'Data Scientist' Job Listings")
plt.xlabel("Frequency")
plt.tight_layout()
plt.show()


# In[ ]:





# In[88]:


pattern = re.compile(r'(Hadoop|hadoop)')
matches = pattern.findall(text)
len(matches)


# In[90]:


pattern = re.compile(r'(Spark|spark)')
matches = pattern.findall(text)
len(matches)


# In[91]:


pattern = re.compile(r'(Hive|hive)')
matches = pattern.findall(text)
len(matches)


# In[183]:


freq = [117,66,45]
labels=["Spark","Hadoop","Hive"]


# In[184]:


plt.pie(freq, labels=labels, autopct="%1.1f%%",
       wedgeprops={'edgecolor':'black'})
plt.title("Big Data skills Sought in 'Data Scientist' Job Listings (relative)")
plt.tight_layout()
plt.show()


# In[97]:


pattern = re.compile(r'([Mm]achine [Ll]earning|ML)')
matches = pattern.findall(text)
len(matches)


# In[ ]:





# In[100]:


pattern = re.compile(r'[Dd]ocker')
matches = pattern.findall(text)
len(matches)


# In[105]:


pattern = re.compile(r'[Kk]ubernetes')
matches = pattern.findall(text)
len(matches)


# In[111]:


pattern = re.compile(r'[Jj]enkins')
matches = pattern.findall(text)
len(matches)


# In[ ]:





# In[107]:


pattern = re.compile(r'([Nn]atural [Ll]anguage [Pp]rocessing|NLP)')
matches = pattern.findall(text)
len(matches)


# In[140]:


pattern = re.compile(r'[Cc]omputer [Vv]ision')
matches = pattern.findall(text)
len(matches)


# In[141]:


pattern = re.compile(r'[Rr]einforcement [Ll]earning')
matches = pattern.findall(text)
len(matches)


# In[142]:


pattern = re.compile(r'[Ss]tructured [Dd]ata')
matches = pattern.findall(text)
len(matches)


# In[178]:


freq = [161,47,82,11]
labels = ['NLP','Computer Vision','Time-series Data','Reinforcment Learning']
explode = [0,0,0,0,0]

plt.pie(freq, labels=labels, autopct="%1.1f%%",
       wedgeprops={'edgecolor':'black'})
plt.title("Types of Data/Algorithms - 'Data Scientist' Job Listings (relative)")
plt.tight_layout()
plt.show()


# In[ ]:





# In[124]:


pattern = re.compile(r'[Tt]ableau')
matches = pattern.findall(text)
len(matches)


# In[123]:


pattern = re.compile(r'(PowerBI|Power BI)')
matches = pattern.findall(text)
len(matches)


# In[115]:


pattern = re.compile(r'[Ll]ooker')
matches = pattern.findall(text)
len(matches)


# In[177]:


freq = [115,30,17]
labels = ['Tableau','Power BI','Looker']
explode = [0,0,0,0,0]

plt.pie(freq, labels=labels, shadow=True, startangle=90, autopct="%1.1f%%",
       wedgeprops={'edgecolor':'black'})
plt.title("Dataviz Tools Sought in 'Data Scientist' Job Listings (relative)")
plt.tight_layout()
plt.show()


# In[ ]:





# In[116]:


pattern = re.compile(r'AWS')
matches = pattern.findall(text)
len(matches)


# In[117]:


pattern = re.compile(r'Azure')
matches = pattern.findall(text)
len(matches)


# In[119]:


pattern = re.compile(r'(GCP|[Gg]oogle [Cc]loud)')
matches = pattern.findall(text)
len(matches)


# In[186]:


freq = [104,46,30]
labels = ["AWS","Azure","GCP"]
explode = [0,0,0,0,0]

plt.pie(freq, labels=labels, shadow=True, startangle=90, autopct="%1.1f%%",
       wedgeprops={'edgecolor':'black'})
plt.title("Cloud Skills Sought in 'Data Scientist' Job Listings (relative)")
plt.tight_layout()
plt.show()


# In[ ]:





# In[136]:


pattern = re.compile(r'[Tt]ensor[Ff]low')
matches = pattern.findall(text)
len(matches)


# In[137]:


pattern = re.compile(r'(PyTorch|pytorch|Pytorch)')
matches = pattern.findall(text)
len(matches)


# In[138]:


pattern = re.compile(r'[Kk]eras')
matches = pattern.findall(text)
len(matches)


# In[185]:


freq = [60,42,20]
labels = ['Tensorflow','Pytorch','Keras']

plt.pie(freq, labels=labels, shadow=True, startangle=90, autopct="%1.1f%%",
       wedgeprops={'edgecolor':'black'})
plt.title("ML Frameworks Sought in 'Data Scientist' Job Listings (relative)")
plt.tight_layout()
plt.show()


# In[ ]:




