import sys
from enum import IntEnum


class Level(IntEnum):
    Null = 0
    Fatal = 1
    Silent = 2
    Label = 3
    Misc = 4
    Error = 5
    Warning = 6
    Info = 7
    Debug = 8
    Verbose = 9


MaxLevel = Level.Info


def _format_label(level: Level, label: str) -> str:
    if level in (Level.Silent, Level.Misc):
        return ""
    lookup = {
        Level.Warning: "Warning",
        Level.Error: "Error",
        Level.Label: "WRN",
        Level.Fatal: "Fatal",
        Level.Debug: "DEBUG",
        Level.Info: "INFO",
    }
    return f"[{lookup.get(level, label)}] "


def _log(level: Level, label: str, fmt: str, *args):
    if level == Level.Null:
        return
    if level <= MaxLevel:
        msg = fmt % args if args else fmt
        out = _format_label(level, label) + msg
        print(out, file=sys.stdout)


def Infof(fmt: str, *args):
    _log(Level.Info, "", fmt, *args)


def Warningf(fmt: str, *args):
    _log(Level.Warning, "", fmt, *args)


def Errorf(fmt: str, *args):
    _log(Level.Error, "", fmt, *args)


def Debugf(fmt: str, *args):
    _log(Level.Debug, "", fmt, *args)


def Verbosef(fmt: str, label: str, *args):
    _log(Level.Verbose, label, fmt, *args)


def Silentf(fmt: str, *args):
    _log(Level.Silent, "", fmt, *args)


def Fatalf(fmt: str, *args):
    _log(Level.Fatal, "", fmt, *args)
    sys.exit(1)


def Printf(fmt: str, *args):
    _log(Level.Misc, "", fmt, *args)


def Labelf(fmt: str, *args):
    _log(Level.Label, "", fmt, *args)
