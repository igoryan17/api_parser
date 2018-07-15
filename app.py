import urllib.request
import ssl

import time
from selenium import webdriver

import links_parser

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
page = urllib.request.urlopen('https://10.101.72.106/docs/rest/', context=ctx)
links = links_parser.parse_links_to_api(page)
link = next(iter(links))

driver = webdriver.Chrome('C:\Tools\chromedriver.exe')
driver.get(link)
time.sleep(5)
section = driver.find_elements_by_xpath('//section/div')
print(section)
