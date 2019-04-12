#美國非農就業人口
import requests
from bs4 import BeautifulSoup
url='https://tradingeconomics.com/united-states/non-farm-payrolls'
Response=requests.get(url)
Response.encoding='Utf-8'
print(Response.status_code)
#print(Response.text)
soup=BeautifulSoup(Response.text,"html.parser")
find=soup.select("td.datatable-item.datatable-item-positive")

for blank_scan in range(len(find)):
    if find[blank_scan] == '''<td class="datatable-item datatable-item-positive" id="actual"></td>''':
        find[blank_scan].text = "None"

for row in range(7):
    print("---")
    print_=row*4
    print(str.strip(find[print_].text),str.strip(find[print_+1].text),str.strip(find[print_+2].text),str.strip(find[print_+3].text))
print("---")
