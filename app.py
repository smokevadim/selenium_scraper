from selenium import webdriver
from os import path

CHROME_DRIVER = path.join(path.dirname(path.realpath(__file__)), "chromedriver.exe") # windows driver

base_link = "https://s3.amazonaws.com/outagemap.peco.com/external/default.html?initialWidth=882&childId=ctl00_ctl89_g_a940e154_03a4_4900_86a7_37d65bca5cad_ctl00_iFrameDiv&parentUrl=https%3A%2F%2Fwww.peco.com%2FOutages%2FCheckOutageStatus%2FPages%2FOutageMap.aspx"

options = webdriver.ChromeOptions()
# headless mode (without window)
options.add_argument('headless')
driver = webdriver.Chrome(CHROME_DRIVER, options=options)

driver.get(base_link)
driver.find_element_by_id('summary-icon').click()
driver.find_element_by_id('view-summary-county-muni').click()
table = driver.find_element_by_id('report-panel-county-muni-table')

print(table)