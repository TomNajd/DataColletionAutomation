from requests_html import HTMLSession
from datetime import datetime
import pandas as pd

ls1 = []
ls2 = []
ls3 = []
ls4 = []
ls5 = []
ls6 = []

now = datetime.now()
date_time_str = now.strftime("%d-%m-%y")

#greenslopes

session = HTMLSession()

url = 'https://petrolspy.com.au/map/station/5212f92f0364bb212f028e6a'

r = session.get(url)

r.html.render(sleep=2, keep_page=True, reload=True, wait=True)

prices = r.html.find('#infobox')

for item in prices:
    prices = {
      'title' : item.text
    }

    ls1.append(prices)
    mystring=' '.join(map(str,ls1))
    x = mystring.split()
    x1 = (x[1:17])
convback1=' '.join(map(str, x1))
print(convback1)     

#eight mile planes

session = HTMLSession()

url = 'https://petrolspy.com.au/map/station/609a2656b9914210ca607665'

r = session.get(url)

r.html.render(sleep=2, keep_page=True, reload=True, wait=True)

prices = r.html.find('#infobox')

for item in prices:
    prices = {
      'title' : item.text
    }

    ls2.append(prices)
    mystring=' '.join(map(str,ls2))
    x = mystring.split()
    x1 = (x[1:18])
convback2=' '.join(map(str, x1))
print(convback2)

#east brisbane

session = HTMLSession()

url = 'https://petrolspy.com.au/map/station/5212f92f0364bb212f028e65'

r = session.get(url)

r.html.render(sleep=2, keep_page=True, reload=True, wait=True)

prices = r.html.find('#infobox')

for item in prices:
    prices = {
      'title' : item.text
    }

    ls3.append(prices)
    mystring=' '.join(map(str,ls3))
    x = mystring.split()
    x1 = (x[1:17])
convback3=' '.join(map(str, x1))
print(convback3)  
    

#Mount gravatt east

session = HTMLSession()

url = 'https://petrolspy.com.au/map/station/5212f92f0364bb212f028e6c'

r = session.get(url)

r.html.render(sleep=2, keep_page=True, reload=True, wait=True)

prices = r.html.find('#infobox')

for item in prices:
    prices = {
      'title' : item.text
    }

    ls4.append(prices)
    mystring=' '.join(map(str,ls4))
    x = mystring.split()
    x1 = (x[1:20])
convback4=' '.join(map(str, x1))
print(convback4)  

#Carina

session = HTMLSession()

url = 'https://petrolspy.com.au/map/station/5212f92f0364bb212f028e3c'

r = session.get(url)

r.html.render(sleep=2, keep_page=True, reload=True, wait=True)

prices = r.html.find('#infobox')

for item in prices:
    prices = {
      'title' : item.text
    }

    ls5.append(prices)
    mystring=' '.join(map(str,ls5))
    x = mystring.split()
    x1 = (x[1:17])
convback5=' '.join(map(str, x1))
print(convback5)  

#acacia ridge

session = HTMLSession()

url = 'https://petrolspy.com.au/map/station/5848c7afe4b02b1af00ce722'

r = session.get(url)

r.html.render(sleep=2, keep_page=True, reload=True, wait=True)

prices = r.html.find('#infobox')

for item in prices:
    prices = {
      'title' : item.text
    }

    ls6.append(prices)
    mystring=' '.join(map(str,ls6))
    x = mystring.split()
    x1 = (x[1:17])
convback6=' '.join(map(str, x1))
print(convback6)   

print(date_time_str)  

df = pd.DataFrame({'greenslops':convback1,'eight-mile-planes':convback2,'east brisbane':convback3,'Mount-gravatt-east':convback4,'Carina':convback5,'acacia ridge':convback6, 'Date': date_time_str}, index =[0])

df.to_csv('data10-08-2022.csv', index=False, encoding='utf-8')