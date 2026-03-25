#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
to_ansi.py - Convert MirServer script files to ANSI (GBK) encoding
Usage:
  python to_ansi.py <file_or_dir>   # convert single file or whole directory
  python to_ansi.py                 # convert default D:\MirServer\Mir200\Envir
"""

import sys
import os
import chardet

TARGET_EXTS = {'.txt', '.ini'}

def detect_encoding(filepath):
    with open(filepath, 'rb') as f:
        raw = f.read()
    if not raw:
        return 'gbk', raw
    # BOM check
    if raw[:3] == b'\xef\xbb\xbf':
        return 'utf-8-sig', raw
    if raw[:2] == b'\xff\xfe':
        return 'utf-16-le', raw
    if raw[:2] == b'\xfe\xff':
        return 'utf-16-be', raw
    # chardet detect
    result = chardet.detect(raw)
    enc = (result.get('encoding') or 'gbk').lower()
    conf = result.get('confidence', 0)
    # If chardet says ascii or gbk/gb2312/gb18030 -> already ANSI, skip
    if enc in ('ascii', 'gbk', 'gb2312', 'gb18030', 'big5', 'hz'):
        return enc, raw
    # If detected utf-8 with high confidence, convert
    if 'utf-8' in enc and conf > 0.7:
        return enc, raw
    # Default: treat as GBK (already ANSI)
    return 'gbk', raw

def convert_to_ansi(filepath):
    enc, raw = detect_encoding(filepath)
    norm = enc.replace('-', '').lower()
    # Already GBK/ANSI family -> skip
    if norm in ('gbk', 'gb2312', 'gb18030', 'ascii', 'big5', 'hz'):
        print(f'[SKIP]    Already ANSI: {filepath}')
        return False
    try:
        text = raw.decode(enc, errors='replace')
        new_bytes = text.encode('gbk', errors='replace')
        with open(filepath, 'wb') as f:
            f.write(new_bytes)
        print(f'[CONVERT] {enc} -> GBK: {filepath}')
        return True
    except Exception as e:
        print(f'[ERROR]   {filepath}: {e}')
        return False

def process_path(path):
    converted = 0
    skipped = 0
    if os.path.isfile(path):
        if convert_to_ansi(path):
            converted += 1
        else:
            skipped += 1
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for fname in files:
                ext = os.path.splitext(fname)[1].lower()
                if ext in TARGET_EXTS:
                    fp = os.path.join(root, fname)
                    if convert_to_ansi(fp):
                        converted += 1
                    else:
                        skipped += 1
    print(f'\nDone: converted={converted} skipped={skipped}')

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else r'D:\MirServer\Mir200\Envir'
    print(f'Target: {target}')
    process_path(target)
