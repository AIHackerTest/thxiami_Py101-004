#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
How to make a interactive program?
- Read
- Eval
- Print
- Loop

Discoverablity
User focus
Configurablity

Check List
- Persistent history
- History search
- Emacs Keybingdings
- Paged Output
- Auto-Completion
- Minimal Config
- Syntax Coloring

"""

import prompt_toolkit
from prompt_toolkit import prompt

while 1:
    inp = prompt('>')
    print(inp)