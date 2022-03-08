#!/usr/bin/env python
# coding: utf-8

# # Built-in Functions

# In[1]:


# To check the python version
get_ipython().system('python --version')


# In[2]:


# To retrieve all the builtin functions on the console
import builtins


# In[3]:


dir(builtins)


# In[4]:


help('modules')


# # Variables

# In[5]:


# storing values in variables i.e; A random memory location in a computer storage

salary = 30000
print(salary)
print(type(salary))
print(id(salary))


# In[6]:


# Assigning values to variables 
x,y,z = 1,2,3
print(x,y,z)


# # Data Types

# In[7]:


# Numerical (Integer,Float,Complex)
# Sequnce Type (Strings,Lists,Tuples)
# Dictionary
# Sets
# Boolean (True,False)


# In[8]:


Integer_type = 20
type(Integer_type)


# In[9]:


Float_type = 20.2
type(Float_type)


# In[10]:


Complex_type = 1+2j
type(Complex_type)


# In[11]:


# Sequence Type

String_data = "Raviteja"
type(String_data)


# In[12]:


List = [1,2,3,4,5]
type(List)


# In[13]:


Tuple_data = (1,2,3,4,5)
type(Tuple_data)


# In[14]:


# Dictionary
Dictionary_data = {"a":1,"b":2,"c":[1,2,3]}
type(Dictionary_data)


# In[15]:


# Sets
# It is a collection of Unorder Distinct data.
Set_data = set()


# In[16]:


dir(Set_data)


# In[18]:


Set_data.add(1)


# In[19]:


for i in range(2,6):
    Set_data.add(i)
print(Set_data)


# In[20]:


Set_data.add(List)


# In[21]:


Set_data.add(String_data)


# In[22]:


print(Set_data)


# In[23]:


Set_data.add(Tuple_data)


# In[24]:


print(Set_data)


# In[25]:


# Boolean data type
Boolean_data_1 = True
type(Boolean_data_1)
Boolean_data_2 = False
type(Boolean_data_2)


# In[ ]:




