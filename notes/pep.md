# PEP

## String

If string contains single-quote characters, it's recommended that you use double-quoted strings `comment = "I'm Yuki"`.

If string contains double-quote characters, it's recommended that you use single-quoted strings `comment = 'He said "Hello".'`

## Docstring

`__doc__` attribute, any string literals after the definition of a function/module/class/method

`help(object)`

Module docstring should list classes, exceptions, and functions with one-line summary of each.

Function docstring should summarize its behaviour, and document arguments, returned value, side effects, exceptions, and
restrictions when it's called.

Class docstring should summarize the behavior and purpose, not provide detailed listing of methods and attributes.

## Linter

Tool to help you write your code and analyze it for any stylistic anomalies and programming errors against a set of pre-
defined rules.

Flake8, Pylint, Pyflakes, Pychecker, Mypy, Pycodestyle

## Fixer

Program to fix coding issues and format to be consistent with the standard

Black, YAPF, autopep8

