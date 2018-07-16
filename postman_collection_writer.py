import re


def create_main_body(main_name):
    return {
        'info': {
            '_postman_id': "c482243b-ff44-4bd4-9dd3-48dd898da01b",
            'name': main_name,
            'description': "bla bla bla",
            'schema': "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
        },
        'item': [],
        'auth': {
            'type': "basic",
            'basic': [
                {
                    'key': "password",
                    'value': "versa123",
                    'type': "string"
                },
                {
                    'key': "username",
                    'value': "Administrator",
                    'type': "string"
                }
            ]
        },
        'event': [
            {
                'listen': "prerequest",
                'script': {
                    'id': "8d5a4e4e-0509-44af-aa03-4dd2c4dddaa7",
                    'type': "text/javascript",
                    'exec': [""]
                }
            },
            {
                'listen': "test",
                'script': {
                    'id': "5dbbeec7-5c15-4a1f-8655-ed49863646cc",
                    'type': "text/javascript",
                    'exec': [""]
                }
            }
        ]
    }


def create_item(name, method, body, api_url):
    api_url = prepare_url(api_url)
    protocol = parse_protocol(api_url)
    host = parse_host(api_url)
    port = parse_port(api_url)
    item = {
        'name': name,
        'request': {
            'method': method,
            'header': [
                {
                    'key': "Content-Type",
                    'value': "application/json"
                }
            ],
            'body': {
                'mode': "raw",
                'raw': body
            },
            'url': {
                'raw': api_url,
                'protocol': protocol,
                'host': [
                    host
                ],
                'port': port,
                'path': parse_path(api_url)
            },
            'description': "bla bla bla"
        },
        'response': []
    }
    return item


def parse_protocol(api_url):
    return api_url[:api_url.find('://')]


def parse_host(api_url):
    m = re.search('://(.*):', api_url)
    return m.group(1)


def prepare_url(api_url):
    return api_url.replace('<', '{{').replace('>', '}}')


def parse_port(api_url):
    right_pos = api_url.find('/', 10)
    return re.search('//.*:(.*)', api_url[:right_pos]).group(1)


def parse_path(api_url):
    left_pos = api_url.find('/', 10)
    return api_url[left_pos + 1:].split('/')
