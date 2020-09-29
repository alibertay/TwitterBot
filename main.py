from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

username = input("Please enter your twitter username (if you do not want to log in, do not fill here): ")
password = input("Please enter your twitter password (if you do not want to log in, do not fill here): ")

options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)

browser.get("https://www.twitter.com/login")
time.sleep(2)

login_area = browser.find_elements_by_class_name("r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-1inuy60.r-utggzx.r-vmopo1.r-1w50u8q.r-1lrr6ok.r-1dz5y72.r-fdjqy7.r-13qz1uu")[0]
login_area.send_keys(username)
password_area = browser.find_elements_by_class_name("r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-1inuy60.r-utggzx.r-vmopo1.r-1w50u8q.r-1lrr6ok.r-1dz5y72.r-fdjqy7.r-13qz1uu")[1]
password_area.send_keys(password,Keys.RETURN)

browser.get("https://twitter.com/explore")
time.sleep(2)

source = browser.page_source
soup = BeautifulSoup(source, 'html.parser')
table = soup.find_all("div", {"dir":"ltr"})

for table in table:
    trends = table.find("span", {"class":"css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"})
    if trends == None:
        pass

    else:
        trends = trends.text
        if trends.startswith("@") == False:
            print(trends)
browser.close()