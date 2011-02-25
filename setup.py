from setuptools import setup

__author__ = "Christopher Bertels"

setup(
    name='Fancy Pygments Lexer',
    version='1.0',
    description='Pygments Lexer for the Fancy Programming Language',
    packages=['fancy_pygments'],
    install_requires=['pygments'],
    entry_points='''
[pygments.lexers]
fancy = fancy_pygments:fancy_lexer.FancyLexer
'''
)
