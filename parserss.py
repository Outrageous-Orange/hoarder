#!/usr/bin/env python

import xml.etree.ElementTree
from lxml import html
import requests
root = xml.etree.ElementTree.parse('rss/dalarna.xml').getroot()
# res = root.findall('.')
for e in root.findall('.//item'):
    title = e.find('title').text
    link = e.find('link').text
    print(title, link)

    page = requests.get(link)
    tree = html.fromstring(page.content)
    content = tree.xpath('//div[@class="event-page editorial-content"]/h1/text()')
    print(content)
    break