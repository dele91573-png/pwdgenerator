from .file_handle import file_load
from . import config
from .utils import merge_slice
from .logger import Infof


def add_common_pass(f):
    res = file_load(config.common_pass_file, 1024)
    if res:
        f.write(res)
        return True
    return False


def add_keyboard_pass(f):
    res = file_load(config.keyboard_pass, 1024)
    if res:
        f.write(res)
        return True
    return False


def add_rule_pass(f, key: str) -> bool:
    rules = [
        "key+special_letter+year",
        "key+special_letter+keyboard_walk",
        "key+keyboard_walk",
        "key+special_letter+common_pass",
        "common_pass+special_letter+key",
        "key+common_pass",
        "key+special_letter+china_name",
        "china_name+special_letter+key",
        "key+special_letter+common_number",
        "key+common_number+special_letter",
    ]
    for count, value in enumerate(rules):
        Infof(" 增加第%d种可能：%s\n", count + 1, value)
        rule = value.split("+")
        result_list = rule_got_pass(key, rule)
        if result_list:
            for p in result_list:
                pass_str = p.replace(" ", "").replace("\n", "").replace("\r", "") + "\r\n"
                f.write(pass_str)
    return True


def rule_got_pass(key: str, rule: list[str]) -> list[str]:
    rule_list = []
    tmp_pass_list = []
    store_tmp_list = []
    for k in rule:
        if check_format(k):
            if not store_tmp_list:
                tmp_pass_list = get_list_by_format(k, key)
                store_tmp_list = merge_slice(store_tmp_list, tmp_pass_list)
                tmp_pass_list = []
            else:
                tmp = []
                tmp_pass_list = get_list_by_format(k, key)
                for v in store_tmp_list:
                    for vv in tmp_pass_list:
                        p = (v + vv).replace("\n", "")
                        tmp.append(p)
                store_tmp_list = tmp
                tmp = []
        else:
            Infof("rules had wrong fotmat: %s", k)
    rule_list = store_tmp_list
    return rule_list


def check_format(k: str) -> bool:
    fmt = ["key", "special_letter", "year", "keyboard_walk", "common_pass", "china_name", "common_number"]
    return k in fmt


def get_list_by_format(k: str, key: str) -> list[str]:
    special_letter = ["!", "@", "#", "$", "%", "*"]
    year = ["2015", "2016", "2017", "2018", "2019", "2020"]
    china_name = file_load(config.china_name_file, 1024)
    keyboard_walk = file_load(config.keyboard_walk_file, 1024)
    common_number = file_load(config.common_number_file, 1024)
    common_pass = file_load(config.common_pass_file, 1024)
    lst = []
    if k == "key":
        lst.append(key)
    elif k == "special_letter":
        lst = merge_slice(lst, special_letter)
        return lst
    elif k == "year":
        lst = merge_slice(lst, year)
        return lst
    elif k == "china_name":
        lst.append(china_name)
    elif k == "keyboard_walk":
        lst.append(keyboard_walk)
    elif k == "common_number":
        lst.append(common_number)
    elif k == "common_pass":
        lst.append(common_pass)
    # split first element by newlines
    if not lst:
        return []
    return lst[0].split("\n")
