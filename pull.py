from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time
import csv
from collections import defaultdict
import matplotlib.pyplot as plt

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
s = Service('/Users/franzgorlich/Documents/GitHub/chromedriver')
DRIVER_PATH = '/path/to/chromedriver'
driver = webdriver.Chrome(options=chrome_options,service=s)


df = pd.DataFrame(columns=['caseName', 'weaponType','rarity', 'weapon', 'name'])

url = "https://csgostash.com/case/"

time.sleep(4)

for i in range(1,400):
    print('-------------------------------- Page %s'%(i))
    driver.get(url+str(i))    
    try:
        caseName = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/h1').text
    except:
        continue
    print(caseName)

    sub = driver.find_elements(By.CLASS_NAME,"result-box")
    for s in sub:
        newRow = {'caseName':None, 'weaponType':None, 'rarity':None, 'weapon':None, 'name':None}
        try:
            rarity = s.find_element(By.CLASS_NAME,"quality")
            rar = rarity.find_element(By.CLASS_NAME,'nomargin').text
            rar = rar.split(' ')
            rarity = rar[0]
            if len(rar)>0:
                weaponType = rar[1]
            else:
                weaponType = 'Sticker'
            name = s.find_element(By.TAG_NAME,'h3')

            nlist = name.find_elements(By.TAG_NAME,'a')
            weaponName = ' '.join([n.text for n in nlist])

            #print(nlist,weaponName)
            newRow['caseName'] = caseName
            newRow['rarity'] = rarity
            newRow['weaponType'] = weaponType
            newRow['weapon'] = nlist[0].text
            if len(nlist)>1:
                newRow['name'] = nlist[1].text
            else:
                newRow['name'] = nlist[0].text

            df = df.append(newRow,ignore_index=True)
        except:
            print('--- NONE ---')
print(df)
time.sleep(2)
driver.close()
df.to_csv('out.csv',index=False)
quit()


for i in range(24,31):
    urls = []
    dates = []

    driver.get('https://leetcode.com/problemset/all/')
    time.sleep(4)
    c = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div/button[1]')
    for i in range(i):
        c.click()
        time.sleep(1)
    a = driver.find_element(By.CLASS_NAME, "grid-cols-7")
    childs = a.find_elements(By.CSS_SELECTOR,"*")

    for child in childs:
        if child.get_attribute('href')!=None:
            urls.append(child.get_attribute('href'))
            dates.append(child.get_attribute('data-value').split(' ')[:4])

    for i in range(len(urls)):
        url = urls[i]
        dayType = dates[i][0]
        month = dates[i][1]
        day = dates[i][2]
        year = dates[i][3]
        diff = getDifficulty(url)
        print('Difficulty %s on %s/%s/%s'%(diff,day,month,year))
        dic['diff'].append(diff)
        dic['day_type'].append(dayType)
        dic['day'].append(day)
        dic['year'].append(year)
        dic['month'].append(month)




