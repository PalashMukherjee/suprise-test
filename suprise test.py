#!/usr/bin/env python
# coding: utf-8

# In[21]:


def balance_parenthesis(expression): 
      
    open = ('({[')
    close = (')}]') 
    map = dict(zip(open, close)) 
    stack = [] 
    for i in expression: 
        if i in open: 
            stack.append(map[i]) 
        elif i in close: 
            pos = close.index(i) 
            if ((len(stack) > 0) and
                (open[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return len(expression)
    if stack == []: 
        return "success"
    else: 
        return len(expression)
string = "{[}"
print(balance_parenthesis(string))

