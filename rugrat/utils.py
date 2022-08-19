"""Provides some utilities used by other modules"""

from typing import AnyStr
from urllib.parse import urljoin, urlparse
import csv
import json


# ______________________________________________________________


def is_relative_path(link: str) -> bool:
    """
    Checks if the given link is relative link or absolute link.
    "scheme://netloc/path;parameters?query#fragment"
    If the url has scheme and netloc then it is absolute link
    If the url has path only, then it is relative link

    :param link:
    :return: True if the link is relative
    """
    parsed_url = urlparse(link)
    return not parsed_url.scheme and not parsed_url.netloc


def join_urls(link1: str, link2: str) -> AnyStr:
    """
    Join website URL with the image URL;
    if the image URL is absolute then it returns the same
    if the image URL is relative then it joins it with the website URL and returns

    :param link1: website URL
    :param link2: image link relative or absolute
    :return: absolute path of the image
    """
    return urljoin(link1, link2)


def save_as_csv(filename: str, links: list[str]) -> None:
    """
    Save all the links in a CSV file.

    :param filename: filename of the csv file
    :param links: image links scraped from the website
    """
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for link in links:
            writer.writerow([link])


def save_as_json(filename: str, links: list[str]) -> None:
    links_dict = dict(
        image_links=links
    )

    with open(filename, 'w') as json_file:
        json.dump(links_dict, json_file)
