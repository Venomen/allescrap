#!/usr/bin/python3
# -*- encoding: utf-8 -*-
#  Copyright (c) 2019 - Dawid Deręgowski - MIT

__author__ = "Dawid Deręgowski"
__copyright__ = "Copyright (c) $today.year - deregowski.net Dawid Deręgowski"
__license__ = "MIT"
__version__ = "0.1"

"""
WTF?
Some simple script to webscrap [getting url in this case] Allegro auctions (for example).

Configuration
Change configuration data in conf.py file to make it good for you ;). Delay time, seller id/name etc.
Script is showing only 1st URL result and if it has been found, then opens system default browser.

Running
You can use '--help' to check options:

Using API:
./allescrap.py --api

Using Web:
./allescrap.py --web

Refreshing Token:
./alescrap.py --refresh
"""

import urllib
from urllib import request
from bs4 import BeautifulSoup
import time
import webbrowser
import json
import conf
import requests
from sys import argv
import argparse


# showing only 1st parsed result - aiming for the prize :_)


def get_alle_from_api():

    while True:

        print("Running API search... (%s sec. delay) -- CTR+C to stop!" % conf.delay)

        try:
            opener = urllib.request.build_opener()
            opener.addheaders = conf.api_access_token_h['allegro']
            opener = urllib.request.install_opener(opener)

            response = request.urlopen(conf.api_url_get_offers)
            result = response.read()
            result = json.loads(result)
            result = result['items']['promoted']
            result = json.dumps(result)

            auction_id = result.split('"')[3]

            print("I've found auction ID!", auction_id)
            print("Openning browser... Bye, bye.")
            webbrowser.open(conf.api_allegro_listing % auction_id)
            break

        except Exception as details:
            print("Ups, no results...", details)

        time.sleep(conf.delay)


def get_alle_url():

    while True:

        print("Running search... (%s sec. delay) -- CTRL+C to stop!" % conf.delay)

        try:
            response = request.urlopen(conf.req)
            result = response.read()
            soup = BeautifulSoup(result, 'html.parser')
            data = soup.find_all("div", attrs=conf.div_class)
            data = str(data)
            data = data.split('"')[5]

            print("I've found URL!", data)
            print("Openning browser... Bye, bye.")
            webbrowser.open(data)
            break

        except Exception as details:
            print("Ups, no results...", details)

        time.sleep(conf.delay)


def refresh_token():

    print("Running request for refreshing token...")

    try:
        response = requests.post(conf.api_url_refresh_token, headers=conf.api_refresh_token_h)
        response = response.text

        response = json.loads(response)
        print(response)
        # grab token and change it in conf file

    except Exception as details:
        print("Ups, no results...", details)


if __name__ == "__main__":
    if "--help" in argv:  # little help menu
        parser = argparse.ArgumentParser(description="Simple script for Allegro API"
                                                     " for ex. searching new user auctions.")
        parser.add_argument('api', nargs='?', help='example: "./allescrap.py api" - api scraping method')
        parser.add_argument('web', nargs='?', help='example: "./allescrap.py web" - web scraping method')
        parser.add_argument('refresh', nargs='?', help='example: "./allescrap.py refresh" - refreshing tokens')
        args = parser.parse_args()

    if "api" in argv:
        get_alle_from_api()

    if "web" in argv:
        get_alle_from_api()

    if "refresh" in argv:
        refresh_token()
