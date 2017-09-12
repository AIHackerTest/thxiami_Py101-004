# ex3 calculation
"""
在 Python 2 中, 两个 int 类型的数使用 '/' 相除会得到结果的整数部分，如：5 / 2 == 2；
但是从 Python 2.2 开始，关于除法运算的改变就纳入计划，所以自那时开始，
将 'from __future__ import division' 该行代码添加至文件中（在除法运算之前）,可以得到： 
        5 / 2 == 2.5
        5 // 2 == 2
在 Python 3 中，默认 '/'  和 '//' 的作用同上，即：
        '/' 得到的结果类型为 float； 
        '//'得到的结果类型为 int。
"""

print('I will now conut my chickens:')
print('Hens', 25 + 30// 6)
print('Roosters', 100 - 25 * 3 % 4)

print('Now I will count the eggs:')

print(3 + 2 + 1 - 5 + 4 % 2 - 1 // 4 + 6)

print('Is it true that 3 + 2 < 5 - 7?')
print(3 + 2 < 5 - 7)

print("Oh, that's why it's False.")

print('How about some more.')

print('Is it greater?', 5 > -2)
print('Is it greater or equal?', 5 <= -2)
print('Is it less or equal?', 5 <= -2)