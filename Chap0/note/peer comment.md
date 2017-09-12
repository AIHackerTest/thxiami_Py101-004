## 做帮别人挠痒痒的猴子——Vwan作业点评

根据 [Python 课程同学自评、互评参考维度](https://github.com/AIHackers/Py101-004/wiki/HbHackerStyle) 结合代码考察

### 闪光点
- Vwan 自行探索 timeit 和 cprofile 模块，为了测试不同同学随数生成函数的效率
  - 比较用代码文件： [compare_perf_for_Generate_Num_Function](https://github.com/Vwan/Py101-004/blob/master/Chap0/project/BullsAndCows/compare_perf_for_Generate_Num_Function.py)
  - 比较过程记录：[设计与实现](https://github.com/Vwan/Py101-004/blob/master/Chap0/note/Execise_Notes_chp0.md#设计与实现)
  - 通过该文件，我也测试了自己的随机数生成函数，发现完败:
    - 用时：Vwan 0.013s 左右；自己 0.020s 左右
    - 调用函数数量：Vwan < 自己

- 总结记录自己学 Python 遇到的知识点，环境配置，有用文档和工具，可以借鉴学习，形成自己的备忘录
  - [Learning Notes_ch0](https://github.com/Vwan/Py101-004/blob/master/Chap0/note/Learning%20Notes_chp0.md)

### 代码中的问题

- [猜字游戏基础版](https://github.com/Vwan/Py101-004/blob/master/Chap0/project/BullsAndCows/bulls_and_cows.py) 只记录了用户输入次数，忘了写判定次数的代码

### 一些建议

- 文件开头可添加python环境编码格式、作者、版本、编辑日期[0]
    ```python
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    ```
    第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
    第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码[1]。
     ```python
    """
    Program name: Bulls And Cows Advanced Edition
    Author: thxiami
    Github: https://github.com/thxiami/
    Edition：v1.0
    Edit date: 2017.08.14
    """
     ```

- [猜字游戏进阶版](https://github.com/Vwan/Py101-004/blob/master/Chap0/project/BullsAndCows/bulls_and_cows_advanced.py)
  - **变量命名**：`counta` 可改为`count_of_a`，更清晰易懂
  - **代码可读性**:
  ```python
    def verify_number(n1,n2):
        if (n1 == n2):
            return len(str(n1)),0
        else:
            numlist1 = [int(i) for i in str(n1)]
            numlist2 = [int(i) for i in str(n2)]
            numlist = [x - y for x,y in zip(numlist1,numlist2)]
            counta = numlist.count(0)
            return counta,len(set(numlist1) & set(numlist2)) - counta
  ```
    最后两行可改为， 这样就能直接就看出来函数返回了哪两个变量
    ```python
    count_of_b = len(set(numlist1) & set(numlist2)) - count_of_a
    return count_of_a, count_of_b
    ```
    - **docstring & comment** :如果有函数，可适当添加一些 docstring & comment，别人看到docstring 就能知道你的函数的功能，传入参数的类型和含义，返回变量的类型和含义。参考资料有：
    - [注释与docstring](http://python-web-guide.readthedocs.io/zh/latest/codingstyle/codingstyle.html#id21) 作者给出了他推崇的一种 google 的 docstring 示例以及他对于注释的理解
      - [What is the standard Python docstring format?](https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format)Stack Overflow上一个回答
      - [PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/) Python 官方关于 docstring 的增强技术规范
      - [Example Google Style Python Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

### Reference
- [0] [Python 课程同学自评、互评参考维度](https://github.com/AIHackers/Py101-004/wiki/HbHackerStyle)
- [1] [廖雪峰的Python教程-字符串和编码](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431664106267f12e9bef7ee14cf6a8776a479bdec9b9000)