# ex6 - Format string

num = 10

# 在 python2.x 和 3.x 中均可使用第 1 种方式格式化字符串
# 在 python2.6 中新增第 2 种方式格式化字符串
# 在 python3.6 中新增第 3 种方式格式化字符串
x = "There are %d types of people." % num
x1 = "There are {} types of people.".format(num)
x2 = f"There are {num} types of people."

print('python2.x &3.x:\n', x)
print('python2.6:\n', x1)
print('python3.6:\n', x2)

binary = "binary"
do_not = "don't"

# 在 python2.x 和 3.x 中均可使用第 1 种方式格式化字符串
# 在 python2.6 中新增第 2 种方式格式化字符串
# 在 python3.6 中新增第 3 种方式格式化字符串
y = "Those who know %s and those who %s." % (binary , do_not)
y1 = "Those who know {} and those who {}.".format(binary , do_not)
y2 = f"Those who know {binary} and those who {do_not}."

print('python2.x &3.x:\n', y)
print('python2.6:\n', y1)
print('python3.6:\n', y2)


print("I said: {!s}".format(x))
print("I said: {!r}".format(x))
print("I also said: '{!s}'".format(y))

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {!r}"

print(joke_evaluation.format(hilarious))
w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)