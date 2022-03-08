#!/usr/bin/env python
# coding: utf-8

# # Strings

# In[1]:


# defining a string 

String = "Teja"
type(String)


# In[2]:


# Builtins in String


# In[3]:


dir(String)


# In[5]:


# Working with all the builtins
Capitalized_String = String.capitalize()
print(Capitalized_String)


# In[12]:


help(String.casefold)


# In[14]:


# performing slicing operations on strings 
string_data = "Python is awesome"


# In[15]:


string_data[0]


# In[17]:


string_data[1:5]


# In[18]:


len(string_data)


# In[24]:


string_data[-5:-1]


# In[25]:


string_data[-1:-10:-1]


# In[26]:


string_data[-1:-5:-1]


# In[28]:


Center = String.center(10)
print(Center)


# In[30]:


Count = String.count('T')
print(Count)


# In[31]:


EndsWith = String.endswith('a')
print(EndsWith)


# In[32]:


help(String.expandtabs)


# In[33]:


ExpandTabs = String.expandtabs(tabsize = 16)
print(ExpandTabs)


# In[35]:


print(String * 3)


# In[36]:


print(String + 3)


# In[37]:


print(f"Hello Welcome to python")


# In[39]:


print("Good Morning! Welcome to python tutorials. Hello %s" %(String))


# In[40]:


print('Hello Raviteja what\'s up?')


# In[41]:


# multi line strings
print('''Hello Raviteja
        how is the course?
        Would you mind rating the course on a scale of 5''')


# In[42]:


# comments in python
# This is a single line comment
'''
Hello there!
'''


# In[43]:


"""
This is a multiline comment
"""
print("Hello Teja")


# In[46]:


s = "Ravi"
print("Hello there! how is you day? {}".format(s))


# In[ ]:




