import urllib.request
import ssl

import time
from selenium import webdriver

import links_parser

LOADING_WAIT_TIME = 7

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
page = urllib.request.urlopen('https://10.101.72.106/docs/rest/', context=ctx)
links = links_parser.parse_links_to_api(page)
link = next(iter(links))

driver = webdriver.Chrome('C:\Tools\chromedriver.exe')
driver.get(link)
time.sleep(LOADING_WAIT_TIME)
sections = links_parser.parse_sections(driver)
section = next(iter(sections))
article = links_parser.parse_article_name(section)
print(article)
print(links_parser.parse_query_type(article))
print(links_parser.parse_request_url(section))
print(links_parser.parse_request_body(section))
driver.close()
