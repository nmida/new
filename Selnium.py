from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
##1+2
##a
s = Service("c:\chromedriver.exe")
chromdriver = webdriver.Chrome(service=s)
# chromdriver.get("http://www.walla.co.il")
# title = chromdriver.title
# chromdriver.refresh()
# title2 = chromdriver.title
# if title == title2:
#     print(f"Website {title2} is equal to {title}")
# else:
#     print(f"Website {title2} is not equal to {title}")
#
#
# ##b
f = Service("c:\geckodriver.exe")
firefoxdriver = webdriver.Firefox(service=f)
# firefoxdriver.get("http://www.ynet.co.il")
#
# ##3
#
# chromdriver.get("http://walla.co.il")
# one = "/html/body/div[2]/div/div[2]/header/div[1]/div/div[1]/form/input"
# firefoxdriver.get("https://walla.co.il")
# two = "/html/body/div[2]/div/div[2]/header/div[1]/div/div[1]/form/input"
# if one == two:
#     print("Same")
# else:
#     print("Not the same")
# ##4
#
# chromdriver.get("https://translate.google.co.il/?hl=iw")
# chromdriver.find_element(By.XPATH, '//*[@id="i8"]/span[3]').click()
# chromdriver.find_element(By.XPATH, '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea').send_keys("FullXpath")
# # chromdriver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea').send_keys("Xpath")
# # #chromdriver.find_element(By.ID, '"yDmH0d"').send_keys("ID")
#
#
# ##5
# youtube = webdriver.Chrome(service=s)
# youtube.get("https://youtube.com")
# youtube.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys("סלניום בכל הכוח")
# youtube.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/yt-icon-button/button/yt-icon").click()
#
# ##6
# chromdriver.get("https://translate.google.co.il/?hl=iw")
# chromdriver.find_element(By.XPATH, '//*[@id="i8"]/span[3]').click()
# chromdriver.find_element(By.XPATH, '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea').send_keys("FullXpath")
# chromdriver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea').send_keys("Xpath")
# chromdriver.find_element(By.ID, '"yDmH0d"').send_keys("ID")

##7
firefoxdriver.get("http://facebook.com")
firefoxdriver.find_element(By.XPATH, '//*[@id="email"]').send_keys("nmida18@gmail.com")
firefoxdriver.find_element(By.XPATH, '//*[@id="pass"]').send_keys("**********")
submit = firefoxdriver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
submit.click()

##8
chromdriver.get("https://one.co.il")
cookies = chromdriver.delete_cookie("name")
print(cookies)

##9
chromdriver.get("https://github.com/")
chromdriver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]').send_keys("Selenium", Keys.ENTER)

##10

options = webdriver.chrome.options.Options()
options.add_argument("--disable-extensions")




# s = Service("C:\chromedriver.exe")
# driver = webdriver.Chrome(service=s)
# driver.get('http://youtube.com')
# driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys("לך לישון")
# driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/yt-icon-button').click()
# f = Service("c:\geckodriver.exe")
# driver2 = webdriver.Firefox(service=f)
# driver2.get('https://youtube.com')
# search = driver2.find_element_by_xpath('//*[@id="search"]')
# search.send_keys("hello")


