#!/usr/bin/env python
# coding: utf-8

# In[143]:


import string
import random
import time

#Record program time
start = time.time()

#Get user input for password requirements
def pass_info():
    global num_characters
    global numbers_added
    global symbols_added
    
    
    while True:
        num_characters = int(input("How many characters do you want your password to be ? (6 minimum)"))
        if num_characters < 6:
            print("Invalid password length, please try again.")
            continue
        else:            
            break
    
    while True:
        numbers_added = input("Do you want numbers added to your password? (y/n)").lower()
        if numbers_added in ["y", "n"]:
            break
        else:
            print("Invalid response, please try again.")
            continue
            
    while True:
        symbols_added = input("Do you want symbols added to your password? (y/n)").lower()
        if symbols_added in ["y", "n"]:
            break
        else:
            print("Invalid response, please try again.")
            continue
        
user_start_time = time.time()   
pass_info()  
user_finish_time = time.time()  

 #Calculate how long user took to input
user_total_time = user_finish_time - user_start_time                           


# In[144]:


#Password generator lists


lowercase = [lower for lower in string.ascii_lowercase]
uppercase = [upper for upper in string.ascii_uppercase]
numbers = [number for number in range(0,10)]


# In[149]:


#Adding symbols list
symbol_slice = []
for i in string.printable:
    if i in lowercase:
        pass
    elif i in uppercase:
        pass
    elif i in numbers:
        pass
    else:
        symbol_slice.append(i)
        
symbol_slice = symbol_slice[10:-5]
#checking list


# In[150]:


#Removing double character symbols
symbol_slice.remove("\\")


# Password generator ratio:
# - 1 special symbol every 6 characters
# - 1 number every 6 characters
# - 2 capital letters every 6 characters
# - the rest filled with lowercase

# In[151]:


#Making empty password string then finding ratio 
password = ""
ratio = num_characters // 6

#For every 6 characters 1 symbol, 1 number, 2 uppercase and the rest filled with lower
for i in range(ratio):
    if numbers_added == "y":
        password += str(random.choice(numbers))
    if symbols_added == "y":
        password += random.choice(symbol_slice)
    for j in range(2):
        password += random.choice(uppercase)
    
        
#Finding out how many lowercase letters to add   
lower_required = num_characters - len(password)
    


# In[152]:


#Filling in last characters with lowercase
for i in range(lower_required):
    password += random.choice(lowercase)


# In[153]:


#Turn into a list so can shuffle password so in random order
password_2 = [k for k in password]
random.shuffle(password_2)


# In[154]:


#Tuning random order back into a string and printing password
password = "".join(password_2)
print("Your random password is {}".format(password))

#Caclulate program time
finish_time = time.time()
total_time = (finish_time - start) - user_total_time
print("The total program time without user input was: {}".format(total_time))


# In[ ]:




