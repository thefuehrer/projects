#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


#Get user choice
def userInput():
    
    choice = int(input('1. Stone\n2. Paper\n3. Scissors\nEnter your choice '))
    return options[choice-1] 


# In[3]:


# return comp choice from options
def compChoice():
    return random.choice(options)


# In[4]:


#this chick draw
def checkDraw(comp_choice,user_choice):
    draw = False
    if user_choice == comp_choice:
        draw = True
    return draw


# In[5]:


#this check comp_win
def checkCompWin(comp_choice,user_choice):
    win = False
    if not checkDraw(comp_choice,user_choice):
        if comp_choice == 'Stone':
            if user_choice == 'Paper':
                win = False
            elif user_choice == 'Scissor':
                win = True
        elif comp_choice == 'Paper':
            if user_choice == 'Stone':
                win = True
            elif user_choice == 'Scissor':
                win = False
        elif comp_choice == 'Scissor':
            if user_choice == 'Stone':
                win = False
            elif user_choice == 'Paper':
                win = True
    return win


# In[6]:


#this check comp_win
def checkManWin(comp_choice,user_choice):
    win = False
    if not checkDraw(comp_choice,user_choice):
        if user_choice == 'Stone':
            if comp_choice == 'Paper':
                win = True
            elif comp_choice == 'Scissor':
                win = False
        elif user_choice == 'Paper':
            if comp_choice == 'Stone':
                win = True
            elif comp_choice == 'Scissor':
                win = False
        elif user_choice == 'Scissor':
            if comp_choice == 'Stone':
                win = True
            elif comp_choice == 'Paper':
                win = False
    return win


# In[12]:


options = ['Stone','Paper','Scissor']
comp_choice = compChoice()
user_choice = userInput()
if not checkDraw(comp_choice,user_choice):
    if checkCompWin(comp_choice,user_choice):
        print(f'Man chooses {user_choice} and Computer chooses {comp_choice} so computer Wins !!')
    elif checkManWin(comp_choice,user_choice):
        print(f'Man chooses {user_choice} and Computer chooses {comp_choice} so Man Wins !!')
else:
     print(f'Man chooses {user_choice} and Computer chooses {comp_choice} so it draw!!')      


# In[ ]:




