#!/usr/bin/env python
"""Simple script to run Idle from a venv in PyCharm."""
# Import for Python pre 3.6
try:
    from idlelib.PyShell import main
# Import for Python version 3.6 and later
except ModuleNotFoundError:
    from idlelib.pyshell import main

if __name__ == '__main__':
    main()
