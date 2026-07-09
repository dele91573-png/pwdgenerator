import pytest
from py_pwdgenerator.options import parse_options, Options


def test_parse_options_with_defaults(monkeypatch):
    monkeypatch.setattr('sys.argv', ['main.py'])
    opts = parse_options()
    assert opts.min_len == 0
    assert opts.max_len == 30
    assert opts.level == 1
    assert opts.file_name.endswith('.txt')


def test_parse_options_with_values(monkeypatch):
    monkeypatch.setattr('sys.argv', ['main.py', '-d', 'example', '--min', '4', '--max', '12', '-l', '2', '-o', 'out.txt'])
    opts = parse_options()
    assert opts.domain_key == 'example'
    assert opts.min_len == 4
    assert opts.max_len == 12
    assert opts.level == 2
    assert opts.file_name == 'out.txt'
