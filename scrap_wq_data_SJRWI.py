# -*- coding: utf-8 -*-
"""
Created on Sat August 25, 2018

@author: gmallya
"""
# Broad preliminary Goal - This file should be able to fetch water quality data 
# from SJRWI website and save them as .csv or .txt files 
 
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os
#import numpy as np
#import matplotlib.pyplot as plt
#import random
###### USER INPUT- Provide the Tripadvisor URL #####
# url = 'http://wqis.ipfw.edu/nutrientView/?site=101&startDate=4/3/2002&endDate=9/26/2017'
# url = 'http://wqis.ipfw.edu/bacteriaView/?site=101&startDate=4/6/2004&endDate=10/29/2013'
# url = 'http://wqis.ipfw.edu/pesticideView/?site=101&startDate=4/6/2004&endDate=10/29/2013'
# url = 'http://wqis.ipfw.edu/wQMdataView/?site=101&startDate=4/6/2004&endDate=10/29/2013'
# concat integer to string: Suppose a = [1, 2, 3]. Then "abc" + `a[2]` will give abc3
######################
#stn_nums = range(100,107)
#stn_nums.extend(117)
#stn_nums.extend(121,136)
#stn_nums.extend(141,144)
#stn_nums.extend(145,148)
#stn_nums.extend(149,)

# First get a list all of stations in the system 
url = 'http://wqis.ipfw.edu/chartSelection/'
with open('stations.csv', 'w') as stations:
    # Read HTML content from the url provided by the user
    web_response = requests.get(url)
    
    # Process the content only if the web request was successful
    if web_response.ok:
        # Write the header line to stations.csv file
        stations.write("S.No.;Station Name\n")
        
        # Parse the HTML content using Beautiful Soup        
        soup  = BeautifulSoup(web_response.text,"lxml")
        
        # Read all station listings available in the form at the current url
        allstations = soup.findAll('form')
        
        # Loop through each station to extract relevant details such as station number and station name
        prices = []
        stn_nums = []
        stn_names = []
        for i in allstations:
            opt = i.findAll('option')
            ind = 0
            for j in opt:
                if ind > 0:
                    stn_nums.append(int(j['value']))
                    stn_names.append(j.text)
                    stations.write(j['value'] + ";" + j.text +'\n')
                ind = ind + 1
            
# Second step: read data for each station and store it in a csv file
    # url = 'http://wqis.ipfw.edu/nutrientView/?site=101&startDate=4/3/2002&endDate=9/26/2017'
    # url = 'http://wqis.ipfw.edu/bacteriaView/?site=101&startDate=4/6/2004&endDate=10/29/2013'
    # url = 'http://wqis.ipfw.edu/pesticideView/?site=101&startDate=4/6/2004&endDate=10/29/2013'
    # url = 'http://wqis.ipfw.edu/wQMdataView/?site=101&startDate=4/6/2004&endDate=10/29/2013'
st_dt = '1/1/2000'
end_dt = '12/31/2018'
wqclass = ['nutrientView','bacteriaView','pesticideView','wQMdataView']
driver = webdriver.Chrome('C:/Users/gmallya/Downloads/chromedriver')
time.sleep(10) # Waits for the webdriver to load and be available to execute driver.get(url) command

# We will collect data for each water quality class
for wqcl in range(len(wqclass)): #range(len(wqclass))
    # Query data for each station
    for s in range(len(stn_nums)): #range(len(stn_nums)):
        time.sleep(1) # helps prevent abuse of host website from where we are scraping data
        sn = stn_nums[s] # Get the station number
        print sn
        # There are few stations with no data, so do not query them. There was no 
        # neat way of excluding them, therefore we have hard-coded
        if sn not in range(170,176):
            # initialize data
            d_samplenum = []
            d_ecoli = []
            d_n = []
            d_tp = []
            d_drp = []
            d_al = []
            d_at = []
            d_me = []
            d_cond = []
            d_do = []
            d_pH = []
            d_WT = []
            d_TDS = []
            d_Turb = []
            # define url
            url = 'http://wqis.ipfw.edu/'+ wqclass[wqcl] + '/?site=' + `sn` + '&startDate=' + st_dt + '&endDate=' + end_dt
            driver.get(url)
            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')
            # Get data available on the first page
            tb = soup.find('tbody')
            itr = 0
            for tr in tb.findAll('tr'):
                if itr > 0: # skip html table headers
                    itd = 0
                    for td in tr.findAll('td'):
                        if wqcl == 0: # nutrients
                            if itd == 1: #Store Sample number  
                                d_samplenum.append(int(td.text))
                            if itd == 2: # Nitrate/Nitrite (mg/L)
                                if td.text.strip() == "None":
                                    d_n.append(-999)
                                else:
                                    d_n.append(float(td.text))
                            if itd == 3: # Total Phosphorus (mg/L) 
                                if td.text.strip() == "None":
                                    d_tp.append(-999)
                                else:
                                    d_tp.append(float(td.text))
                            if itd == 4: # Dissolved Reactive Phosphorus (mg/L)
                                if td.text.strip() == "None":
                                    d_drp.append(-999)
                                else:
                                    d_drp.append(float(td.text))   
                        if wqcl == 1: # Bacteria
                            if itd == 1: #Store Sample number  
                                d_samplenum.append(int(td.text))
                            if itd == 2: # E_coli
                                if td.text.strip() == "None":
                                    d_ecoli.append(-999)
                                else:
                                    d_ecoli.append(float(td.text))
                        if wqcl == 2: # pesticide
                            if itd == 1: #Store Sample number  
                                d_samplenum.append(int(td.text))
                            if itd == 2: # Alachlor (µg/L) 
                                if td.text.strip() == "None":
                                    d_al.append(-999)
                                else:
                                    d_al.append(float(td.text))
                            if itd == 3: # Atrazine (µg/L) 
                                if td.text.strip() == "None":
                                    d_at.append(-999)
                                else:
                                    d_at.append(float(td.text))
                            if itd == 4: # Metolachlor (µg/L)
                                if td.text.strip() == "None":
                                    d_me.append(-999)
                                else:
                                    d_me.append(float(td.text))
                        if wqcl == 3: # Physical properties
                            if itd == 2: #Store Sample number  (itd is incremented by 1, because there is a column for TIME)
                                d_samplenum.append(int(td.text))
                            if itd == 3: # Conductivity (mS/cm) 
                                if td.text.strip() == "None":
                                    d_cond.append(-999)
                                else:
                                    d_cond.append(float(td.text))
                            if itd == 4: # Dissolved Oxygen (mg/L) 
                                if td.text.strip() == "None":
                                    d_do.append(-999)
                                else:
                                    d_do.append(float(td.text))
                            if itd == 5: # pH 
                                if td.text.strip() == "None":
                                    d_pH.append(-999)
                                else:
                                    d_pH.append(float(td.text))
                            if itd == 6: # Water Temperature (°C) 
                                if td.text.strip() == "None":
                                    d_WT.append(-999)
                                else:
                                    d_WT.append(float(td.text))
                            if itd == 7: # Total Dissolved Solids (g/L) 
                                if td.text.strip() == "None":
                                    d_TDS.append(-999)
                                else:
                                    d_TDS.append(float(td.text))
                            if itd == 8: # Turbidity (NTU)
                                if td.text.strip() == "None":
                                    d_Turb.append(-999)
                                else:
                                    d_Turb.append(float(td.text))
                        itd = itd + 1
                itr = itr + 1
            # Get a list of pagination links
            all_a = soup.find('span',{"id":'pagelist'})
            for a in all_a.findAll('a'):
                time.sleep(0.5)
                 # update url
                url = 'http://wqis.ipfw.edu/'+ wqclass[wqcl] + '/' + a['href']
                driver.get(url)
                html = driver.page_source
                soup = BeautifulSoup(html, 'lxml')
                # Get data available on the first page
                tb = soup.find('tbody')
                itr = 0
                for tr in tb.findAll('tr'):
                    if itr > 0: # skip html table headers
                        itd = 0
                        for td in tr.findAll('td'):
                            if wqcl == 0: # nutrients
                                if itd == 1: #Store Sample number  
                                    d_samplenum.append(int(td.text))
                                if itd == 2: # Nitrate/Nitrite (mg/L)
                                    if td.text.strip() == "None":
                                        d_n.append(-999)
                                    else:
                                        d_n.append(float(td.text))
                                if itd == 3: # Total Phosphorus (mg/L) 
                                    if td.text.strip() == "None":
                                        d_tp.append(-999)
                                    else:
                                        d_tp.append(float(td.text))
                                if itd == 4: # Dissolved Reactive Phosphorus (mg/L)
                                    if td.text.strip() == "None":
                                        d_drp.append(-999)
                                    else:
                                        d_drp.append(float(td.text))   
                            if wqcl == 1: # Bacteria
                                if itd == 1: #Store Sample number  
                                    d_samplenum.append(int(td.text))
                                if itd == 2: # E_coli
                                    if td.text.strip() == "None":
                                        d_ecoli.append(-999)
                                    else:
                                        d_ecoli.append(float(td.text))
                            if wqcl == 2: # pesticide
                                if itd == 1: #Store Sample number  
                                    d_samplenum.append(int(td.text))
                                if itd == 2: # Alachlor (µg/L) 
                                    if td.text.strip() == "None":
                                        d_al.append(-999)
                                    else:
                                        d_al.append(float(td.text))
                                if itd == 3: # Atrazine (µg/L) 
                                    if td.text.strip() == "None":
                                        d_at.append(-999)
                                    else:
                                        d_at.append(float(td.text))
                                if itd == 4: # Metolachlor (µg/L)
                                    if td.text.strip() == "None":
                                        d_me.append(-999)
                                    else:
                                        d_me.append(float(td.text))
                            if wqcl == 3: # Physical properties
                                if itd == 2: #Store Sample number  (itd is incremented by 1, because there is a column for TIME)
                                    d_samplenum.append(int(td.text))
                                if itd == 3: # Conductivity (mS/cm) 
                                    if td.text.strip() == "None":
                                        d_cond.append(-999)
                                    else:
                                        d_cond.append(float(td.text))
                                if itd == 4: # Dissolved Oxygen (mg/L) 
                                    if td.text.strip() == "None":
                                        d_do.append(-999)
                                    else:
                                        d_do.append(float(td.text))
                                if itd == 5: # pH 
                                    if td.text.strip() == "None":
                                        d_pH.append(-999)
                                    else:
                                        d_pH.append(float(td.text))
                                if itd == 6: # Water Temperature (°C) 
                                    if td.text.strip() == "None":
                                        d_WT.append(-999)
                                    else:
                                        d_WT.append(float(td.text))
                                if itd == 7: # Total Dissolved Solids (g/L) 
                                    if td.text.strip() == "None":
                                        d_TDS.append(-999)
                                    else:
                                        d_TDS.append(float(td.text))
                                if itd == 8: # Turbidity (NTU)
                                    if td.text.strip() == "None":
                                        d_Turb.append(-999)
                                    else:
                                        d_Turb.append(float(td.text))
                            itd = itd + 1
                    itr = itr + 1
            # Save data to text/csv file
            print '\n\tWriting results\n'
            dirpath = 'C:\\OfficeWorkspace\\SJRWI_scraping\\' + `sn`
            if not os.path.exists(dirpath):
                os.mkdir(dirpath)
            os.chdir(dirpath)        
            if wqcl == 0: # Nutrients
                with open('nutrients.csv','w') as data_file:
                    for isam in range(len(d_samplenum)):
                        data_file.write(str(d_samplenum[isam]) + ";" + str(d_n[isam]) + ";" + str(d_tp[isam]) + ";" + str(d_drp[isam]) +'\n')
            elif wqcl == 1: # Bacteria
                with open('bacteria.csv','w') as data_file:
                    for isam in range(len(d_samplenum)):
                        data_file.write(str(d_samplenum[isam]) + ";" + str(d_ecoli[isam]) +'\n')
            elif wqcl == 2: # Pesticide
                with open('pesticides.csv','w') as data_file:
                    for isam in range(len(d_samplenum)):
                        data_file.write(str(d_samplenum[isam]) + ";" + str(d_al[isam]) + ";" + str(d_at[isam]) + ";" + str(d_me[isam]) +'\n')
            else: # Physical properties
                with open('physical_properties.csv','w') as data_file:
                    for isam in range(len(d_samplenum)):
                        data_file.write(str(d_samplenum[isam]) + ";" + str(d_cond[isam]) + ";" + str(d_do[isam]) + ";" + str(d_pH[isam]) + ";" + str(d_WT[isam]) + ";" + str(d_TDS[isam]) + ";" + str(d_Turb[isam]) +'\n')
