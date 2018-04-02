Testing https://youtrack.jetbrains.com/issue/PY-28457

Steps to reproduce:

1. start debug server
2. edit someapp/views.py (add or remove a comment in the index function)
3. hit Ctrl+S to save

Result: "Process finished with exit code 139 (interrupted by signal 11: SIGSEGV)"

Debian 9
Python 3.5.3
Pycharm 2018.1
