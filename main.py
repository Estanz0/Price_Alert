from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#in the string/Quotation marks enter the path to where you downloaded the chromedriver.
browser = webdriver.Chrome("chromedriver")

#navigates you to the facebook page.
browser.get('https://www.facebook.com/')

#find the username field and enter the email example@yahoo.com.
username = browser.find_elements_by_css_selector("input[name=email]")
username[0].send_keys('example@yahoo.com')

#find the password field and enter the password password.
password = browser.find_elements_by_css_selector("input[name=pass]")
password[0].send_keys('password')

#find the login button and click it.
loginButton = browser.find_elements_by_css_selector("input[type=submit]")
loginButton[0].click()