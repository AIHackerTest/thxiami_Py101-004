# ex11- input

"""
Python 2 中的函数 raw_input()和 input()，其中：
raw_input() 将用户输入以字符串类型保存；
input() 会将用户输入当做代码来执行，会有一定的安全问题；

Python 3 中使用 input() 代替 raw_input()
"""
print('How old are you?')
age = input(' >')
print('How tall are you?')
height = input(' >')
print('How much do you weigh?')
weight = input(' >')

print(F"so, you're {age!r} old, {height!r} tall and {weight!r} heavy.")


"""
原书中有个 note ：
注意到我在每行  print  后面加了个逗号 (comma) ,  了吧？这样的话  print  就不会输出新行符而结束
这一行跑到下一行去了。
自己实践时候发现：python3.6中无法生效，会有换行
"""