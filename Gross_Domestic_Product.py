#國內生產毛額(GDP)
import requests
from bs4 import BeautifulSoup
url=''
Response=requests.get(url)
Response.encoding='Utf-8'
#print(Response.status_code)
#print(Response.text)
soup=BeautifulSoup(Response.text,"html.parser")
#find=soup.select("")