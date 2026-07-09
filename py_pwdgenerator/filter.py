from .logger import Infof


def filter_pass(password: str, option) -> bool:
    password = password.replace(" ", "").replace("\n", "")
    if len(password) < option.min_len:
        return False
    if len(password) > option.max_len:
        return False
    kind = 1
    if check_special_char(password):
        kind += 1
    if check_number(password):
        kind += 1
    if check_upper_letter(password):
        kind += 1
    if check_lower_letter(password):
        kind += 1
    if kind <= option.level:
        return False
    return True


def check_special_char(password: str) -> bool:
    for ch in password:
        o = ord(ch)
        if 32 <= o <= 47 or 58 <= o <= 64 or 91 <= o <= 96 or 123 <= o <= 126:
            return True
    return False


def check_number(password: str) -> bool:
    return any(ch.isdigit() for ch in password)


def check_upper_letter(password: str) -> bool:
    return any('A' <= ch <= 'Z' for ch in password)


def check_lower_letter(password: str) -> bool:
    return any('a' <= ch <= 'z' for ch in password)
