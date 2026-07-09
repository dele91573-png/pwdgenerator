from .logger import Infof
from .utils import get_path, uniq
from .generate_pass import add_rule_pass, add_common_pass, add_keyboard_pass


def start(option):
    Infof(" 当前关键词：%s\n", option.domain_key)
    Infof(" 当前level：%d\n", option.level)
    path = get_path()
    file_path = path + option.file_name
    try:
        f = open(file_path, "w", encoding="utf-8")
    except Exception as e:
        from .logger import Errorf
        Errorf("创建文件失败：%s\n", str(e))
        return
    try:
        Infof(" 根据规则生成对应密码\n")
        if add_rule_pass(f, option.domain_key):
            Infof(" 根据规则生成对应密码成功\n")
        Infof(" 加入一点常见弱口令\n")
        if add_common_pass(f):
            Infof(" 增加常见弱口令成功\n")
        Infof(" 加入一点键盘顺序弱口令\n")
        if add_keyboard_pass(f):
            Infof(" 增加键盘顺序弱口令成功\n")
    finally:
        f.close()

    Infof(" 对结果进行去重、复杂度检测、长度筛选\n")
    if uniq(file_path, option.file_name, option):
        Infof(" 去重、复杂度检测、长度筛选成功\n")
