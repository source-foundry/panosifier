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

In many cases, you can define these values in your type design source files and rely on the font compiler to write these values into your font instances. However, there are situations where this behavior is not well-defined and differs across font compilers.  

An example is the approach to panose data writes in variable font format files.  In this case, the OpenType specification is vague, environments where these data are essential are not well-defined, and compilers handle the source file defined panose data differently.  

This tool allows you to modify build-time decisions in these situations.

## Quick Start

- Install in a Python 3.6+ virtual environment with `pip install panosifier`
- Define your panose values with a comma-delimited panose value list using the `--panose` command line option or individually with the ten available OpenType panose field options (see `panosifier --help` for a list of available options)

See the documentation below for additional details.

## Installation

This project requires a Python 3.6+ interpreter.

We recommend installation in a Python3 virtual environment.

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

panosifier supports two command line approaches to edit panose data in one or more command line defined font paths:

1. Define all 10 OpenType panose fields with an ordered comma-delimited list of integers with the `--panose` option
2. Define with individual command line options for one or more of the 10 OpenType panose fields

### Comma-delimited list definition

You can define all panose fields at once with an ordered,  comma-delimited list of all 10 OpenType panose values.  These must be integer values.  

The field order is:

1. FamilyType
2. SerifStyle
3. Weight
4. Proportion
5. Contrast
6. StrokeVariation
7. ArmStyle
8. LetterForm
9. Midline
10. XHeight

The following image exemplifies this order in the `--panose` option definition idiom.  Note that the values in this example are not intended to be valid for a font, but rather to demonstrate how the definition order maps to panose definition fields.

<img src="https://user-images.githubusercontent.com/4249591/97115080-ed937180-16ca-11eb-8d3f-ce9d43766f21.png" >

### Individual panose field options

There are ten available OpenType panose definitions.  Each panose field has a corresponding option in the panosifier tool.  These options allow you to define each field individually and make panose definitions explicit in scripted build workflows.  Define these options with integer values.

The example below modifies the panose data write in the comma-delimited list section above with new FamilyType and Proportion values of 2 and 9, respectively:

<img src="https://user-images.githubusercontent.com/4249591/97115146-609ce800-16cb-11eb-82fd-d74e5d846060.png" >

Use `panosifier --help` to view all available options.

**Note**: This tool does not perform sanity checks on your definitions and can be used to write invalid definitions in fonts.  The tool assumes that you understand how to set these panose values.  Please refer to the [panose documentation](https://monotype.github.io/panose/pan1.htm) for detailed background.

### Reporting

panosifier reports panose data definitions in the standard output stream at the end of execution.

## Contributing

Contributions are warmly welcomed.  A development dependency environment can be installed in editable mode with the developer installation documentation above.

Please use the standard Github pull request approach to propose source changes.

### Source file linting

We lint Python source files with `flake8`.  See the Makefile `test-lint` target for details.

### Testing

Continuous integration testing is performed on the GitHub Actions service with the `pytest` toolchain.  Test modules are located in the `tests` directory of the repository.

Perform local Python interpreter version testing with the following command executed from the root of the repository:

```
$ tox -e [PYTHON INTERPRETER VERSION]
```

Please see the `tox` documentation for additional details.

### Test coverage

We perform unit test coverage testing with the `coverage` tool.  See the Makefile `test-coverage` target for details.

## Acknowledgments

panosifier is built with the fantastic free [fonttools](https://github.com/fonttools/fonttools) Python library.

## License

[Apache License v2.0](https://github.com/source-foundry/panosifier/blob/main/LICENSE)