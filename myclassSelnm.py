from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\Pandas\chromedriver.exe")

driver.get("https://myclass.lpu.in")

user_le=driver.find_element_by_name("i")

print(user_le.is_displayed())       #eturns true or false depending on status
print(user_le.is_enabled())

pwd_le=driver.find_element_by_name("p")

print(pwd_le.is_displayed())   #returns true or false depending on status
print(pwd_le.is_enabled())

user_le.send_keys("11602882")
pwd_le.send_keys("Jack@786")

driver.find_element_by_xpath("/html/body/div[2]/div/form/div[7]/button").click()

driver.find_element_by_xpath("//a[contains(text(),'View Classes/Meetings')]").click()
time.sleep(10)

driver.implicitly_wait(5)
try:
    join = driver.find_element_by_xpath("//a[@class='btn btn-primary btn-block btn-sm']")
    time.sleep(200)
    print("Class Started")


except:
    print("Class not started, try after some time")