from py_pwdgenerator.options import parse_options
from py_pwdgenerator.start import start as start_service


def main():
    opts = parse_options()
    start_service(opts)


if __name__ == '__main__':
    main()
