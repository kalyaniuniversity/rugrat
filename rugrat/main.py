from bs4 import BeautifulSoup
from bs4.element import ResultSet
import requests
from utils import *
from urllib.parse import urljoin


def scrape_images(url: str) -> list_of_str | None:
    """
    Scrape image links from the given website

    :param url: url for the website
    :return: list of the image links or None
    """

    try:
        # html content from a website
        html_text: str = requests.get(url).text

        # BeautifulSoup instance of the html content
        soup: BeautifulSoup = BeautifulSoup(html_text, 'lxml')

        # all 'img' tags from the page
        all_image_tags: ResultSet = soup.findAll('img')

        # return the list of the images links
        all_image_links: list_of_str = [
            img['src'] if not is_relative_path(img['src'])
            else urljoin(url, img['src'])
            for img in all_image_tags
        ]

        return all_image_links

    except Exception as error:
        print(f"Could not get the links! Possible errors:\n{error}")


if __name__ == '__main__':
    web_page: str = 'https://unsplash.com/'
    # web_page: str = 'https://docs.python.org/3/library/typing.html'

    # all the image links
    image_links: list_of_str = scrape_images(web_page)

    print(image_links)
