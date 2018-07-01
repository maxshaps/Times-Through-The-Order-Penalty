import os
from sys import argv
from os.path import exists
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""
Repeatedly clicks a button on the Baseball-Reference website that downloads all data from a large query.
Input: numberWebpages = Number of webpages that script needs to iterate over.
"""


script, numberWebpages = argv

baseWebpage = "http://www.baseball-reference.com/play-index/event_finder.cgi?type=b#gotresults&year=2012&year_to=2012&divisory=%d&from=button&type=b&team_id=ANY&event=modPA&out_type=&criteria1=defensive_position---8---As_CF---def&criteria2=defensive_position---3---As_1B---def&criteria3=defensive_position---2---As_C---def&criteria4=defensive_position---7---As_LF---def&criteria5=defensive_position---4---As_2B---def&criteria6=defensive_position---6---As_SS---def&criteria7=defensive_position---9---As_RF---def&criteria8=defensive_position---5---As_3B---def&criteria9=defensive_position---10---As_DH---def&criteria10=inning---1---during_1st_Inning---inning&criteria11=inning---2---during_2nd_Inning---inning&criteria12=inning---3---during_3rd_Inning---inning&ajax=1&submitter=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1&z=1"

elementXPath = '//*[@id="outer_ajax_result_table_2012_%d"]/div[1]/div/span[5]' #%d gets incremented

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 60) #make sure number is in seconds
for index in range(0,int(numberWebpages)):
    currentWebpage = baseWebpage % (index + 1)
    driver.get(currentWebpage) #put the webpage here
    driver.get(currentWebpage)
    sleep(10)
    try:
        element = wait.until(EC.element_to_be_clickable((By.XPATH,elementXPath % index)))
        element.click()
    except:
        index -= 1
        continue
    sleep(5)
    while True:
        if os.path.isfile('*.csv.crdownload'):
            sleep(5)
        else:
            break
driver.close()
