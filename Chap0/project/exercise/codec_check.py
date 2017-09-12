
"""
import chardet
with open ('test.txt', 'rb') as f:
    s = f.read()

chatest = chardet.detect(s)

print(chatest)
"""
import sys

print('sys.stdin.encoding:', sys.stdin.encoding)
print('sys.stdout.encoding:', sys.stdout.encoding)
print('sys.getdefaultencoding():', sys.getdefaultencoding())