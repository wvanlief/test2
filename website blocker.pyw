# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 16:50:10 2019

@author: Admin
"""
import time
from datetime import datetime as dt 

host_temp = "hosts"
hosts_path =r"C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1"
website_list =["www.facebook.com","facebook.com"]

while True: 
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working Hours")
        with open(host_temp,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect +" "+website+"\n")
    else:
        with open(host_temp,'r+') as file:
            content = file.readlines() # readlines put each line in a list, put but the pointer at the end of the file
            file.seek(0) # we put the point back on top of the file, so that we dont copy the file below itself but rewrite it
            for line in content: 
                if not any(website in line for website in website_list): # any returns true if there is any element of the website list in the line list 
                    file.write(line)
        print("Other Hours")
    time.sleep(5)

