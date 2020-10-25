#!/usr/bin/env python3

import argparse
import os
import shutil
import tempfile

import pytest
from fontTools.ttLib import TTFont

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


def test_run_define_with_options():
    test_font_name = "NotoSans-Regular.subset.ttf"
    source_path = os.path.join("tests", "testfiles", "fonts", test_font_name)
    with tempfile.TemporaryDirectory() as tmpdirname:
        dest_path = os.path.join(tmpdirname, test_font_name)
        shutil.copyfile(source_path, dest_path)

        # confirm pre panose data
        tt_pre = TTFont(dest_path)
        assert tt_pre["OS/2"].panose.bFamilyType == 2
        assert tt_pre["OS/2"].panose.bSerifStyle == 11
        assert tt_pre["OS/2"].panose.bWeight == 5
        assert tt_pre["OS/2"].panose.bProportion == 2
        assert tt_pre["OS/2"].panose.bContrast == 4
        assert tt_pre["OS/2"].panose.bStrokeVariation == 5
        assert tt_pre["OS/2"].panose.bArmStyle == 4
        assert tt_pre["OS/2"].panose.bLetterForm == 2
        assert tt_pre["OS/2"].panose.bMidline == 2
        assert tt_pre["OS/2"].panose.bXHeight == 4

        argv = ["--proportion", "9", "--xheight", "2", f"{dest_path}"]
        __main__.run(argv)

        tt_post = TTFont(dest_path)
        assert tt_post["OS/2"].panose.bFamilyType == 2
        assert tt_post["OS/2"].panose.bSerifStyle == 11
        assert tt_post["OS/2"].panose.bWeight == 5
        assert tt_post["OS/2"].panose.bProportion == 9
        assert tt_post["OS/2"].panose.bContrast == 4
        assert tt_post["OS/2"].panose.bStrokeVariation == 5
        assert tt_post["OS/2"].panose.bArmStyle == 4
        assert tt_post["OS/2"].panose.bLetterForm == 2
        assert tt_post["OS/2"].panose.bMidline == 2
        assert tt_post["OS/2"].panose.bXHeight == 2


def test_run_define_with_panose_comma_delimited_definition():
    test_font_name = "NotoSans-Regular.subset.ttf"
    source_path = os.path.join("tests", "testfiles", "fonts", test_font_name)
    with tempfile.TemporaryDirectory() as tmpdirname:
        dest_path = os.path.join(tmpdirname, test_font_name)
        shutil.copyfile(source_path, dest_path)

        # confirm pre panose data
        tt_pre = TTFont(dest_path)
        assert tt_pre["OS/2"].panose.bFamilyType == 2
        assert tt_pre["OS/2"].panose.bSerifStyle == 11
        assert tt_pre["OS/2"].panose.bWeight == 5
        assert tt_pre["OS/2"].panose.bProportion == 2
        assert tt_pre["OS/2"].panose.bContrast == 4
        assert tt_pre["OS/2"].panose.bStrokeVariation == 5
        assert tt_pre["OS/2"].panose.bArmStyle == 4
        assert tt_pre["OS/2"].panose.bLetterForm == 2
        assert tt_pre["OS/2"].panose.bMidline == 2
        assert tt_pre["OS/2"].panose.bXHeight == 4

        argv = ["--panose", "1,2,3,4,5,6,7,8,9,10", f"{dest_path}"]
        __main__.run(argv)

        tt_post = TTFont(dest_path)
        assert tt_post["OS/2"].panose.bFamilyType == 1
        assert tt_post["OS/2"].panose.bSerifStyle == 2
        assert tt_post["OS/2"].panose.bWeight == 3
        assert tt_post["OS/2"].panose.bProportion == 4
        assert tt_post["OS/2"].panose.bContrast == 5
        assert tt_post["OS/2"].panose.bStrokeVariation == 6
        assert tt_post["OS/2"].panose.bArmStyle == 7
        assert tt_post["OS/2"].panose.bLetterForm == 8
        assert tt_post["OS/2"].panose.bMidline == 9
        assert tt_post["OS/2"].panose.bXHeight == 10


def test_run_invalid_font_filepath(capsys):
    test_path = os.path.join("tests", "testfiles", "fonts", "README.md")
    argv = ["--panose", "1,2,3,4,5,6,7,8,9,10", f"{test_path}"]

    with pytest.raises(SystemExit) as e:
        __main__.run(argv)

    captured = capsys.readouterr()
    assert e.type == SystemExit
    assert e.value.code == 1
    assert "[ERROR]" in captured.err


def test_run_invalid_panose_definition(capsys):
    test_font_name = "NotoSans-Regular.subset.ttf"
    source_path = os.path.join("tests", "testfiles", "fonts", test_font_name)
    with tempfile.TemporaryDirectory() as tmpdirname:
        dest_path = os.path.join(tmpdirname, test_font_name)
        shutil.copyfile(source_path, dest_path)

        # test with too many panose values
        argv = ["--panose", "1,2,3,4,5,6,7,8,9,10,11", f"{dest_path}"]

        with pytest.raises(SystemExit) as e:
            __main__.run(argv)

    captured = capsys.readouterr()
    assert e.type == SystemExit
    assert e.value.code == 1
    assert "[ERROR]" in captured.err


def test_run_invalid_option_definition(capsys):
    test_font_name = "NotoSans-Regular.subset.ttf"
    source_path = os.path.join("tests", "testfiles", "fonts", test_font_name)
    with tempfile.TemporaryDirectory() as tmpdirname:
        dest_path = os.path.join(tmpdirname, test_font_name)
        shutil.copyfile(source_path, dest_path)

        # test with non-integer definition
        argv = ["--proportion", "bogus", f"{dest_path}"]

        with pytest.raises(SystemExit) as e:
            __main__.run(argv)

        captured = capsys.readouterr()
        assert e.type == SystemExit
        assert e.value.code == 2
        assert "invalid int value" in captured.err
