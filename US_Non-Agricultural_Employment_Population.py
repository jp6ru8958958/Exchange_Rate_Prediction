#美國非農就業人口
import requests
from bs4 import BeautifulSoup
url='https://tradingeconomics.com/united-states/non-farm-payrolls'
Response=requests.get(url)
Response.encoding='Utf-8'
#print(url)
#print(Response.status_code)
#print(Response.text)
soup=BeautifulSoup(Response.text,"html.parser")
find=soup.select("td.datatable-item.datatable-item-positive")#數據

print("  Actual  Previous 	Consensus TEForecast ")
for row in range(7):
    print("--------------------------------------------")
    print_=row*4
    print("%7s  %7s   %7s    %7s"%(str.strip(find[print_].text),str.strip(find[print_+1].text),str.strip(find[print_+2].text),str.strip(find[print_+3].text)))

