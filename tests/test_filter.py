import pytest

from py_pwdgenerator.filter import filter_pass
from py_pwdgenerator.options import Options


def test_filter_pass_rejects_short_password():
    opts = Options(min_len=6, max_len=12, level=1)
    assert not filter_pass("abc", opts)


def test_filter_pass_rejects_long_password():
    opts = Options(min_len=1, max_len=5, level=1)
    assert not filter_pass("123456", opts)


def test_filter_pass_requires_complexity():
    opts = Options(min_len=1, max_len=20, level=3)
    assert filter_pass("aA1!", opts)
    assert not filter_pass("aaaa", opts)
    assert not filter_pass("AAAA", opts)
    assert not filter_pass("1111", opts)


def test_filter_pass_accepts_valid_password():
    opts = Options(min_len=1, max_len=20, level=2)
    assert filter_pass("aA1", opts)
    assert filter_pass("a1!", opts)
