import urllib.request
import ssl
import links_parser

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
page = urllib.request.urlopen('https://10.101.72.106/docs/rest/', context=ctx)
links_parser.parse_links_to_api(page)
