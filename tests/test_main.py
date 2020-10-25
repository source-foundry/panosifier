#!/usr/bin/env python3

import argparse
import os

import pytest

from panosifier import __main__


def test_validate_args_exclusive(capsys):
    parser = argparse.ArgumentParser()
    parser.add_argument("--panose")
    parser.add_argument("--familytype")
    parser.add_argument("PATH", nargs="+")
    argv = ["--panose", "1", "--familytype", "1", "testfont.ttf"]
    args = parser.parse_args(argv)
    with pytest.raises(SystemExit) as e:
        __main__.validate_args_exclusive(args)

    captured = capsys.readouterr()
    assert e.type == SystemExit
    assert e.value.code == 1
    assert (
        "the '--panose' option cannot be used with other panose definition"
        in captured.err
    )


def test_validate_args_at_least_one_def(capsys):
    parser = argparse.ArgumentParser()
    parser.add_argument("--panose")
    parser.add_argument("--familytype")
    parser.add_argument("--serifstyle")
    parser.add_argument("--weight")
    parser.add_argument("--proportion")
    parser.add_argument("--contrast")
    parser.add_argument("--strokevar")
    parser.add_argument("--armstyle")
    parser.add_argument("--letterform")
    parser.add_argument("--midline")
    parser.add_argument("--xheight")
    parser.add_argument("PATH", nargs="+")
    argv = ["testfont.ttf"]
    args = parser.parse_args(argv)
    with pytest.raises(SystemExit) as e:
        __main__.validate_args_at_least_one_definition(args)

    captured = capsys.readouterr()
    assert e.type == SystemExit
    assert e.value.code == 1
    assert "include at least one panose definition in your command" in captured.err


def test_validate_args_filepaths_exist(capsys):
    parser = argparse.ArgumentParser()
    parser.add_argument("PATH", nargs="+")
    argv = ["testfont.ttf"]
    args = parser.parse_args(argv)

    # invalid path should raise exception
    with pytest.raises(SystemExit) as e:
        __main__.validate_args_filepaths_exist(args)

    captured = capsys.readouterr()
    assert e.type == SystemExit
    assert e.value.code == 1
    assert "does not appear to be a valid file" in captured.err

    # valid path should not raise exception
    argv_2 = [
        f"{os.path.join('tests', 'testfiles', 'fonts', 'NotoSans-Regular.subset.ttf')}"
    ]
    args2 = parser.parse_args(argv_2)
    __main__.validate_args_filepaths_exist(args2)
