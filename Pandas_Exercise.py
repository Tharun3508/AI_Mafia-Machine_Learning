#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# <center>Introduction to Pandas</center>

get_ipython().system('[](https://pandas.pydata.org/_static/pandas_logo.png)')


## Installation

Simply,
```
pip install pandas
```


## Reading data from a CSV file

You can read data from a CSV file using the ``read_csv`` function. By default, it assumes that the fields are comma-separated.


# In[1]:


# import pandas
import numpy as np
import pandas as pd


# >The `imdb.csv` dataset contains Highest Rated IMDb "Top 1000" Titles.

# In[2]:


# load imdb dataset as pandas dataframe
df = pd.read_csv(r"C:\Users\PUTTA THARUN SAI\imdb_1000.csv")


# In[3]:


# show first 5 rows of imdb_df
df.head()


# In[4]:


## >The `bikes.csv` dataset contains information about the number of bicycles that used certain bicycle lanes in Montreal in the year 2012.


# In[5]:


# load bikes dataset as pandas dataframe
df1 = pd.read_csv(r"C:\Users\PUTTA THARUN SAI\bikes.csv",sep = ';')


# In[6]:


# show first 3 rows of bikes_df
df1.head(3)


# In[7]:


## Selecting columns

When you read a CSV, you get a kind of object called a DataFrame, which is made up of rows and columns. You get columns out of a DataFrame the same way you get elements out of a dictionary.


# In[8]:


# list columns of imdb_df
df.columns


# In[9]:


# what are the datatypes of values in columns
df.dtypes


# In[10]:


# list first 5 movie titles
df.loc[0:5,["title"]]


# In[11]:


# show only movie title and genre
df[['title','genre']]


# ## Understanding columns
# 
# On the inside, the type of a column is ``pd.Series`` and pandas Series are internally numpy arrays. If you add ``.values`` to the end of any Series, you'll get its internal **numpy array**.

# In[12]:


# show the type of duration column
df['duration'].dtype


# In[13]:


# show duration values of movies as numpy arrays
d = np.array(df['duration'])
print(d)


# ## Applying functions to columns
# 
# Use `.apply` function to apply any function to each element of a column.

# In[14]:


# convert all the movie titles to uppercase
upper_case = lambda x: x.upper()
df['title'].apply(upper_case)


# ## Plotting a column
# 
# Use ``.plot()`` function!

# In[15]:


# plot the bikers travelling to Berri1 over the year
import matplotlib.pyplot as plt
fig= plt.figure(figsize=(10,10))
plt.plot(df1['Date'],df1['Berri1'])
plt.xlabel('Date')
plt.ylabel('Bikers travelling to Berri1')
plt.title('Bikers Data')

plt.show()


# In[16]:


# plot all the columns of bikes_df
fig= plt.figure(figsize=(10,10))
plt.plot(df1['Date'] ,df1.loc[0:,'Rachel / Papineau' : 'Pont_Jacques_Cartier'])
plt.xlabel('Date')
plt.ylabel('Bikers travelling to Berri1')
plt.title('Bikers Data')

plt.show()


# ## Value counts
# 
# Get count of unique values in a particular column/Series.

# In[17]:


# what are the unique genre in imdb_df?
gen_arr = pd.unique(df['genre'])
gen_arr


# In[18]:


# plotting value counts of unique genres as a bar chart
fig= plt.figure(figsize=(10,10))
df['genre'].value_counts().plot(kind = 'bar')


# In[19]:


# plotting value counts of unique genres as a pie chart
fig= plt.figure(figsize=(16,16))
df['genre'].value_counts().plot(kind = 'pie')


# ## Index
# 
# ### DATAFRAME = COLUMNS + INDEX + ND DATA
# 
# ### SERIES = INDEX + 1-D DATA
# 
# **Index** or (**row labels**) is one of the fundamental data structure of pandas. It can be thought of as an **immutable array** and an **ordered set**.
# 
# > Every row is uniquely identified by its index value.

# In[20]:


# show index of bikes_df
df1.index.values


# In[21]:


# get row for date 2012-01-01
df2 = df1[(df1['Date'] == '2012-01-01')]
df2


# #### To get row by integer index:
# 
# Use ``.iloc[]`` for purely integer-location based indexing for selection by position.

# In[22]:


# show 11th row of imdb_df using iloc
df1.iloc[10]


# ## Selecting rows where column has a particular value

# In[23]:


# select only those movies where genre is adventure
df3 = df[(df['genre'] == 'Adventure')]
df3


# In[47]:


# which genre has highest number of movies with star rating above 8 and duration more than 130 minutes?
df4 = df[(df['star_rating'] > 8) & (df['duration'] > 130)]
df4['genre'].value_counts().index[0]


# ## Adding a new column to DataFrame

# In[58]:


# add a weekday column to bikes_df


# ## Deleting an existing column from DataFrame

# In[26]:


# remove column 'Unnamed: 1' from bikes_df
df5 = df1.drop('Unnamed: 1', axis=1)
df5


# ## Deleting a row in DataFrame

# In[27]:


# remove row no. 1 from bikes_df
df1.drop([0])


# ## Group By
# 
# Any groupby operation involves one of the following operations on the original object. They are −
# 
# - Splitting the Object
# 
# - Applying a function
# 
# - Combining the results
# 
# In many situations, we split the data into sets and we apply some functionality on each subset. In the apply functionality, we can perform the following operations −
# 
# - **Aggregation** − computing a summary statistic
# 
# - **Transformation** − perform some group-specific operation
# 
# - **Filtration** − discarding the data with some condition

# In[35]:


# group imdb_df by movie genres
genre = df.groupby('genre')
genre


# In[31]:


# get crime movies group
genre.get_group('Crime')


# In[34]:


# get mean of movie durations for each group
mean_dur = genre['duration'].mean()
mean_dur


# In[41]:


# change duration of all movies in a particular genre to mean duration of the group
n = len(df.index)
for i in range(n):
    df.loc[i,'duration'] = mean_dur[df.loc[i,'genre']]

df


# In[45]:


# drop groups/genres that do not have average movie duration greater than 120.
n = len(df.index)
for i in range(n):
    if(df.loc[i,'duration'] < 120):
        df.drop(i,inplace = True)

df


# In[59]:


# group weekday wise bikers count
weekday_grp = df1.groupby(['Weekday'])


# In[ ]:


# get weekday wise biker count


# In[ ]:


# plot weekday wise biker count for 'Berri1'


# ![](https://memegenerator.net/img/instances/500x/73988569/pythonpandas-is-easy-import-and-go.jpg)
