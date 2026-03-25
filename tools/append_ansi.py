#!/usr/bin/env python3
"""
append_ansi.py - Append text content to a file in ANSI (GBK) encoding
Usage: python append_ansi.py <filepath> <content>
       python append_ansi.py <filepath> -  (read content from stdin)
"""
import sys
import os

def append_ansi(filepath, content):
    os.makedirs(os.path.dirname(os.path.abspath(filepath)), exist_ok=True)
    with open(filepath, 'a', encoding='gbk', errors='replace') as f:
        f.write(content)
    print(f'[OK] Appended GBK: {filepath}')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python append_ansi.py <filepath> <content_or_->')
        sys.exit(1)
    fp = sys.argv[1]
    if sys.argv[2] == '-':
        content = sys.stdin.read()
    else:
        content = sys.argv[2]
    append_ansi(fp, content)
