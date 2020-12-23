import contextlib
import os
import time
import urllib

import requests
from bs4 import BeautifulSoup

from reliable.settings import BASE_DIR


def fetch_html(url):

    print("url: %s" % url)

    _buffer = ""

    try:

        response = requests.get(url, timeout=4)

        status_code = response.status_code
        print("status_code: %s" % status_code)

        if status_code == 200:

            _buffer = response.text

        else:  # not 200
            pass

    except Exception as e:
        print("e: %s" % e)

    time.sleep(0.25)

    return _buffer


def extract_urls(html):

    _buffer = []

    try:

        soup = BeautifulSoup(html, "html.parser")

        for link in soup.findAll('a'):

            url = str(link.get('href'))

            if "reliablecontrols.com" in url:  # internal url

                if "/products/" in url:

                    if ".pdf" not in url:  # not pdf

                        if "#" not in url:

                            _buffer.append(url)

                        else:  # has anchor tag

                            length = len(url)
                            position = url.find("#")
                            diff = length - position

                            url = url[:-diff]

                            if url not in _buffer:

                                _buffer.append(url)

    except Exception as e:
        print("e: %s" % e)

    time.sleep(0.25)

    return _buffer


def extract_description(html):

    _buffer = ""

    try:

        soup = BeautifulSoup(html, "html.parser")

        for meta in soup.findAll('meta'):

            name = str(meta.get('name'))

            if name == "description":

                content = str(meta.get('content'))
                content = content.rstrip('\r\n')
                content = content.lstrip('\r\n')

                content = content.replace("<br>", "")

                return content

    except Exception as e:
        print("e: %s" % e)

    time.sleep(0.25)

    return _buffer


def extract_title(html):

    _buffer = ""

    try:

        soup = BeautifulSoup(html, "html.parser")

        for title in soup.findAll('title'):

            title = str(title)
            title = title.replace("<title>", "")
            title = title.replace("</title>", "")
            title = title.replace("Reliable Controls | ", "")
            title = title.replace("Peripheral Partner - ", "")
            title = title[:255]

            return title

    except Exception as e:
        print("e: %s" % e)

    time.sleep(0.25)

    return _buffer
