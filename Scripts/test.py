import os
from sys import argv
from os.path import exists
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


webpageOne = "http://www.google.com"
webpageTwo = "http://fivethirtyeight.com"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get(webpageOne)
sleep(10)
driver.get(webpageTwo)
sleep(10)
driver.close()
