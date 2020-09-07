#!/usr/bin/env python
# coding: utf-8

# # Sending Email using python

# In[3]:


import smtplib
import getpass
from email.mime.text import MIMEText


# In[13]:


def send_email():
    sender_address = 'marveric6835@gmail.com'
    password = getpass.getpass()
    subject = 'AI Mafia - Machine Learning'
    msg = '''Hello! How are you?
    I hope you are fine.
    Let's meet very soon.
    
    Thank You'''
    
    
    # Server initialisation
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_address,password)
    
    #Draft my message body
    msg = MIMEText(msg)
    msg['Subject'] = subject
    msg['From'] = sender_address
    msg['To'] = 'marveric3508@gmail.com'
    recipients = ['marveric3508@gmail.com','tharunsai.putta@gmail.com']
    
    server.sendmail(sender_addess,recipients,msg.as_string())


# In[ ]:





# In[ ]:




