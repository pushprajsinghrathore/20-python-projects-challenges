#!/usr/bin/env python
# coding: utf-8

# You will learn how to create an Instagram bot. You can make a bot to perform various operations with the help of Instagram automation with Python.
You can get these things from python Instagram API:
Follow an Instagram account
Upload photo from a bot Instagram account
Unfollow an Instagram account
Send direct messages on Instagram
Total information about followers and following of Instagram accounts

You have to select the file directory to upload photos and write the channel username for following using the Instagram automation tool-free. You can check the followers with the help of Instagram automation with a bot in Python.
# Instabot is a Python module, which not only implements the wrapper over the Instagram API, but also various useful methods, such as login to an Instagram account, getting users from the data, getting media from users or from hashtags, comments, likes, follows, and uploading photos.

# In[2]:


from instabot import Bot 


# In[ ]:


bot=Bot()
bot.login(username="username",password="password")
# this line of code use for login on insta gram
bot.follow("kamya_.kharya_") # this line of code follow the follower


# In[ ]:


# to uplod image
bot.uplod_photo("path image",captaion="")


# In[ ]:


# to unfollow 
bot.unfollow("type username to unfollow")


# In[ ]:


# to msg multipal person 
bot.send_message("hi how are you",["username1","username2"])


# In[ ]:


# find how many followers 
followers= bot.get_user_follower("pushprajsinghrathore_offical")
for follower in followers:
    print(bot.get_user_info(follower))


# In[ ]:




