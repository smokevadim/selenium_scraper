from selenium import webdriver
from os import path
from selenium.webdriver.common.action_chains import ActionChains

current_dir = path.dirname(path.realpath(__file__))
CHROME_DRIVER = path.join(current_dir, "chromedriver.exe") # windows driver

base_link = "https://google.com"

options = webdriver.ChromeOptions()
# headless mode (without window)
options.add_argument('headless')
options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(CHROME_DRIVER, options=options)
try:
    driver.get(base_link)
    q = driver.find_element_by_name('q')
    actions = ActionChains(driver)
    actions.move_to_element(q).send_keys('"cats"').perform()
    lucky_button = driver.find_element_by_css_selector('[name=btnI]')
    actions.move_to_element(q).click(lucky_button).perform()
    driver.get_screenshot_as_file(path.join(current_dir, driver.current_url.split('/')[2]+'-'+driver.current_url.split('/')[3]+'.png'))
except:
    pass

driver.close()