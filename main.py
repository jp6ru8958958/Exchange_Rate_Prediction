import requests
from bs4 import BeautifulSoup
from selenium import webdriver

class Crawler():

    def __init__(self,select_feature):
        self.feature = select_feature
        if (select_feature == "1"):
            self.URL = "http://statdb.dgbas.gov.tw/pxweb/Dialog/varval.asp?ma=PR0101A1M&ti=%AE%F8%B6O%AA%CC%AA%AB%BB%F9%B0%F2%A5%BB%A4%C0%C3%FE%AB%FC%BC%C6-%A4%EB&path=../PXfile/PriceStatistics/&lang=9&strList=L"
        elif (select_feature == "2"):
            self.URL = "http://statdb.dgbas.gov.tw/pxweb/Dialog/varval.asp?ma=NA8101A1A&ti=%B0%EA%A5%C1%A9%D2%B1o%B2%CE%ADp%B1%60%A5%CE%B8%EA%AE%C6-%A6%7E&path=../PXfile/NationalIncome/&lang=9&strList=L"
        elif (select_feature == "3"):
            self.URL = "http://statdb.dgbas.gov.tw/pxweb/Dialog/varval.asp?ma=LM0107A1M&ti=%A4H%A4O%B8%EA%B7%BD%A5D%ADn%AB%FC%BC%D0-%A4%EB&path=../PXfile/LaborForce/&lang=9&strList=L"
        elif (select_feature == "4"):
            self.URL = "https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=MCRSCUS1&f=M"
        elif (select_feature == "5"):
            self.URL = "https://tradingeconomics.com/united-states/non-farm-payrolls"

    def Consumer_Prise_Index(self):
        driver = webdriver.Firefox()
        driver.get(self.URL)
        driver.find_element_by_link_text(u"全選").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='搜尋 文件開始'])[1]/preceding::option[83]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='搜尋 文件開始'])[1]/preceding::option[2]").click()
        driver.find_element_by_name("sel").click()
        html = driver.page_source
        # print(html)
        soup = BeautifulSoup(html, "html.parser")
        CPI = soup.select("td", nowrap="")
        print("", end="          ")
        month = 12
        for print_M in range(12):
            print("M%2d" % (print_M + 1), end="      ")
        print("")
        for print_ in range(39):
            move = print_ * 24 + 5
            if((1981+print_) >= 2019):
                month = 4
                if((1981+print_)==2020):
                    break
            print(1981 + print_, end="  ")
            for print_CPI in range(month):
                print("%7s" % (CPI[move + print_CPI * 2].text), end="  ")
            print("")

    def Gross_Domestic_Product(self):
        driver = webdriver.Firefox()
        driver.get(self.URL)
        driver.find_element_by_link_text(u"全選").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='搜尋 文件開始'])[1]/preceding::option[14]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='搜尋 文件開始'])[1]/preceding::option[2]").click()
        driver.find_element_by_name("sel").click()
        html = driver.page_source
        # print(html)
        soup = BeautifulSoup(html, "html.parser")
        gdp = soup.select("td", nowrap="")
        print("Years          GDP")
        for year in range(67):
            years = year * 2
            print(" %s   %10s" % (str(gdp[years + 6].text), str(gdp[years + 7].text)))
            print("-----------------")

    def Unemployment_Rate(self):
        driver = webdriver.Firefox()
        driver.get(self.URL)
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
        UR = soup.select("td", nowrap="")
        print("", end="          ")
        month = 12
        for print_M in range(12):
            print("M%2d" % (print_M + 1), end="      ")
        print("")
        for print_ in range(45):
            move = print_ * 24 + 5
            if((1978+print_) >= 2019):
                month = 2
                if((1978+print_)==2020):
                    break
            print(1978 + print_, end="  ")

            for print_UR in range(month):
                print("%7s" % (UR[move + print_UR * 2].text), end="  ")
            print("")

    def US_Crude_Inventories(self):
        Response = requests.get(self.URL)
        Response.encoding = 'Utf-8'
        # print(Response.status_code)
        # print(Response.text)
        soup = BeautifulSoup(Response.text, "html.parser")
        Month = soup.find_all('th', class_="G")
        Years = soup.find_all('td', class_="B4")
        Cosc = soup.find_all('td', class_="B3")
        for print_month in Month:
            print("       %3s" % (print_month.text), end="")
        print("")
        for year in range(len(Years)):
            print(str.strip(Years[year].text), end="  ")
            for print_ in range(12):
                print_ += 12 * year
                print("%8s" % (str.strip(Cosc[print_].text)), end="  ")
            print("")

    def US_Non_Agricultural_Employment_Population(self):
        Response = requests.get(self.URL)
        Response.encoding = 'Utf-8'
        # print(url)
        # print(Response.status_code)
        # print(Response.text)
        soup = BeautifulSoup(Response.text, "html.parser")
        find = soup.select("td.datatable-item.datatable-item-positive")  # 數據
        print(" month     Actual  Previous  Consensus TEForecast ")
        for row in range(7):
            print("-------------------------------------------------")
            print_ = row * 4
            print("2019 -", row + 1, "%7s  %7s   %7s    %7s" % (
            str.strip(find[print_].text), str.strip(find[print_ + 1].text), str.strip(find[print_ + 2].text),
            str.strip(find[print_ + 3].text)))

while(1):
    User_in = input("1.消費者物價指數\n2.國內生產毛額(GDP)\n3.失業率\n4.美國原油庫存量\n5.美國非農就業人口\n")
    Search = Crawler(User_in)
    if(User_in == "1"):
        Search.Consumer_Prise_Index()
    elif(User_in == "2"):
        Search.Gross_Domestic_Product()
    elif (User_in == "3"):
        Search.Unemployment_Rate()
    elif (User_in == "4"):
        Search.US_Crude_Inventories()
    elif (User_in == "5"):
        Search.US_Non_Agricultural_Employment_Population()
    else:
        break
print("end")

