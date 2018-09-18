# encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')

# 宽400 高800
browser.set_window_size(400, 800)

elem = browser.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]')
ActionChains(browser).click(elem).perform()

WebDriverWait(browser, 1)

login_elem = browser.find_element_by_xpath('//*[@id="J_QRCodeLogin"]/div[5]/a[1]')
ActionChains(browser).click(login_elem).perform()

WebDriverWait(browser, 1)

# //*[@id="J_Form"]/div[2]/span
username_elem = browser.find_element_by_xpath('//*[@id="TPL_username_1"]')
username_elem.send_keys('15638223226')

WebDriverWait(browser, 4)

while True:
    pwd_elem = browser.find_element_by_xpath('//*[@id="TPL_password_1"]')
    pwd_elem.send_keys('tengtaobao')

    browser.implicitly_wait(2)

    sliding_elem = browser.find_element_by_xpath('//*[@id="nc_1_n1z"]')
    ActionChains(browser).drag_and_drop_by_offset(sliding_elem, 260, 0).perform()

    browser.implicitly_wait(2)

    affirm_elem = browser.find_element_by_xpath('//*[@id="J_SubmitStatic"]')
    ActionChains(browser).click(affirm_elem).perform()

    browser.implicitly_wait(2)
