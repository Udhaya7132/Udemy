#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split


# In[2]:


df = pd.read_csv("C:/Users/UDHAYA KUMAR . R/Desktop/udemy_courses.csv")


# In[3]:


df.head()


# In[4]:


df.info()


# In[6]:


df.isnull().sum()


# In[8]:


df.isna().sum()


# In[9]:


df.describe()


# In[12]:


df.shape


# In[14]:


df.duplicated().sum()


# In[16]:


df.drop_duplicates(inplace=True)


# In[18]:


df.shape


# In[19]:


df.info()


# In[20]:


df['subject'].value_counts()


# In[28]:


sns.countplot(x=df['subject'])


# In[35]:


colors = ['orange', 'green', 'red', 'blue']

df['subject'].value_counts().plot(kind='bar',color=colors,rot=60)
height=10
for i ,count in enumerate(df['subject'].value_counts()):
    plt.text(x=i,y=count+height,s=count, ha='center')
plt.show()


# In[37]:


df.info()


# In[39]:


df['level'].unique()


# In[40]:


df['level'].value_counts()


# In[48]:


colors = ['orange', 'green', 'red', 'blue']
df['level'].value_counts().plot(kind='bar',color=colors)

height = 20

for i,count in enumerate(df['level'].value_counts()):
    plt.text(x=i,y=count+height,s=count,ha='center')
    
plt.show()


# Display The Count of Paid and Free Courses

# In[49]:


df.columns


# In[51]:


df['is_paid'].value_counts()


# In[58]:


sns.countplot(x=df['is_paid'])

plt.xlabel("Level", fontsize = 13)
plt.ylabel("Number of Free And Paid Courses",fontsize = 13)
plt.show()


# Which Course Has More Lectures (Free or Paid)?

# In[66]:


df.groupby(['is_paid']).mean(numeric_only=True)


# Which Courses Have A Higher Number of Subscribers Free or Paid?

# In[86]:


sns.barplot(x="is_paid",y="num_subscribers",data=df)
plt.xticks(rotation=60)
plt.show()


# In[80]:


x=df['price']
y=df['num_subscribers']

plt.scatter(x,y)
plt.show()


# Which Level Has The Highest Number of Subscribers

# In[87]:


sns.barplot(x="level",y="num_subscribers",data=df)
plt.xticks(rotation=60)
plt.show()


# In[89]:


df.columns


# Find Most Popular Course Title

# In[92]:


df[df['num_subscribers'].max() == df['num_subscribers']]['course_title']


# Display 10 Most Popular Courses As Per Number of
# Subscribers

# In[94]:


df.columns


# In[100]:


top10 = df.sort_values(by='num_subscribers',ascending=False)


# In[101]:


top10.head()


# In[103]:


sns.barplot(x='num_subscribers',y='course_title',data=top10.head(10))

plt.show()


# Find The Course Which Is Having The Highest Number of Reviews.
# 

# In[104]:


df.columns


# In[106]:


plt.figure(figsize=(10,6))
sns.barplot(x='subject',y='num_reviews',data=df)
plt.show()


# In[107]:


df['course_title'].value_counts()


# In[119]:


a=print("Total no.of Python Courses",len(df[df['course_title'].str.contains('python', case=False)]))
b=print("Total no.of Forex Courses",len(df[df['course_title'].str.contains('forex', case=False)]))
c=print("Total no.of HTML Courses",len(df[df['course_title'].str.contains('HTML', case=False)]))
d=print("Total no.of Accounts Courses",len(df[df['course_title'].str.contains('accounts', case=False)]))


# Display 10 Most Popular Python Courses As Per Number of Subscribers

# In[131]:


python = df[df['course_title'].str.contains('python',case=False)].\
sort_values(by='num_subscribers',ascending=False).head(10)


# In[133]:


sns.barplot(x="num_subscribers",y="course_title",data=python)

plt.show()


# In Which Year The Highest Number of Courses Were Posted

# In[134]:


df.columns


# In[141]:


df['published_timestamp'] = pd.to_datetime(df['published_timestamp'])

df['Year'] = df['published_timestamp'].dt.year

most_common_year = df['Year'].value_counts().idxmax()

print("The year with the highest number of courses:", most_common_year)


# In[143]:


df['Year'].value_counts()


# In[144]:


sns.countplot(x=df['Year'],data=df)


# In[146]:


df.groupby(df['Year'])['subject'].value_counts().idxmax()


# In[147]:


df.groupby(df['Year'])['subject'].value_counts()


# In[ ]:




