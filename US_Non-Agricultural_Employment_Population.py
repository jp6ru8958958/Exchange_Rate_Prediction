#美國非農就業人口
import requests
from bs4 import BeautifulSoup
url='https://stock-ai.com/eom-1-PAYEMS.php'
Response=requests.get(url)
Response.encoding='Utf-8'
#print(Response.status_code)
#print(Response.text)
soup=BeautifulSoup(Response.text,"html.parser")
#find=soup.select("div.pic2t.pic2t_bg a")