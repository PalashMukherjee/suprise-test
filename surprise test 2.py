#!/usr/bin/env python
# coding: utf-8

# In[1]:


# question 4
class stack:
    def __init__(self):
        self.item = []
    def push(self,element):
        self.item.append(element)
        m = 0
        if len(self.item) == 0:
            if m < element:
                m = element
                self.item.append(element)
        else:
            if element > m
            
    def pop(self):
        if len(self.item) > 0:
            self.item.pop()
        else:
            return "insert something"
    def get_stack(self):
        return self.item
    def max(self):
        
h = stack()


# In[2]:


h.push(1)


# In[4]:


h.push(7)


# In[5]:


h.push(8)


# In[7]:


h.push(5)


# In[8]:


h.push(4)


# In[10]:


h.get_stack()


# In[11]:


h.pop()


# In[12]:


h.get_stack()

