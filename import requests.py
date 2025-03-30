import requests
from bs4 import BeautifulSoup
r=requests.get("http://127.0.0.1:5500/index.html")
soup=BeautifulSoup(r.content,'html.parser')
for i in soup.find_all("h1"):
    print(i.text)
    
    
    
    
    
    
    