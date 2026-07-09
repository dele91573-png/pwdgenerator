import os
import time
from .logger import Infof, Errorf


def get_file_name(filename: str) -> str:
    time_unix = int(time.time())
    name = f"{filename}_{time_unix}.txt"
    Infof(" filename未设定，生成名为：%s\n", name)
    return name


def check_domain_key(domain_key: str) -> bool:
    return True


def get_path() -> str:
    path = "./results/"
    try:
        os.makedirs(path, exist_ok=True)
    except Exception as e:
        Errorf("创建结果目录失败：%s", str(e))
        raise
    return path


def merge_slice(s1: list[str], s2: list[str]) -> list[str]:
    return s1 + s2


def remove_duplicate_element(items: list[str]) -> list[str]:
    seen = set()
    out = []
    for it in items:
        if it not in seen:
            seen.add(it)
            out.append(it)
    return out


def uniq(file_path: str, filename: str, option) -> bool:
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception:
        return False
    slice_list = content.split("\n")
    result = remove_duplicate_element(slice_list)
    path = get_path()
    file_path_new = path + "筛选完毕" + filename
    try:
        with open(file_path_new, "w", encoding="utf-8") as fw:
            from .filter import filter_pass
            for password in result:
                if filter_pass(password, option):
                    fw.write(password + "\n")
    except Exception:
        return False
    return True
