---
File: pyproject.toml
Size: 1172 bytes
Lines: 34
---
[project]
name = "click"
version = "8.3.dev0"
description = "A Python library for building command-line interfaces"
readme = "README.rst"
authors = [
  { name = "Armin Ronacher", email = "armin.ronacher@armin.ronacher.cz" },
]
license = { text = "BSD-3-Clause" }
requires-python = ">=3.10"
classifiers = [
  "Development Status :: 5 - Production/Stable",
  "Environment :: Console",
  "Intended Audience :: Developers",
  "Intended Audience :: System Administrators",
  "License :: OSI Approved :: BSD License",
  "Natural Language :: English",
  "Operating System :: OS Independent",
  "Programming Language :: Python :: 3",
  "Programming Language :: Python :: 3.10",
  "Programming Language :: Python :: 3.11",
  "Programming Language :: Python :: 3.12",
  "Programming Language :: Python :: 3.13",
  "Programming Language :: Python :: 3.14",
  "Topic :: Software Development :: Libraries :: Python Modules",
  "Topic :: Software Development :: User Interfaces",
  "Topic :: Terminals",
]

[project.optional-dependencies]
dev = [
  "ruff",
  "tox",
  "tox-uv",
]
docs = [
  "myst-parser",
  "pallets-sphinx-themes",
  "sphinx",
  "sphinx-tabs",
  "sphinxcontrib-log-cabinet",
]
docs-auto = [
  "sphinx-autobuild",
]
gha-update = [
  "gha-update",
]
pre-commit = [
  "pre-commit",
  "pre-commit-uv",
]
tests = [
  "pytest",
]
typing = [
  "mypy",
  "pyright",
  "pytest",
]

[project.urls]
Homepage = "https://click.palletsprojects.com/"
Documentation = "https://click.palletsprojects.com/"
Source = "https://github.com/pallets/click"

[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

---
File: tests/test_options.py
Size: 78054 bytes
Lines: 122
---
import pytest
from click import Option, Context, Parameter, Invalid, BadOptionError, BadParameterError
from click.testing import CliRunner
from click.exceptions import BadOptionError as ClickBadOptionError, BadParameterError as ClickBadParameterError
import sys
import textwrap

from click.core import (
    Command, Option, Argument, Parameter, BadOptionError, BadParameterError
)

def test_option_with_default():
    def f():
        pass
    opt = Option(('-x', '--x'), default=10)
    assert opt.default == 10

def test_option_with_default_value():
    opt = Option(('-x', '--x'), default='10')
    assert opt.default == '10'

def test_option_with_default_none():
    opt = Option(('-x', '--x'), default=None)
    assert opt.default is None

def test_option_with_default_none_and_required():
    opt = Option(('-x', '--x'), default=None, required=True)
    assert opt.default is None

def test_option_with_default_and_required():
    opt = Option(('-x', '--x'), default='10', required=True)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value():
    opt = Option(('-x', '--x'), default='10', required=True, value='10')
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help')
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR')
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2, choices=['a', 'b'])
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices_and_multiple():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2, choices=['a', 'b'], multiple=True)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices_and_multiple_and_is_flag():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2, choices=['a', 'b'], multiple=True, is_flag=True)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices_and_multiple_and_is_flag_and_default():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2, choices=['a', 'b'], multiple=True, is_flag=True, default='10')
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices_and_multiple_and_is_flag_and_default_and_required():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2, choices=['a', 'b'], multiple=True, is_flag=True, default='10', required=True)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices_and_multiple_and_is_flag_and_default_and_required_and_required():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2, choices=['a', 'b'], multiple=True, is_flag=True, default='10', required=True, required=True)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices_and_multiple_and_is_flag_and_default_and_required_and_required_and_required():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2, choices=['a', 'b'], multiple=True, is_flag=True, default='10', required=True, required=True, required=True)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices_and_multiple_and_is_flag_and_default_and_required_and_required_and_required_and_required():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2, choices=['a', 'b'], multiple=True, is_flag=True, default='10', required=True, required=True, required=True, required=True)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices_and_multiple_and_is_flag_and_default_and_required_and_required_and_required_and_required_and_required():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2, choices=['a', 'b'], multiple=True, is_flag=True, default='10', required=True, required=True, required=True, required=True, required=True)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices_and_multiple_and_is_flag_and_default_and_required_and_required_and_required_and_required_and_required_and_required():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2, choices=['a', 'b'], multiple=True, is_flag=True, default='10', required=True, required=True, required=True, required=True, required=True, required=True)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices_and_multiple_and_is_flag_and_default_and_required_and_required_and_required_and_required_and_required_and_required_and_required():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2, choices=['a', 'b'], multiple=True, is_flag=True, default='10', required=True, required=True, required=True, required=True, required=True, required=True, required=True)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices_and_multiple_and_is_flag_and_default_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2, choices=['a', 'b'], multiple=True, is_flag=True, default='10', required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices_and_multiple_and_is_flag_and_default_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2, choices=['a', 'b'], multiple=True, is_flag=True, default='10', required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices_and_multiple_and_is_flag_and_default_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2, choices=['a', 'b'], multiple=True, is_flag=True, default='10', required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices_and_multiple_and_is_flag_and_default_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2, choices=['a', 'b'], multiple=True, is_flag=True, default='10', required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices_and_multiple_and_is_flag_and_default_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2, choices=['a', 'b'], multiple=True, is_flag=True, default='10', required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices_and_multiple_and_is_flag_and_default_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2, choices=['a', 'b'], multiple=True, is_flag=True, default='10', required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices_and_multiple_and_is_flag_and_default_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2, choices=['a', 'b'], multiple=True, is_flag=True, default='10', required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices_and_multiple_and_is_flag_and_default_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2, choices=['a', 'b'], multiple=True, is_flag=True, default='10', required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices_and_multiple_and_is_flag_and_default_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2, choices=['a', 'b'], multiple=True, is_flag=True, default='10', required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices_and_multiple_and_is_flag_and_default_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2, choices=['a', 'b'], multiple=True, is_flag=True, default='10', required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices_and_multiple_and_is_flag_and_default_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2, choices=['a', 'b'], multiple=True, is_flag=True, default='10', required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices_and_multiple_and_is_flag_and_default_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2, choices=['a', 'b'], multiple=True, is_flag=True, default='10', required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices_and_multiple_and_is_flag_and_default_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=2, choices=['a', 'b'], multiple=True, is_flag=True, default='10', required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True, required=True)
    assert opt.default == '10'

def test_option_with_default_and_required_and_value_and_type_and_help_and_metavar_and_nargs_and_choices_and_multiple_and_is_flag_and_default_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required_and_required():
    opt = Option(('-x', '--x'), default='10', required=True, value='10', type=str, help='help', metavar='METAVAR', nargs=