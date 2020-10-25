from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from htmldom import htmldom

PATH = 'D:\\PycharmPackages\\chromedriver.exe'

driver = webdriver.Chrome(PATH)

driver.get("https://www.sofascore.com/football/italy/2020-08-01")
time.sleep(5)
srch = driver.find_elements_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div/div/div[2]')
for x in srch:
    print(x.text)

#search.send_keys("Juventus")
#search.send_keys(Keys.RETURN)

#print(driver.page_source)


#driver.quit()


'''dom = htmldom.HtmlDom("https://www.sofascore.com/football/italy/2020-08-01").createDom()
# Find all the links present on a page and prints its "href" value
div = dom.find("div")
chldrn = div.children()
[print(ch.attr('href')) for ch in chldrn if ch.attr('href') != 'Undefined Attribute']
'''