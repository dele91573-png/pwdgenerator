from dataclasses import dataclass
import argparse
import sys
from .logger import Errorf, Infof
from .utils import check_domain_key, get_file_name


@dataclass
class Options:
    domain_key: str = ""
    min_len: int = 0
    max_len: int = 30
    level: int = 1
    file_name: str = ""


def parse_options() -> Options:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", dest="domain_key", default="", help="域名关键字")
    parser.add_argument("--min", dest="min_len", type=int, default=0, help="密码最小长度")
    parser.add_argument("--max", dest="max_len", type=int, default=30, help="密码最大长度")
    parser.add_argument("-l", dest="level", type=int, default=1, help="密码复杂级别，1-5")
    parser.add_argument("-o", dest="file_name", default="", help="输出的文件名，默认为txt格式")
    args = parser.parse_args()

    opts = Options()
    if args.domain_key:
        if check_domain_key(args.domain_key):
            opts.domain_key = args.domain_key
        else:
            Errorf(" 输入的关键词有问题")
            sys.exit(-1)

    if args.min_len >= 0:
        opts.min_len = args.min_len
    else:
        Errorf(" 设定的密码最小长度有问题")
        sys.exit(-1)

    if args.max_len > 0:
        opts.max_len = args.max_len
    else:
        Errorf(" 设定的密码最大长度有问题")
        sys.exit(-1)

    if opts.min_len > opts.max_len:
        Errorf("密码最大长度需大于最小长度")
        sys.exit(-1)

    if 0 < args.level <= 5:
        opts.level = args.level
    else:
        Errorf(" 密码复杂度 level 仅支持1-5之间选择")
        sys.exit(-1)

    if args.file_name == "":
        opts.file_name = get_file_name(opts.domain_key)
    else:
        if ".txt" not in args.file_name:
            opts.file_name = args.file_name + ".txt"
            Infof("%s", opts.file_name)
        else:
            opts.file_name = args.file_name

    return opts
