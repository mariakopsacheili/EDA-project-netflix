#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns', None)
from datetime import datetime


# In[6]:


df = pd.read_csv('Netflix TV Shows and Movies.csv')


# In[104]:


df2=df.copy()
df2


# In[105]:


df2


# In[106]:


df2.info()


# In[107]:


df2.describe()


# In[108]:


df2.dropna(subset = ['imdb_votes'], inplace=True)
df2


# In[109]:


df2.info()


# In[110]:


#weighted score
df2['weighted_score'] = df2['imdb_score'] * df2['imdb_votes']
df2.info()


# In[111]:


df2


# In[112]:


df2.info()


# In[48]:


#normalized score
#df2["normalized_weighted_score"] = (df2["weighted_score"] - df2["weighted_score"].min()) \
                                              #  / (df2["weighted_score"].max() - df2["weighted_score"].min()) * 100


# In[115]:


df2.info()


# In[33]:





# In[116]:


df2


# # movies over8.5
# 

# In[153]:


df3 = df2[df2['type'] == 'MOVIE']
top_rated=df3[df3['imdb_score']>= 8.5]
top10 = top_rated.sort_values(by='imdb_votes', ascending = False).head(10)
top10


# # age restrictions

# In[119]:


dropage = df3[df3['age_certification'].notna()]
dropage


# In[123]:


plotage=dropage.groupby(['age_certification']).count().sort_values(by='title', ascending=False)
plotage


# In[126]:


sns.barplot(x='age_certification', y='index', data=plotage)
plt.title('Top Movies Age Restrictions')
plt.show()


# # 3 movie lenght

# In[140]:


df2.info()


# In[141]:


dflenght = df2[df2['type'] == 'MOVIE']
dflenght


# In[148]:


toplenght= dflenght[dflenght['imdb_score']>= 8.5]


# In[149]:


toplenght


# In[154]:


runtime=toplenght['runtime'].value_counts()
runtime.sortby


# In[ ]:





# In[ ]:




