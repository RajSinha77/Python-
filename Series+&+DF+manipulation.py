
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.0** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-data-analysis/resources/0dhYG) course resource._
# 
# ---

# # The Series Data Structure

# In[1]:


import pandas as pd
get_ipython().magic('pinfo pd.Series')


# In[2]:


animals = ['Tiger', 'Bear', 'Moose']
pd.Series(animals)


# In[3]:


numbers = [1, 2, 3]
pd.Series(numbers)


# In[4]:


animals = ['Tiger', 'Bear', None]
pd.Series(animals)


# In[5]:


numbers = [1, 2, None]
pd.Series(numbers)


# In[6]:


import numpy as np
np.nan == None


# In[7]:


np.nan == np.nan


# In[8]:


np.isnan(np.nan)


# In[9]:


sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
s


# In[10]:


s.index


# In[11]:


s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
s


# In[12]:


sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports, index=['Golf', 'Sumo', 'Hockey'])
s


# # Querying a Series

# In[13]:


sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
s


# In[14]:


s.iloc[3]


# In[15]:


s.loc['Golf']


# In[16]:


s[3]


# In[17]:


s['Golf']


# In[20]:


sports = {99: 'Bhutan',
          100: 'Scotland',
          101: 'Japan',
          102: 'South Korea'}
s = pd.Series(sports)


# In[21]:


s[0] #This won't call s.iloc[0] as one might expect, it generates an error instead


# In[22]:


s = pd.Series([100.00, 120.00, 101.00, 3.00])
s


# In[23]:


total = 0
for item in s:
    total+=item
print(total)


# In[24]:


import numpy as np

total = np.sum(s)
print(total)


# In[25]:


#this creates a big series of random numbers
s = pd.Series(np.random.randint(0,1000,10000))
s.head()


# In[26]:


len(s)


# In[27]:


get_ipython().run_cell_magic('timeit', '-n 100', 'summary = 0\nfor item in s:\n    summary+=item')


# In[29]:


get_ipython().run_cell_magic('timeit', '-n 100', 'summary = np.sum(s)')


# In[30]:


s+=2 #adds two to each item in s using broadcasting
s.head()


# In[31]:


for label, value in s.iteritems():
    s.set_value(label, value+2)
s.head()


# In[41]:


get_ipython().run_cell_magic('timeit', '-n 10', 's = pd.Series(np.random.randint(0,1000,10000))\nfor label, value in s.iteritems():\n    s.loc[label]= value+2')


# In[33]:


get_ipython().run_cell_magic('timeit', '-n 10', 's = pd.Series(np.random.randint(0,1000,10000))\ns+=2')


# In[34]:


s = pd.Series([1, 2, 3])
s.loc['Animal'] = 'Bears'
s


# In[35]:


original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'})
cricket_loving_countries = pd.Series(['Australia',
                                      'Barbados',
                                      'Pakistan',
                                      'England'], 
                                   index=['Cricket',
                                          'Cricket',
                                          'Cricket',
                                          'Cricket'])
all_countries = original_sports.append(cricket_loving_countries)


# In[36]:


original_sports


# In[37]:


cricket_loving_countries


# In[38]:


all_countries


# In[39]:


all_countries.loc['Cricket']


# # The DataFrame Data Structure

# In[42]:


import pandas as pd
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
df.head()


# In[43]:


df.loc['Store 2']


# In[44]:


type(df.loc['Store 2'])


# In[45]:


df.loc['Store 1']


# In[46]:


df.loc['Store 1', 'Cost']


# In[47]:


df.T


# In[48]:


df.T.loc['Cost']


# In[49]:


df['Cost']


# In[50]:


df.loc['Store 1']['Cost']


# In[51]:


df.loc[:,['Name', 'Cost']]


# In[52]:


df.drop('Store 1')


# In[53]:


df


# In[54]:


copy_df = df.copy()
copy_df = copy_df.drop('Store 1')
copy_df


# In[55]:


get_ipython().magic('pinfo copy_df.drop')


# In[56]:


del copy_df['Name']
copy_df


# In[57]:


df['Location'] = None
df


# # Dataframe Indexing and Loading

# In[58]:


costs = df['Cost']
costs


# In[59]:


costs+=2
costs


# In[60]:


df


# In[61]:


get_ipython().system('cat olympics.csv')


# In[62]:


df = pd.read_csv('olympics.csv')
df.head()


# In[63]:


df = pd.read_csv('olympics.csv', index_col = 0, skiprows=1)
df.head()


# In[64]:


df.columns


# In[65]:


for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#' + col[1:]}, inplace=True) 

df.head()


# # Querying a DataFrame

# In[66]:


df['Gold'] > 0


# In[67]:


only_gold = df.where(df['Gold'] > 0)
only_gold.head()


# In[68]:


only_gold['Gold'].count()


# In[69]:


df['Gold'].count()


# In[70]:


only_gold = only_gold.dropna()
only_gold.head()


# In[71]:


only_gold = df[df['Gold'] > 0]
only_gold.head()


# In[72]:


len(df[(df['Gold'] > 0) | (df['Gold.1'] > 0)])


# In[73]:


df[(df['Gold.1'] > 0) & (df['Gold'] == 0)]


# # Indexing Dataframes

# In[74]:


df.head()


# In[75]:


df['country'] = df.index
df = df.set_index('Gold')
df.head()


# In[76]:


df = df.reset_index()
df.head()


# In[77]:


df = pd.read_csv('census.csv')
df.head()


# In[78]:


df['SUMLEV'].unique()


# In[79]:


df=df[df['SUMLEV'] == 50]
df.head()


# In[80]:


columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']
df = df[columns_to_keep]
df.head()


# In[81]:


df = df.set_index(['STNAME', 'CTYNAME'])
df.head()


# In[82]:


df.loc['Michigan', 'Washtenaw County']


# In[83]:


df.loc[ [('Michigan', 'Washtenaw County'),
         ('Michigan', 'Wayne County')] ]


# # Missing values

# In[84]:


df = pd.read_csv('log.csv')
df


# In[85]:


get_ipython().magic('pinfo df.fillna')


# In[86]:


df = df.set_index('time')
df = df.sort_index()
df


# In[87]:


df = df.reset_index()
df = df.set_index(['time', 'user'])
df


# In[88]:


df = df.fillna(method='ffill')
df.head()

