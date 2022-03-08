#!/usr/bin/env python
# coding: utf-8

# # Lists

# In[1]:


# initializing an empty list


# In[2]:


l1 = []
print(l1)


# In[3]:


bool(l1)


# In[4]:


type(l1)


# In[14]:


# intitializing non empty list
l2 = [1,2,3,4,5]
print(l2)


# In[15]:


print(type(l2))


# In[16]:


print(bool(l2))


# In[17]:


# adding values to a list

for i in range(6,11):
    l2.append(i)
print(l2)


# In[12]:


clear(l2)


# In[18]:


print(l2)


# In[19]:


# inbuilt functions in list
dir(l2)


# In[20]:


# Assigning a list with the help of .copy creates deep copy

l3 = l2.copy()
print(l3)


# In[21]:


print(id(l2))


# In[22]:


print(id(l3))


# In[23]:


l3.append(11)
print(l3)


# In[24]:


print(l2)


# In[25]:


print(id(l2))
print(id(l3))


# In[26]:


l4 = l3
print(l4)


# In[27]:


# Assigning a list without .copy creates a shallow copy of the list

print(id(l3))
print(id(l4))


# In[28]:


l4.append(12)
print(l3)
print(l4)


# In[29]:


print(id(l3),"\n",id(l4))


# In[30]:


# providing user input to the list

l5 = list(map(int,input().strip().split(" ")))
print(l5)


# In[31]:


# appending user defined input to the list 
n = int(input("Enter the number of elements to be appended to the list"))
l6 = []
for i in range(n):
    k = int(input())
    l6.append(k)
print(l6)


# In[32]:


help(l6.count)


# In[33]:


l6.count(4)


# In[34]:


l6.append(4)


# In[35]:


print(l6)


# In[36]:


l6.count(4)


# In[37]:


l6.count(4,1)


# In[38]:


print(l5)


# In[39]:


l6.extend(l5)


# In[40]:


print(l6)


# In[41]:


l6.count(4)


# In[42]:


l6.index(4)


# In[43]:


l6.index(4,1)


# In[44]:


l6.index(4,5)


# In[45]:


l6.index(4,6)


# In[46]:


help(l6.insert)


# In[47]:


dir(l6.insert)


# In[48]:


help('l6.insert')


# In[49]:


help('insert')


# In[50]:


l6.insert(0,15)
print(l6)


# In[51]:


help(l6.pop)


# In[52]:


l6.pop(0)
print(l6)


# In[53]:


help(l6.remove)


# In[54]:


l6.remove(4)


# In[55]:


print(l6)


# In[56]:


help(l6.reverse)


# In[57]:


l6.reverse()
print(l6)


# In[58]:


l6.sort()
print(l6)


# In[59]:


l6.sort(reverse = True)
print(l6)


# In[60]:


# Slicing in lists
l6[0]


# In[61]:


l6[1:5]


# In[62]:


l6[-1]


# In[63]:


l6[-1:-5]


# In[64]:


l6[-1:-5:1]


# In[65]:


l6[-1:-5:-1]


# In[66]:


l6[:]


# In[67]:


l6[::]


# In[68]:


l6[::-1]


# In[69]:


l6[1::-1]


# In[70]:


l6[:-1]


# In[71]:


print(l6)


# In[72]:


l6[:-1]


# In[73]:


l6[::-1]


# In[74]:


print(l6)


# In[75]:


l6[:-5:-1]


# In[76]:


print(l6)


# In[77]:


l6[:-5:1]


# In[78]:


list_1 = ["Apple","Banana","Mango","Orange",5.5,7//4,5+3j,{"A":1,"B":2,"C":3},{1,2,3,4,5},(7,8,9,10,11)]
print(list_1)


# In[79]:


type(list_1)


# In[80]:


list_1[0]


# In[81]:


list_1[6]


# In[82]:


list_1[7]


# In[83]:


list_1[7]["A"]


# In[84]:


list_1[7]["A"] = 1.1
print(list_1)


# In[85]:


list_1[8][1].append(1)


# In[86]:


list_1[8][1]


# In[87]:


list_1[8]


# In[88]:


for value in list_1[8]:
    print(value)


# In[89]:


list_1[9]


# In[90]:


list_1[9][1]


# In[91]:


list_1[8].add(1)


# In[92]:


print(list_1)


# In[93]:


print(type(list_1[8]))


# In[94]:


dir(list_1[9])


# In[95]:


for i in list_1[0]:
    print(i)


# In[96]:


print(l5)


# In[97]:


print(l6)


# In[98]:


print(l5+ l6)


# In[99]:


print(l5 * 3)


# In[100]:


print(l5 * l6)


# In[101]:


print(l5//2)


# In[102]:


print(l5/2)


# In[103]:


String = "Hello There! Welcome to python tutorials"
String_split = String.split(" ")
print(String_split)


# In[108]:


list_2 = [1,2,3,4,5]
list_3 = ["a","b","c","d","e"]
zipped = zip(list_2,list_3)


# In[109]:


result = list(zipped)


# In[110]:


print(result)


# In[111]:


list_4,list_5 = zip(*result)
print(list_4)
print(list_5)


# In[ ]:




