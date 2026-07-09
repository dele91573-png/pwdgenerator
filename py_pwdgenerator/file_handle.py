from .logger import Errorf


def file_load(file_path: str, buf_size: int = 1024) -> str:
    try:
        with open(file_path, "rb") as f:
            chunks = []
            while True:
                b = f.read(buf_size)
                if not b:
                    break
                chunks.append(b)
        return b"".join(chunks).decode(errors="ignore")
    except Exception as e:
        Errorf("%s", str(e))
        return ""


def remove_file(path: str):
    import os
    try:
        os.remove(path)
    except Exception as e:
        Errorf("%s", str(e))
