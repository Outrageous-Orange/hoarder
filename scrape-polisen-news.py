#!/usr/bin/env python3

import argparse
import json
import lxml.html
import requests

parser = argparse.ArgumentParser(description="Scrape Polisen's news articles")
parser.add_argument('file',
                    type=argparse.FileType('r'),
                    help='File containing the RSS events (JSON)')
args = parser.parse_args()

def scrape_news(url):
    html = requests.get(url).text
    html = lxml.html.fromstring(html)
    xpaths = {
        'headline': r'//div[@class="event-page editorial-content"]/h1/text()',
        'preamble': r'//p[@class="preamble"]/text()',
        'body': r'//div[@class="text-body editorial-html"]/p/text()',
    }
    def get_text(xpath):
        lines = html.xpath(xpath)
        lines = ( s.strip() for s in lines )
        return '\n'.join(s for s in lines if s)
    return {key: get_text(xpath) for key, xpath in xpaths.items()}

events = json.load(args.file)
urls = ( event['link'] for event in events )
news = [ { 'url': url, **scrape_news(url) } for url in urls ]
print(json.dumps(news))
