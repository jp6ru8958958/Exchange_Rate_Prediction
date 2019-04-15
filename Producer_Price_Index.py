# 生產者物價指數
from selenium import webdriver
from bs4 import BeautifulSoup
url = 'http://statdb.dgbas.gov.tw/pxweb/Dialog/varval.asp?ma=PR0101A1M&ti=%AE%F8%B6O%AA%CC%AA%AB%BB%F9%B0%F2%A5%BB%A4%C0%C3%FE%AB%FC%BC%C6-%A4%EB&path=../PXfile/PriceStatistics/&lang=9&strList=L'
driver = webdriver.Firefox()
driver.get(url)
driver.find_element_by_link_text(u"全選").click()
driver.find_element_by_xpath(
    u"(.//*[normalize-space(text()) and normalize-space(.)='搜尋 文件開始'])[1]/preceding::option[83]").click()
driver.find_element_by_xpath(
    u"(.//*[normalize-space(text()) and normalize-space(.)='搜尋 文件開始'])[1]/preceding::option[2]").click()
driver.find_element_by_name("sel").click()
html = driver.page_source
# print(html)

soup = BeautifulSoup(html, "html.parser")
PPI = soup.select("td", nowrap="")
print("", end="          ")
for print_M in range(12):
    print("M%2d"%(print_M+1), end="      ")
print("")
for print_ in range(39):
    move = print_ * 24 + 5
    print(1981+print_, end="  ")
    for print_PPI in range(12):
        print("%7s"%(PPI[move+print_PPI*2].text), end="  ")
    print("")
