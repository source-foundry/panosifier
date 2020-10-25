#!/usr/bin/env python3

# Copyright 2020 Source Foundry Authors

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import os
import sys
from typing import List

from fontTools.ttLib import TTFont  # type: ignore

from . import __version__
from .datastructures import Panose


def main() -> None:  # pragma: no cover
    run(sys.argv[1:])


def validate_args_exclusive(args: argparse.Namespace) -> None:
    if args.panose and (
        args.familytype
        or args.serifstyle
        or args.weight
        or args.proportion
        or args.contrast
        or args.strokevar
        or args.armstyle
        or args.letterform
        or args.midline
        or args.xheight
    ):
        sys.stderr.write(
            f"[ERROR] the '--panose' option cannot be used with other panose definition "
            f"options{os.linesep}"
        )
        sys.exit(1)


def validate_args_at_least_one_definition(args: argparse.Namespace) -> None:
    if not args.panose and not (
        args.familytype
        or args.serifstyle
        or args.weight
        or args.proportion
        or args.contrast
        or args.strokevar
        or args.armstyle
        or args.letterform
        or args.midline
        or args.xheight
    ):
        sys.stderr.write(
            f"[ERROR] include at least one panose definition in your command "
            f"{os.linesep}"
        )
        sys.exit(1)


def validate_args_filepaths_exist(args: argparse.Namespace) -> None:
    for fontpath in args.PATH:
        if not os.path.isfile(fontpath):
            sys.stderr.write(
                f"[ERROR] '{fontpath}' does not appear to be a valid file{os.linesep}"
            )
            sys.exit(1)


def run(argv: List[str]) -> None:
    # ===========================================================
    # argparse command line argument definitions
    # ===========================================================
    parser = argparse.ArgumentParser(description="Panose data editor for fonts")
    parser.add_argument(
        "-v", "--version", action="version", version=f"panosifier v{__version__}"
    )
    parser.add_argument(
        "--panose", type=str, required=False, help="comma delimited panose value list"
    )
    parser.add_argument("--familytype", type=int, required=False, help="FamilyType value")
    parser.add_argument("--serifstyle", type=int, required=False, help="SerifStyle value")
    parser.add_argument("--weight", type=int, required=False, help="Weight value")
    parser.add_argument("--proportion", type=int, required=False, help="Propotion value")
    parser.add_argument("--contrast", type=int, required=False, help="Contrast value")
    parser.add_argument(
        "--strokevar", type=int, required=False, help="StrokeVariation value"
    )
    parser.add_argument("--armstyle", type=int, required=False, help="ArmStyle value")
    parser.add_argument("--letterform", type=int, required=False, help="Letterform value")
    parser.add_argument("--midline", type=int, required=False, help="Midline value")
    parser.add_argument("--xheight", type=int, required=False, help="XHeight value")
    parser.add_argument("PATH", nargs="+", help="Font file path")
    args = parser.parse_args(argv)

    # additional CL args validations
    validate_args_at_least_one_definition(args)
    validate_args_exclusive(args)
    validate_args_filepaths_exist(args)

    # panose data edit implementation
    for fontpath in args.PATH:
        try:
            tt = TTFont(fontpath)
        except Exception as e:
            sys.stderr.write(f"[ERROR] during edit of '{fontpath}': {str(e)}{os.linesep}")
            sys.exit(1)

        # define with comma-delimited panose definition string
        if args.panose:
            panose = Panose()
            try:
                panose.set_panose_with_comma_delim_string(args.panose)
            except ValueError as e:
                sys.stderr.write(f"[ERROR] {str(e)}{os.linesep}")
                sys.exit(1)
        # or define with individual panose definition arguments
        else:
            try:
                panose = Panose(
                    familytype=args.familytype,
                    serifstyle=args.serifstyle,
                    weight=args.weight,
                    proportion=args.proportion,
                    contrast=args.contrast,
                    strokevar=args.strokevar,
                    armstyle=args.armstyle,
                    letterform=args.letterform,
                    midline=args.midline,
                    xheight=args.xheight,
                )
            except ValueError as e:
                sys.stderr.write(f"[ERROR] {str(e)}{os.linesep}")
                sys.exit(1)

        try:
            tt = panose.set_font_panose_data(TTFont(fontpath))
            tt.save(fontpath)

            # edited font panose data report
            tt_edited = TTFont(fontpath)
            new_panose = tt_edited["OS/2"].panose.__dict__
            print(f"{fontpath} panose:")
            space = " " * 3
            print(f"{space}FamilyType: {new_panose['bFamilyType']}")
            print(f"{space}SerifStyle: {new_panose['bSerifStyle']}")
            print(f"{space}Weight: {new_panose['bWeight']}")
            print(f"{space}Proportion: {new_panose['bProportion']}")
            print(f"{space}Contrast: {new_panose['bContrast']}")
            print(f"{space}StrokeVariation: {new_panose['bStrokeVariation']}")
            print(f"{space}ArmStyle: {new_panose['bArmStyle']}")
            print(f"{space}LetterForm: {new_panose['bLetterForm']}")
            print(f"{space}Midline: {new_panose['bMidline']}")
            print(f"{space}XHeight: {new_panose['bXHeight']}")
        except Exception as e:
            sys.stderr.write(f"[ERROR] '{fontpath}' error: {str(e)}{os.linesep}")
            sys.exit(1)
