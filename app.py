import json
import urllib.request
import ssl

import time
from selenium import webdriver

import links_parser
import postman_collection_writer

LOADING_WAIT_TIME = 7

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
page = urllib.request.urlopen('https://10.101.72.106/docs/rest/', context=ctx)
driver = webdriver.Chrome('C:\Tools\chromedriver.exe')

for link in links_parser.parse_links_to_api(page):
    driver.get(link)
    time.sleep(LOADING_WAIT_TIME)
    tittle = links_parser.parse_page_tittle(driver)
    collection = postman_collection_writer.create_main_body(tittle)
    for section in links_parser.parse_sections(driver):
        article = links_parser.parse_article_name(section)
        method = links_parser.parse_query_type(article)
        body = links_parser.parse_request_body(section)
        api_url = links_parser.parse_request_url(section)
        item = postman_collection_writer.create_item(article, method, body, api_url)
        collection['item'].append(item)
    with open('out/' + tittle.replace(' ', '_') + '.json', 'w') as outfile:
        json.dump(collection, outfile)

driver.close()
