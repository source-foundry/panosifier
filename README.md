## panosifier

### panose data editor for fonts

[![PyPI](https://img.shields.io/pypi/v/panosifier?color=blueviolet&label=PyPI&logo=python&logoColor=white)](https://pypi.org/project/panosifier/)
[![GitHub license](https://img.shields.io/github/license/source-foundry/panosifier?color=blue)](https://github.com/source-foundry/panosifier/blob/master/LICENSE)
![Python CI](https://github.com/source-foundry/panosifier/workflows/Python%20CI/badge.svg)
![Python Lints](https://github.com/source-foundry/panosifier/workflows/Python%20Lints/badge.svg)
![Python Type Checks](https://github.com/source-foundry/panosifier/workflows/Python%20Type%20Checks/badge.svg)
[![codecov](https://codecov.io/gh/source-foundry/panosifier/branch/main/graph/badge.svg?token=zOdnBS0hIv)](https://codecov.io/gh/source-foundry/panosifier/)

### About

panosifier is a Python 3.6+ command line application that edits [panose data](https://monotype.github.io/panose/pan1.htm) in fonts.  The tool edits the [OpenType specification defined panose fields](https://docs.microsoft.com/en-us/typography/opentype/spec/os2#panose).

### Why do I need this tool?

In many cases, you can define these values in your type design source files and rely on the font compiler to write these values into your font instances; however, there are situations where this behavior is not well-defined and differs across font compilers.  

An example is the approach to panose data writes in variable font format files.  In this case the OpenType specification is vague, environments where these data are important are not well-defined, and compilers handle the source file defined panose data differently.  

This tool will allow you to modify build-time decisions in these situations.

### Quick Start

- Install in a Python 3.6+ virtual environment with `pip install panosifier`
- Define your panose values with a comma-delimited panose value list using the `--panose` command line option or individually with the ten available OpenType panose field options (see `panosifier --help` for a list of available options)

See the documentation below for additional details.


