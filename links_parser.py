from lxml import etree

query_types_map = {'create': 'POST', 'delete': 'DELETE', 'edit': 'PUT', 'get': 'GET'}


def parse_links_to_api(page):
    parser = etree.HTMLParser()
    tree = etree.fromstring(page.read(), parser)
    links = tree.xpath("//a[not(contains(@href, '#'))]/@href")
    result = []
    for link in links:
        result.append(page.url + link)
    return result


def parse_sections(driver):
    sections = driver.find_element_by_xpath("//section/div")
    return sections
