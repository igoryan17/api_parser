from lxml import etree

query_types_map = {'POST': 'create', 'DELETE': 'delete', 'PUT': 'edit', 'GET': 'get'}


def parse_links_to_api(page):
    parser = etree.HTMLParser()
    tree = etree.fromstring(page.read(), parser)
    links = tree.xpath("//a[not(contains(@href, '#'))]/@href")
    result = []
    for link in links:
        result.append(page.url + link)
    return result


def parse_sections(driver):
    sections = driver.find_elements_by_xpath("//section/div")
    return sections


def parse_article_name(section):
    article = section.find_element_by_xpath('article/div/h1')
    return article.text


def parse_query_type(article):
    for query, text in query_types_map.items():
        if text in article.lower():
            return query


def parse_request_url(section):
    result = ''
    for line in section.find_elements_by_xpath('article/pre/code/span'):
        result.join(line.text)
    return result


def parse_request_body(section):
    result = ''
    for line in section.find_elements_by_xpath('article/div/div/pre/code/span'):
        result.join(line.text)
    return result


def parse_page_tittle(driver):
    return driver.find_element_by_id("sections").find_element_by_xpath('./section/h1').text
