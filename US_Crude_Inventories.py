#美國原油庫存量
import requests
from bs4 import BeautifulSoup
url='https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=MCRSCUS1&f=M'
Response = requests.get(url)
Response.encoding='Utf-8'
# print(Response.status_code)
# print(Response.text)
soup = BeautifulSoup(Response.text,"html.parser")
Month = soup.find_all('th',class_="G")
Years = soup.find_all('td',class_="B4")
Cosc = soup.find_all('td',class_="B3")
for print_month in Month:
    print("       %3s"%(print_month.text),end="")
print("")
for year in range(len(Years)):
    print(str.strip(Years[year].text),end="  ")
    for print_ in range(12):
        print_ += 12 * year
        print("%8s"%(str.strip(Cosc[print_].text)),end="  ")
    print("")


