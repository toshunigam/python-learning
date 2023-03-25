import requests
from bs4 import BeautifulSoup
 
# Making a GET request
r = requests.get('https://ayanshtechnology.com/contact.html')
 
# check status code for response received
# success code - 200
print(r)

# print content of request
# print(r.status_code)

soup = BeautifulSoup(r.content, 'html.parser')
# for link in soup.find_all('a'):
    # print(link.get('href'))

# Getting the title tag
# print(soup.title)
# print(soup.title.name)

s = soup.find('div', class_="vp__address__container")

content = s.find_all('p')
 
for line in content:
    print(line.text)