#!/usr/bin/python3
""" Script that takes two arguments for markdown engine
    Arguments
    =========
        First argument is the name of the Markdown file
        Second argument is the output file name
"""
from os.path import exists
from sys import argv, stderr

if __name__ == "__main__":
    if len(argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=stderr)
        exit(1)
    else:
        if not exists(argv[1]):
            print(f"Missing {argv[1]}", file=stderr)
            exit(1)
        else:
            print(end="")
            exit(0)
