# panosifier

### panose data editor for fonts

[![PyPI](https://img.shields.io/pypi/v/panosifier?color=blueviolet&label=PyPI&logo=python&logoColor=white)](https://pypi.org/project/panosifier/)
[![GitHub license](https://img.shields.io/github/license/source-foundry/panosifier?color=blue)](https://github.com/source-foundry/panosifier/blob/main/LICENSE)
![Python CI](https://github.com/source-foundry/panosifier/workflows/Python%20CI/badge.svg)
![Python Lints](https://github.com/source-foundry/panosifier/workflows/Python%20Lints/badge.svg)
![Python Type Checks](https://github.com/source-foundry/panosifier/workflows/Python%20Type%20Checks/badge.svg)
[![codecov](https://codecov.io/gh/source-foundry/panosifier/branch/main/graph/badge.svg?token=zOdnBS0hIv)](https://codecov.io/gh/source-foundry/panosifier/)

## About

panosifier is a Python 3.6+ command line application that edits [panose data](https://monotype.github.io/panose/pan1.htm) in fonts.  The tool edits the [OpenType specification defined panose fields](https://docs.microsoft.com/en-us/typography/opentype/spec/os2#panose).

## Why do I need this tool?

In many cases, you can define these values in your type design source files and rely on the font compiler to write these values into your font instances; however, there are situations where this behavior is not well-defined and differs across font compilers.  

An example is the approach to panose data writes in variable font format files.  In this case the OpenType specification is vague, environments where these data are important are not well-defined, and compilers handle the source file defined panose data differently.  

This tool will allow you to modify build-time decisions in these situations.

## Quick Start

- Install in a Python 3.6+ virtual environment with `pip install panosifier`
- Define your panose values with a comma-delimited panose value list using the `--panose` command line option or individually with the ten available OpenType panose field options (see `panosifier --help` for a list of available options)

See the documentation below for additional details.

## Installation

This project requires a Python 3.6+ interpreter.

Installation in a Python3 virtual environment is recommended.

Use any of the following installation approaches:

### pip install from PyPI

```
$ pip3 install panosifier
```

### pip install from source

```
$ git clone https://github.com/source-foundry/panosifier.git
$ cd panosifier
$ pip3 install -r requirements.txt .
```

### Developer install from source

The following approach installs the project and associated optional developer dependencies so that source changes are available without the need for re-installation.

```
$ git clone https://github.com/source-foundry/panosifier.git
$ cd panosifier
$ pip3 install --ignore-installed -r requirements.txt -e ".[dev]"
```

## Usage



## Contributing

Contributions are warmly welcomed.  A development dependency environment can be installed in editable mode with the developer installation documentation above.

Please use the standard Github pull request approach to propose source changes.

### Source file linting

Python source files are linted with `flake8`.  See the Makefile `test-lint` target for details.

### Testing

The project runs continuous integration testing on the GitHub Actions service with the `pytest` toolchain.  Test modules are located in the `tests` directory of the repository.

Local testing by Python interpreter version can be performed with the following command executed from the root of the repository:

```
$ tox -e [PYTHON INTERPRETER VERSION]
```

Please see the `tox` documentation for additional details.

### Test coverage

Unit test coverage is executed with the `coverage` tool.  See the Makefile `test-coverage` target for details.

## Acknowledgments

panosifier is built with the fantastic free [fonttools](https://github.com/fonttools/fonttools) Python library.

## License

[Apache License v2.0](https://github.com/source-foundry/panosifier/blob/main/LICENSE)