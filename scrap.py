#!/usr/bin/env python

import json
import argparse
from pprint import pprint
from lxml import html
import requests

parser = argparse.ArgumentParser(description='Webscraper')
parser.add_argument('-u', '--url', metavar='URL', help='Site to scrap')
parser.add_argument('-s', '--scrap', metavar='NAME:XPATH', help='Scraping pattern', required=True, nargs='+')
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="count", default=0)

args = parser.parse_args()
if args.verbose:
    print "verbosity turned on to %s" % args.verbose

patterns = {}
for pattern in args.scrap:
    split = pattern.split(':', 1)
    patterns[split[0]] = split[1]

if args.verbose:
    pprint(args, indent=3)
    print ("URL: %s" % args.url)
    pprint(patterns, indent=3)

page = requests.get(args.url)
tree = html.fromstring(page.content)

response_json = {}
for patternName in patterns:
    pattern = patterns[patternName]
    elements = tree.xpath(pattern)
    children = []
    if len(elements) == 0:
        children = '*'
    elif len(elements) == 1:
        children = elements[0].strip()
    else:
        for e in elements:
            children.append(e.strip())
    response_json[patternName] = children

print json.dumps(response_json, separators=(',', ':'))
