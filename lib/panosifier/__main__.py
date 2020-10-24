#!/usr/bin/env python3

import argparse
import sys
from typing import List

from . import __version__


def main() -> None:  # pragma: no cover
    run(sys.argv[1:])


def run(argv: List[str]) -> None:
    # ===========================================================
    # argparse command line argument definitions
    # ===========================================================
    parser = argparse.ArgumentParser(description="Font panose data editor")
    parser.add_argument(
        "--version", action="version", version="panosifier v{}".format(__version__)
    )
    args = parser.parse_args(argv)

    if args.version:
        pass
