HDE Challenge
=============

Environment specification
-------------------------
For Python:
    - Python 3+.
    - It can still run with Python2+, but the following changes need to be done.
        - Replace all ``input()`` to ``raw_input()``.
        - Add ``from __future__ import print_function()`` at the beginning
          of the file.

For C:
    - The code is following the C99 standard.


Solutions
---------
- ``recursive.py``: Python recursive version.
- ``functional.py``: Python functional version.
- ``oneline.py``: Python with one-line version. (Shortest)
- ``ctypes_ver.py``: Python with ``ctypes`` module to call shared library
  version. The shared library can be compiled with ``make``.
- ``recursive.c``: C version. You can compile it with ``make``.

