from lxml import etree


def parse_links_to_api(page):
    parser = etree.HTMLParser()
    tree = etree.fromstring(page.read(), parser)
    links = tree.xpath("//a[not(contains(@href, '#'))]/@href")
    result = []
    for link in links:
        result.append(page.url + link)
    return result

