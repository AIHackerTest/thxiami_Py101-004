### 目录下文件说明

- exercise 文件夹下为使用 Python 3 完成的 LPTHW 的 7 个练习，结合 Python 2 和 3 的一些差异完成
- [guess_easy.py](https://github.com/thxiami/Py101-004/blob/master/Chap0/project/guess_easy.py) 为猜数字游戏基础版的 py 文件
- [guess_hard.py](https://github.com/thxiami/Py101-004/blob/master/Chap0/project/guess_hard.py) 为猜数字游戏升级版的 py 文件

### 猜数字游戏程序使用说明

- 猜数字游戏基础版
    - 程序随机生成一个 20 以内的数字，用户有 10 次机会猜测
    - 用户可能输入数字或其他字符，当输入含有非数字时，程序会提示用户重新输入；若输入仅包含数字，程序会根据输入给予一定提示 （大了、小了、正确）
    - 猜对或用完 10 次机会，游戏结束

- 猜数字游戏基础版
	- 程序内部用 0-9 生成一个 4 位数，每个数位上的数字不重复，且首位数字不为零，如 1942
	- 用户可以输入 4 位数进行猜测，当输入含有非数字或不是4位数时，程序会提示用户重新输入；若输入仅包含数字，程序返回相应提示：
        - 用 A 表示数字和位置都正确，用 B 表示数字正确但位置错误
        - 用户猜测后，程序返回 A 和 B 的数量
        - 比如：2A1B 表示用户所猜数字，有 2 个数字，数字、位置都正确，有 1 个数字，数字正确但位置错误
    - 猜对或用完 10 次机会，游戏结束

## 版本更新记录
### 0 guess_easy.py
- 170813
	-  `play()` 函数，原代码会使用户可以猜 11 次，解决了这个 bug
- 170809 ~ 170810
	- docstring & comment 创建及修改

### 1 guess_hard.py
- 170814 
	- 将变量名中的大写字母修改为小写字母
 	- 单元测试函数中增加了输出，方便判断是否通过测试及快速定位出错函数
 	- `generate_randnum()` 函数后3位数字生成部分代码修改
```python
optional_numbers = [str(i) for i in range(10)]
first_num = optional_numbers.pop(randint(1, 9))
# 原代码：three_num_ls = [str(i) for i in sample(optional_numbers, 3)]
three_num_ls = sample(optional_numbers, 3)
```

- 170813 
	- `play()` 函数，原代码会使用户可以猜 11 次，解决了这个 bug
- 170812 
	- `generate_randnum()` 函数 生成随机数后3位的方案使用了同学的 random.sample() 函数