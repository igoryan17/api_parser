import json
import ssl
import time
import urllib.request

from selenium import webdriver
from multiprocessing.dummy import Pool as ThreadPool

import links_parser
import postman_collection_writer

LOADING_WAIT_TIME = 7

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
page = urllib.request.urlopen('https://10.101.72.106/docs/rest/', context=ctx)
pool = ThreadPool(4)


def parse_and_write(link):
    driver = webdriver.Chrome('C:\Tools\chromedriver.exe')
    driver.get(link)
    time.sleep(LOADING_WAIT_TIME)
    tittle = links_parser.parse_page_tittle(driver)
    print('parse link ', link, ' tittle ', tittle)
    collection = postman_collection_writer.create_main_body(tittle)
    for section in links_parser.parse_sections(driver):
        article = links_parser.parse_article_name(section)
        if not article:
            continue
        method = links_parser.parse_query_type(article)
        if not method:
            continue
        body = links_parser.parse_request_body(section)
        if body.lower() == 'na':
            body = ''
        api_url = links_parser.parse_request_url(section)
        if not api_url:
            continue
        item = postman_collection_writer.create_item(article, method, body, api_url)
        collection['item'].append(item)
    driver.close()
    with open('out/' + tittle.replace(' ', '_') + '.json', 'w') as outfile:
        json.dump(collection, outfile)


links = links_parser.parse_links_to_api(page)
pool.map(parse_and_write, links)
pool.close()
