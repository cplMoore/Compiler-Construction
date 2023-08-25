# COMP 5210 Compiler Construction project.
# Author: Jacob Moore jwm0083.
# Author: Ben Hulsey bph0022.

from typing import NamedTuple
import re

# Recognize tokens print out tokens and put them in a tokenizer.py file.
# Class and tokenize method was used from https://docs.python.org/3/library/re.html?highlight=regular%20expression.
class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int

def tokenize(code):
