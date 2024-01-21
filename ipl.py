#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


ipl=pd.read_csv('C:\Users\kumar\OneDrive\Documents\pythonproject matches.csv')


# In[6]:


ipl=pd.read_csv('C:\Users\kumar\OneDrive\Documents\python project.csv')


# In[8]:


ipl=pd.read_csv('C:/Users/kumar/OneDrive/Documents/python project/matches.csv')


# In[9]:


ipl.head()


# In[10]:


ipl.shape


# In[11]:


ipl['player_of_match'].value_counts()


# In[12]:


ipl['player_of_match'].value_counts()[0:10]


# In[13]:


ipl['player_of_match'].value_counts()[0:5]


# In[18]:


plt.figure(figsize=(8,5))
plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()),list(ipl['player_of_match'].value_counts()[0:5]),color="g")
plt.show()


# In[22]:


plt.figure(figsize=(8,5))
plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()),list(ipl['player_of_match'].value_counts()[0:5]),color="g")
plt.show()


# In[23]:


ipl['result'].value_count()


# In[24]:


ipl['result'].value_counts()


# In[25]:


ipl['toss_winner'].value_counts()


# In[26]:


batting_first.head()


# In[30]:


#making a histogram
plt.figure(figsize=(5,7))
plt.hist(batting_first['win_by_runs'])
plt.title("Distribution of Runs")
plt.xlabel("Runs")
plt.show()


# In[28]:


batting_first=ipl[ipl['win_by_runs']!=0]


# In[29]:


batting_first.head()


# In[31]:


#finding out the number of wins wrt each team after batting first
batting_first['winner'].value_counts()


# In[33]:


#making a bar plot for top 3 teams with most wins after batting first
plt.figure(figsize=(6,6))
plt.bar(list(batting_first['winner'].value_counts()[0:3].keys()),list(batting_first['winner'].value_counts()[0:3]),color=["blue","yellow","orange"])
plt.show()


# In[35]:


#making a pie chart
plt.figure(figsize=(7,7))
plt.pie(list(batting_first['winner'].value_counts()),labels=list(batting_first['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[36]:


#extracting those records where a team has won after batting second
batting_second=ipl[ipl['win_by_wickets']!=0]


# In[37]:


#looking at the head
batting_second.head()


# In[38]:


#Making a histogram for frequency of wins w.r.t number of wickets
plt.figure(figsize=(7,7))
plt.hist(batting_second['win_by_wickets'],bins=30)
plt.show()


# In[39]:


#Finding out the frequency of number of wins w.r.t each time after batting second
batting_second['winner'].value_counts()


# In[40]:


#Making a pie chart for distribution of most wins after batting second
plt.figure(figsize=(7,7))
plt.pie(list(batting_second['winner'].value_counts()),labels=list(batting_second['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[41]:


#Looking at the number of matches played each season
ipl['season'].value_counts()


# In[42]:


#Looking at the number of matches played in each city
ipl['city'].value_counts()


# In[43]:


#Finding out how many times a team has won the match after winning the toss
import numpy as np
np.sum(ipl['toss_winner']==ipl['winner'])


# In[ ]:




