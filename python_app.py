import requests
from bs4 import BeautifulSoup

url = "https://www.codewithtomi.com/"

r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

name  = soup.find_all('h2', {'class':'post-title'})

#print(name[1].get_text())

for t in name:
    print(t.get_text())