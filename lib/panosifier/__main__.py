#!/usr/bin/env python3

import argparse
import os
import sys
from typing import List

from . import __version__


def main() -> None:  # pragma: no cover
    run(sys.argv[1:])


def _validate_args(args: argparse.Namespace) -> None:
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


def run(argv: List[str]) -> None:
    # ===========================================================
    # argparse command line argument definitions
    # ===========================================================
    parser = argparse.ArgumentParser(description="Font panose data editor")
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
    # validate exclusive argument combinations
    _validate_args(args)
