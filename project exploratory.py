#!/usr/bin/env python
# coding: utf-8

# In[4]:


# import python libraries
import pandas as pd
import numpy as nm
import matplotlib.pyplot as plt # visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df=pd.read_csv('Diwali Sales Data.csv',encoding='unicode_escape')


# In[3]:


df.head()


# In[5]:


df.shape


# In[7]:


df.info()


# In[9]:


#drop unrelated/blank columns
df.drop(['Status','unnamed1'],axis=1,inplace=True)


# In[11]:


pd.isnull(df).sum()


# In[12]:


#drop null value
df.dropna(inplace=True)


# In[10]:


df.columns


# In[14]:


# change data type
df['Amount'] = df['Amount'].astype('int')


# In[15]:


df['Amount'].dtypes


# In[16]:


#rename column
df.rename(columns= {'Marital_Status':'Shaadi'})


# In[17]:


# describe() method returns description of the data in the DataFrame (i.e. count, mean, std, etc)
df.describe()


# In[18]:


# use describe() for specific columns
df[['Age', 'Orders', 'Amount']].describe()


# # Exploratory Data Analysis

# ## Gender

# In[19]:


# plotting a bar chart for Gender and it's count

ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[20]:


# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)


#  From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men

# # Age 

# In[27]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[28]:


# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# From above graphs we can see that most of the buyers are of age group between 26-35 yrs female

# # State

# In[29]:


# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[30]:


# total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')


# From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively

# # Marital Status

# In[31]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[33]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# From above graphs we can see that most of the buyers are married (women) and they have high purchasing power

# # Occupation

# In[34]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[15]:





# In[35]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector

# # Product Category

# In[36]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[37]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category

# In[38]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[39]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # Conclusion:

# ## Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category

# ## Thank you!

# In[ ]:




