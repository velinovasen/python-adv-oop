from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


PATH = 'C:\\Users\\Asen\\Desktop\\chromedriver.exe'

driver = webdriver.Chrome(PATH)

driver.get("https://bet365.com/#/HO/")
print(driver.title)

search = driver.find_element_by_class_name("hm-ProductHeaderWide_Link hm-HeaderMenuItem hm-HeaderMenuItem_LinkSelected hm-HeaderMenuItem_LinkSelected-underscore ")
print(search)
#search.send_keys("Juventus")
#search.send_keys(Keys.RETURN)

print(driver.page_source)

#time.sleep(5)

#driver.quit()
