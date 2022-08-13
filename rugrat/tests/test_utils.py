import pytest
from utils import *


def test_is_relative_path():
    assert is_relative_path('../_static/py.svg')
    assert not is_relative_path('https://sb.scorecardresearch.com/')


if __name__ == '__main__':
    pytest.main()
