# -*- coding: utf-8 -*-
"""
Python script to bulk scrape websites for email addresses

Author: Jaya Kumar
 
"""

import urllib.request 
import re
import csv
import pandas as pd
import os



# 1: Get input file path from user 'C:/Users/jaya.kumar/Documents/upw/websites.csv'
user_input = input("Enter the path of your file: ")

if os.path.exists(user_input):
 
    # 2. read file
    df = pd.read_csv(user_input)
   
    # 3. create the output csv file
    with open('EmailID.csv', mode='w',newline='') as file:
                csv_writer = csv.writer(file, delimiter=',')
                csv_writer.writerow(['Website','EmailID'])
                
    # 4. Get websites
    for site in list(df['website']):
        print(site)
        req = urllib.request.Request(site, headers={'User-Agent' : "Magic Browser"}) 
        
        # 5. Scrape email id
        with urllib.request.urlopen(req) as url:
            s = url.read().decode('utf-8')
            email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s)
            print(email)
            # 6. Write the output
            with open('EmailID.csv', mode='a',newline='') as file:
                csv_writer = csv.writer(file, delimiter=',')
                [csv_writer.writerow([site,item]) for item in email]
                       
#If input file doesn't exist            
else:
    print("File not found, verify the location - ",str(user_input))
