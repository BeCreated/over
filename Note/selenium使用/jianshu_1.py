# encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url = 'https://www.jianshu.com/sign_in'

browser = webdriver.Chrome()
browser.get(url)

from selenium.webdriver.common.action_chains import ActionChains

WebDriverWait(browser, 3)

username_elem = browser.find_element_by_xpath('//*[@id="session_email_or_mobile_number"]')
username_elem.send_keys('15638223226')

WebDriverWait(browser, 1)

pwd_elem = browser.find_element_by_xpath('//*[@id="session_password"]')
pwd_elem.send_keys('teng1995')

WebDriverWait(browser, 2)

affirm_elem = browser.find_element_by_xpath('//*[@id="sign-in-form-submit-btn"]')
ActionChains(browser).click(affirm_elem).perform()

# 换图
# WebDriverWait(browser, 3)
# next_elem = browser.find_element_by_xpath("/html/div[3]/div[2]/div[6]/div/div/div[3]/div/a[2]")
# ActionChains(browser).click(next_elem).perform()
# next_elem = browser.find_element_by_xpath("/html/div[3]/div[2]/div[6]/div/div/div[2]/div[1]/div/div[2]/img/@href")
# print(next_elem)





