# pwdgenerator — Python port

This repository contains a Python port of the original Go `pwdgenerator` utility.

Quick start

1. Run the generator (example):

```bash
/home/codespace/.python/current/bin/python main.py -d example --min 4 --max 12 -l 2 -o out.txt
```

2. Output files are written to `./results/` (a deduplicated, filtered file named `筛选完毕<filename>`).

Notes
- The Python port lives in the `py_pwdgenerator` package.
- No external Python dependencies are required; it uses the standard library.

Files added
- `py_pwdgenerator/` — translated modules: `options.py`, `filter.py`, `generate_pass.py`, `file_handle.py`, `utils.py`, `start.py`, `config.py`, `logger.py`.
- `main.py` — CLI entrypoint wired to the Python `start` flow.
- `server.py` — simple HTTP server that serves `web_ui.html` and runs the generator at `/run`.
- `web_ui.html` — browser form for generator input.

Web UI and server usage
1. Start the server:

```bash
/home/codespace/.python/current/bin/python server.py
```

2. Open the UI in your browser:

```text
http://127.0.0.1:8000/
```

3. Or call the generator directly:

```bash
curl "http://127.0.0.1:8000/run?d=example&min=4&max=12&l=2&o=web_out.txt"
```

4. Generated output files and deduplicated results are written to `./results/`.

Testing

Install pytest and run:

```bash
python -m pip install pytest
pytest
```

If you want a packaged distribution or tests, tell me which test framework you prefer and I will add them.
# pwdgenerator
定制化密码字典生成器
(根据bit4woo表哥的passmaker项目写的～ 🙏)

使用方法,下载release
命令行下:  ./pwdgenerator -h 

简单使用 ./pwdgenerator -d baidu.com -min 6 -max 10

Customized password dictionary generator

How to use 

download release

command line: ./pwdgenerator -h

simple usage ./pwdgenerator -d baidu.com -min 6 -max 10

Note: generated output files are written to the `results/` directory. The program creates `results/` automatically if it does not exist.
