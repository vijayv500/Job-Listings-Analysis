#!/usr/bin/env python
# coding: utf-8

# In[41]:


import csv
import requests
from bs4 import BeautifulSoup
import re


# In[42]:


def get_jobdetails(job):
    
    try:
        job_location = job.find('div','recJobLoc').get('data-rc-loc')
    except AttributeError:
        job_location =''
    
    a = job.h2.a
    job_url_initial = 'https://www.indeed.com/viewjob?' + a.get('href')
    pattern = re.compile(r'(/rc/clk\?)')
    job_url = re.sub(pattern,'',job_url_initial)
    
    page = requests.get(job_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    try:
        job_title = job.find('div','jobsearch-JobInfoHeader-title-container').text.strip()
    except AttributeError:
        job_title = ''
    
    try:
        company = job.find('div','jobsearch-CompanyReview--heading').text.strip()
    except AttributeError:
        company = ''
        
    try:
        job_des1 = job.find('div','jobsearch-jobDescriptionText').text.strip() 
        job_des2 = BeautifulSoup(job_des1,'lxml')
        pattern = re.compile(r'(<html><body><p>|</p></body></html>|Job requisition #|R\d+)')
        job_des = re.sub(pattern,'',str(job_des2))
    except AttributeError:
        job_des = ''

    
    job = (job_title,company,job_location,job_des,job_url)
    
    return job


# In[43]:


def fetch_data(designation, location):
    
    jobs_list = []  
    
    template = 'https://www.indeed.com/jobs?q={}&l={}'
    url = template.format(designation, location)
    
    while True:
        page = requests.get(url)    
        soup = BeautifulSoup(page.text, 'html.parser')
        jobs = soup.find_all('div','jobsearch-SerpJobCard')

        for job in jobs:
            job = get_jobdetails(job)
            jobs_list.append(job)

        try:
            url = 'https://www.indeed.com' + soup.find('a',{'aria-label':'Next'}).get('href')
        except AttributeError:
            break   
            
    with open('scraped_jobs.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['Title','Company','Location','Description','URL'])
        w.writerows(jobs_list)     


# In[ ]:


fetch_data('data scientist','united states')


# In[ ]:




