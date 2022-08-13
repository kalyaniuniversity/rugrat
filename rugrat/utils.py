"""Provides some utilities used by other modules"""

import re
from re import Pattern

# ______________________________________________________________

list_of_str = list[str, ...]


def is_relative_path(link: str) -> bool:
    """
    Checks if the current link is absolute image url or a relative image path

    :param link: image link
    :return: True for relative path
    """

    # a valid url looks like 'https://sb.scorecardresearch.com/'
    # relative path: '../_static/py.svg'

    # image link pattern
    link_pattern: Pattern = re.compile(r"^https|http")

    mo: list = link_pattern.findall(link)

    return True if len(mo) == 0 else False


