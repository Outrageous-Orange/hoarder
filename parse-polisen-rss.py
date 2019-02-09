#!/usr/bin/env python3

from defusedxml import ElementTree
import argparse
import datetime
import itertools
import json
import operator
import urllib.request

parser = argparse.ArgumentParser(description="Parse Polisen's RSS feed")
parser.add_argument('--file', '-f',
                    nargs='*',
                    default=[],
                    type=argparse.FileType('r'),
                    help='RSS file(s)')
parser.add_argument('--url', '-u',
                    nargs='*',
                    default=[],
                    type=urllib.request.urlopen,
                    help='RSS feed URL(s)')
args = parser.parse_args()

def get_items(feed):
    rss = ElementTree.parse(feed)
    for item in rss.iter('item'):
        yield { e.tag: e.text for e in item }

def unique(iterable, key):
    return list({ key(i): i for i in iterable }.values())

def convert_date(date):
    return (datetime.datetime
        .strptime(date, '%a, %d %b %Y %H:%M:%S %z')
        .isoformat())

items = (
    item
    for feed in itertools.chain(args.file, args.url)
    for item in get_items(feed)
)
items = unique(items, key=operator.itemgetter('guid'))
for item in items:
    item['pubDate'] = convert_date(item['pubDate'])
print(json.dumps(items))
