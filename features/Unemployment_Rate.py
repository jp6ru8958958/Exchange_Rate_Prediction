#失業率
from selenium import webdriver
from bs4 import BeautifulSoup
url="http://statdb.dgbas.gov.tw/pxweb/Dialog/varval.asp?ma=LM0107A1M&ti=%A4H%A4O%B8%EA%B7%BD%A5D%ADn%AB%FC%BC%D0-%A4%EB&path=../PXfile/LaborForce/&lang=9&strList=L"
driver = webdriver.Firefox()
driver.get(url)
driver.find_element_by_link_text(u"全選").click()
driver.find_element_by_xpath(
    u"(.//*[normalize-space(text()) and normalize-space(.)='搜尋 文件開始'])[1]/preceding::option[4]").click()
driver.find_element_by_xpath(
    u"(.//*[normalize-space(text()) and normalize-space(.)='搜尋 文件開始'])[1]/preceding::option[3]").click()
driver.find_element_by_xpath(
    u"(.//*[normalize-space(text()) and normalize-space(.)='不全選'])[4]/following::option[1]").click()
driver.find_element_by_name("sel").click()
html = driver.page_source

soup = BeautifulSoup(html, "html.parser")
UR = soup.select("td",nowrap="")
print("", end="          ")
for print_M in range(12):
    print("M%2d"%(print_M+1), end="      ")
print("")
for print_ in range(45):
    move = print_ * 24 + 5
    print(1978+print_, end="  ")
    for print_UR in range(12):
        print("%7s"%(UR[move+print_UR*2].text), end="  ")
    print("")
