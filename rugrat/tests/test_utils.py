import pytest
from rugrat.utils import *


def test_is_relative_path():
    assert is_relative_path('../_static/py.svg')
    assert not is_relative_path('https://sb.scorecardresearch.com/')
    assert not is_relative_path('https://sb.scorecardresearch.com/_static/py.svg')


def test_join_urls():
    assert join_urls('https://docs.python.org/3/library/typing.html',
                     '../_static/py.svg') == 'https://docs.python.org/3/_static/py.svg'
    assert join_urls('https://www.google.com/', 'https://www.unsplash.com/') == 'https://www.unsplash.com/'


if __name__ == '__main__':
    pytest.main()
