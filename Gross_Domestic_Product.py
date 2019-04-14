#國內生產毛額(GDP)
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
driver.get("http://statdb.dgbas.gov.tw/pxweb/Dialog/varval.asp?ma=NA8101A1A&ti=%B0%EA%A5%C1%A9%D2%B1o%B2%CE%ADp%B1%60%A5%CE%B8%EA%AE%C6-%A6%7E&path=../PXfile/NationalIncome/&lang=9&strList=L")
driver.find_element_by_link_text(u"全選").click()
driver.find_element_by_xpath(
    u"(.//*[normalize-space(text()) and normalize-space(.)='搜尋 文件開始'])[1]/preceding::option[14]").click()
driver.find_element_by_xpath(
    u"(.//*[normalize-space(text()) and normalize-space(.)='搜尋 文件開始'])[1]/preceding::option[2]").click()
driver.find_element_by_name("sel").click()
html = driver.page_source
# print(html)

soup = BeautifulSoup(html,"html.parser")
gdp = soup.select("td", nowrap="")
print("Years          GDP")
for year in range(67):
    years=year*2
    print(" %s   %10s"%(str(gdp[years+6].text),str(gdp[years+7].text)))
    print("-----------------")


