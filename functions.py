from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import account


def Login():
    global username
    global password

    account.Account.username = input(
        "Please enter your twitter username: ")
    account.Account.password = input(
        "Please enter your twitter password: ")
    account.Account.LogIn = True

def Trends():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)

    browser.get("https://www.twitter.com/login")
    time.sleep(2)

    if account.Account.LogIn == True:
        login_area = browser.find_elements_by_class_name(
            "r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-1inuy60.r-utggzx.r-vmopo1.r-1w50u8q.r-1lrr6ok.r-1dz5y72.r-fdjqy7.r-13qz1uu")[
            0]
        login_area.send_keys(account.Account.username)
        password_area = browser.find_elements_by_class_name(
            "r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-1inuy60.r-utggzx.r-vmopo1.r-1w50u8q.r-1lrr6ok.r-1dz5y72.r-fdjqy7.r-13qz1uu")[
            1]
        password_area.send_keys(account.Account.password, Keys.RETURN)

        browser.get("https://twitter.com/explore")
        time.sleep(2)

        source = browser.page_source
        soup = BeautifulSoup(source, 'html.parser')
        table = soup.find_all("div", {"dir": "ltr"})

        for table in table:
            trends = table.find("span", {"class": "css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"})
            if trends == None:
                pass

            else:
                trends = trends.text
                if trends.startswith("@") == False:
                    print(trends)
        browser.close()

    else:
        print("You did not log in yet. So I am going to show general trends.\n")

        browser.get("https://twitter.com/explore")
        time.sleep(2)

        source = browser.page_source
        soup = BeautifulSoup(source, 'html.parser')
        table = soup.find_all("div", {"dir": "ltr"})

        for table in table:
            trends = table.find("span", {"class": "css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"})
            if trends == None:
                pass

            else:
                trends = trends.text
                if trends.startswith("@") == False:
                    print(trends)
        browser.close()

def SendTweet():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)

    browser.get("https://www.twitter.com/login")
    time.sleep(2)

    if account.Account.LogIn == True:
        login_area = browser.find_elements_by_class_name(
            "r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-1inuy60.r-utggzx.r-vmopo1.r-1w50u8q.r-1lrr6ok.r-1dz5y72.r-fdjqy7.r-13qz1uu")[
            0]
        login_area.send_keys(account.Account.username)
        password_area = browser.find_elements_by_class_name(
            "r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-1inuy60.r-utggzx.r-vmopo1.r-1w50u8q.r-1lrr6ok.r-1dz5y72.r-fdjqy7.r-13qz1uu")[
            1]
        password_area.send_keys(account.Account.password, Keys.RETURN)

        time.sleep(2)
        tweet = input("Write your tweet: ")
        tweet_area = browser.find_element_by_xpath('''//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div
                                                          /div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div
                                                          /div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div
                                                          /div/div/div''')
        tweet_area.send_keys(tweet)
        tweet_area.send_keys(Keys.COMMAND, Keys.ENTER)
        time.sleep(2)
        tweet_button = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]"
                                          "/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]")
        tweet_button.click()
        time.sleep(2)
    else:
        print("Please log in.")

    browser.close()