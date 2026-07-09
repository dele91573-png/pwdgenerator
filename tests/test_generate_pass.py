import os
from py_pwdgenerator.generate_pass import get_list_by_format, check_format
from py_pwdgenerator.config import common_number_file


def test_check_format_known_values():
    assert check_format('key')
    assert check_format('special_letter')
    assert check_format('year')
    assert not check_format('unknown')


def test_get_list_by_format_key():
    result = get_list_by_format('key', 'test')
    assert result == ['test']


def test_get_list_by_format_year():
    result = get_list_by_format('year', 'test')
    assert '2015' in result
    assert '2020' in result


def test_get_list_by_format_special_letter():
    result = get_list_by_format('special_letter', 'test')
    assert '!' in result
    assert '*' in result


def test_get_list_by_format_file_loading():
    # Ensure the common number file can be loaded and returns a list
    assert os.path.exists(common_number_file)
    result = get_list_by_format('common_number', 'test')
    assert isinstance(result, list)
