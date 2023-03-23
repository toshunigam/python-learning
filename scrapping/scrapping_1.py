import requests
from bs4 import BeautifulSoup
 
# Making a GET request
r = requests.get('https://gventure.net/careers')
 
# check status code for response received
# success code - 200
print(r)

# print content of request
# print(r.content)
# print(r.status_code)

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())
for link in soup.find_all('a'):
    print(link.get('href'))
print('hi there')
# Getting the title tag
# print(soup.title)
# print(soup.title.name)
# s = soup.find('div', class_='JobsCard')
# print(s)
# content = s.find_all('h1')
 
# for line in content:
    # print(line.text)