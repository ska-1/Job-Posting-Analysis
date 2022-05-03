import selenium
from selenium import webdriver
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
import warnings
warnings.simplefilter('ignore')

#from selenium.webdriver.chrome.service import Service
#s=Service('./chromedriver.exe')
#driver = webdriver.Chrome(service=s)
driver= webdriver.Chrome("C:\projects\job posting\scraper\chromedriver.exe")


driver.maximize_window()
df = pd.DataFrame(columns=['Title','Company','Ratings','Experience','Salary','Location','Job_Post_History','Skills','Description'])

for q in range(1,251):
    driver.get("https://www.naukri.com/data-scientist-jobs-{}".format(q))
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source,'html5lib')
    results= soup.find(class_='list')
    job_elements= results.find_all('article',class_="jobTuple bgWhite br4 mb-8")
    for i, job_element in enumerate(job_elements):

        title= job_element.find('a',class_="title fw500 ellipsis").text
        company= job_element.find('a',class_="subTitle ellipsis fleft").text

        rating= job_element.find('span', class_='starRating fleft dot')
        if rating is None:
            pass
        else:
            ratings = rating.text

        try:
            exp_element= job_element.find('li',class_="fleft grey-text br2 placeHolderLi experience")
            exp= exp_element.find('span',class_='ellipsis fleft fs12 lh16')
            exp= exp.text
        except:
            exp = "NA"       
    
        sal_element = job_element.find('li',class_='fleft grey-text br2 placeHolderLi salary')
        sal = sal_element.find('span',class_='ellipsis fleft fs12 lh16')
        if sal is None:
            pass
        else:
            sal = sal.text
    
        loc_element = job_element.find('li',class_='fleft grey-text br2 placeHolderLi location')
        loc = loc_element.find('span',class_='ellipsis fleft fs12 lh16')
        if loc is None:
            pass
        else:
            loc = loc.text

        hist_element = job_element.find("div",["type br2 fleft grey","type br2 fleft green"])
        hist = hist_element.find('span',class_='fleft fw500')
        if hist is None:
            pass
        else:
            hist= hist.text

        ans=[]
        skill_element= job_element.find('ul', class_="tags has-description")
        skill=skill_element.find_all('li',class_="fleft fs12 grey-text lh16 dot")
        for s in skill:
            if s is None:
                pass
            else:
                ans.append(s.text)

        desc= job_element.find('div', class_="job-description fs12 grey-text")
        #desc=desc_element.find('i',class_="fleft icon-16 lh16 mr-4 naukicon naukicon-desc")
        try:
            desc = desc.text
        except:
            desc = "NA"       
        
        df=df.append({'Title':title,'Company':company,'Ratings':ratings,'Experience':exp,'Salary':sal,'Location':loc,'Job_Post_History':hist,'Skills':ans, "Description":desc},ignore_index = True)

        print(len(df))

#print(df)
df.to_csv("C:/projects/job posting/scraper/Naukri.com_datascraped.csv",index=False)
driver.close()
time.sleep(2)