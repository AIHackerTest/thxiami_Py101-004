# Git 操作指南
- git 更改远程/本地仓库文件夹名
```
git mv old_folder_name new_foler_name
git commit -m "Change folder name"
git push origin <your-git-branch> (typically 'master', but not always)
```
- git 删除本地和远程仓库文件夹
```
git rm -r one-of-the-directories
git commit -m "Remove duplicated directory"
git push origin <your-git-branch> (typically 'master', but not always)
```

- git 删除远程仓库文件夹
```
git rm -r --cached FolderName
git commit -m "Removed folder from repository"
git push origin <your-git-branch> (typically 'master', but not always)
```

- git 创建远程和删除分支
    ```
    git checkout -b dev_local # 在本地创建一个分支（基于当前所处的分支的文件啥的），并转到该分支上
    git push origin dev_local:dev_remote # 把 dev_local 推送到 dev_remote，远程没有该分支所以就创建了新分支

    git push origin :dev_remote # 给远程 dev_remote 分支推送了一个 空分支，等于删除了远程分支
    ```

- git 创建和远程关联的本地分支分支
    - 在本地创建和远程分支对应的分支，使用`git checkout -b branch-name origin/branch-name`，本地和远程分支的名称最好一致；

    - 建立本地分支和远程分支的关联，使用
        - 快过时的方法：`git branch --set-upstream branch-name origin/branch-name`；
        - 在需要建立关联的本地分支下, `git branch --set-upstream-to origin/branch-name`


- git 撤销修改
  - 迅速上手
        - 场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令`git checkout -- file`。

        - 场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令`git reset HEAD file`就回到了场景1，第二步按场景1操作。

        - 场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考版本回退一节，不过前提是没有推送到远程库。
        - `git reset --hard` 版本回退至最近一次commit id对应的版本，适合所有修改都需要撤销的时候

    > If you are at the root of your working directory, you can do `git checkout --` . to check-out all files in the current HEAD and replace your local files.

    > You can also do `git reset --hard` to reset your working directory and replace all changes (including the index).

  - 文档进一步详细阅读
    - [Reset Demystified](https://git-scm.com/blog/2011/07/11/reset.html)

- Git 变更指令名，缩短常用指令名
  - 参考廖雪峰网站教程修改 git命令，使更短。
  - 修改的命令：`git config --global alias.st status`
  - 效果: `git status` -> `git st`
  - 其他：
        - `git commit -m ""` -> `git ci -m ""`
        - `git reset HEAD filename` -> `git unstage filename` 从工作区撤销 add


# Lambda 
挖坑待补

# Recursion
## 0 什么是递归，为什么用递归（与循环比）？
[wisc大学cs课程教案](http://pages.cs.wisc.edu/~vernon/cs367/notes/6.RECURSION.html) 讲的很清楚，配以例子来讲解理论，适合入门者。摘录总结两部分：
- **rules of recursive method**
    - Remember that every recursive method must have a base case (rule #1).
    - Also remember that every recursive method must make progress towards its base case (rule #2).
    - Sometimes a recursive method has more to do following a recursive call. It gets done only after the recursive call (and all calls it makes) finishes.

- **when it is a good idea to use recursion and why**
  Now let's think about when it is a good idea to use recursion and why. In many cases there will be a choice: many methods can be written either with or without using recursion.

    Q: Is the recursive version usually faster?
    A: No -- it's usually slower (due to the overhead of maintaining the stack)
    Q: Does the recursive version usually use less memory?
    A: No -- it usually uses more memory (for the stack).

    Q: Then why use recursion?
    A: Sometimes it is much simpler to write the recursive version. Use recursion for **clarity**, and (sometimes) for a reduction in the time needed to write and debug code, not for space savings or speed of execution.


## 1 尾递归（tail recursion）又是什么？和一般递归的差异？

### 1.1 定义
In **traditional recursion**, the typical model is that you perform your recursive calls first, and then you take the return value of the recursive call and calculate the result. In this manner, you don't get the result of your calculation until you have returned from every recursive call.

In **tail recursion**, you perform your calculations first, and then you execute the recursive call, passing the results of your current step to the next recursive step. This results in the last statement being in the form of "(++return (recursive-function params++))" (I think that's the syntax for Lisp). **Basically, the return value of any given recursive step is the same as the return value of the next recursive call.**

上面划线处对应 Python 内应该是这个意思
```python
def fun(param):
	...
    return fun(do something with param) # e.g. return fun(param - 1)
```
The consequence of this is that once you are ready to perform your next recursive step, you don't need the current stack frame any more. This allows for some optimization. In fact, with an appropriately written compiler, you should never have a stack overflow snicker with a tail recursive call. Simply reuse the current stack frame for the next recursive step. I'm pretty sure Lisp does this.

### 1.2 实例



- **一般递归**

    Consider a simple function that adds the first N integers. (e.g. sum(5) = 1 + 2 + 3 + 4 + 5 = 15).

    Here is a simple Python implementation that uses recursion:

    ```python
    def recsum(x):
        if x == 1:
            return x
        else:
            return x + recsum(x - 1)
    ```
    If you called recsum(5), this is what the Python interpreter would evaluate.
    ```python
    recsum(5)
    5 + recsum(4)
    5 + (4 + recsum(3))
    5 + (4 + (3 + recsum(2)))
    5 + (4 + (3 + (2 + recsum(1))))
    5 + (4 + (3 + (2 + 1)))
    15
    ```
    Note how every recursive call has to complete before the Python interpreter begins to actually do the work of calculating the sum.

- **尾递归**

    Here's a tail-recursive version of the same function:
    ```python
    def tailrecsum(x, running_total=0):
        if x == 0:
            return running_total
        else:
            return tailrecsum(x - 1, running_total + x)
    ```
    Here's the sequence of events that would occur if you called tailrecsum(5), (which would effectively be tailrecsum(5, 0), because of the default second argument).
    ```python
    tailrecsum(5, 0)
    tailrecsum(4, 5)
    tailrecsum(3, 9)
    tailrecsum(2, 12)
    tailrecsum(1, 14)
    tailrecsum(0, 15)
    15
    ```
    In the tail-recursive case, with each evaluation of the recursive call, the running_total is updated.

    Note: **As mentioned in the comments, Python doesn't have built-in support for optimizing away tail calls, so there's no advantage to doing this in Python.** However, you can use a decorator to achieve the optimization.（decorator 这个不懂）

### 1.3 个人理解

尾递归是递归中的一种，其实现特点是：

- 最后一句代码形式为： `return recursionfunction(do some thing with param)`，即当下层函数调用被返回至本层时，不再执行其他的代码，直接返回上层函数，层层如此
- 每一步都先完成计算，然后把这一步计算的结果作为参数传给下一步
- 尾递归的计算结果不需要依靠栈中先调用的函数存储的变量等信息，仅通过本次函数的变量值就能完成计算。因此一些语言中会对尾递归作优化，应该是对栈中保存的先调用的函数相关信息进行了消除，节省空间
- Python 中默认没有对尾递归作优化 ,因此在Python中使用尾递归不能解决占用空间的问题。但也有一定办法实现尾递归优化，关于为何默认不优化以及DIY优化方法参见 [Guido's blog:Tail Recursion Elimination](http://neopythonic.blogspot.jp/2009/04/tail-recursion-elimination.html)。

## 2 个人总结

### 2.1 评价递归
- 健壮性(Robustness)
    - 根据搜索，代码的健壮性主要指其面对各种异常情景时能否正常处理，输出出错信息。递归会存在栈溢出的潜在问题（学术名词: stack overflow ,这个名词我也不是特别懂，应该跟记录函数运行的记录有关），当递归次数超过一定数量时（我这里默认1000次，使用`sys.getrecursionlimit()`查看），程序会被终止，并抛出 1 个异常:`RuntimeError: maximum recursion depth exceeded` 。因此，当不确定函数需要调用的次数时，这会影响程序运行的稳定性。如果直至报错，递归仍然没有获得结果，那这时的代码就不够健壮，不如使用循环。
- 效率
    - 写代码的效率：递归更接近于一些算法问题的描述，比如（阶乘，斐波那契数列），相对循环来说更容易编写，出问题时也容易 debug
    - 运行效率：递归的速度（一般情况）会比循环要慢,占用内存更多（[Python中没有对尾递归进行优化](http://neopythonic.blogspot.jp/2009/04/tail-recursion-elimination.html)，即便使用尾递归也不能缓解内存占用的问题）。但在某一些问题上，改变递归的实现方式（结合一些数据结构），会给速度带来提升，甚至速度比循环更快(例子可参见: [Recursive Functions](http://www.python-course.eu/recursive_functions.php))
- 可读性
  - 算法问题：一般来说，递归更易读，易 debug
  - ch0，ch1 作业中的获得用户输入的问题：对初学者，递归可读性比循环差
- 其他可能发生的问题
  - 目前不知道


### 2.2 Recuision or Loop
根据上面分析的递归的优劣，阅读好几个类似问题下的答案，基本上大家的观点都比较一致：
- 一个算法如果能通过递归实现，循环也可以实现
- 当递归易写但低效时，那么选择哪种方法解决问题，其实就是选择花更多的时间用 loop 实现，还是花更多的钱提升机器性能

## 3 Reference
- [wisc大学cs课程教案](http://pages.cs.wisc.edu/~vernon/cs367/notes/6.RECURSION.html)
- [Guido's blog:Tail Recursion Elimination](http://neopythonic.blogspot.jp/2009/04/tail-recursion-elimination.html)
- [Recursive Functions](http://www.python-course.eu/recursive_functions.php)
- [What are the advantages and disadvantages of recursion?](https://stackoverflow.com/questions/5250733/what-are-the-advantages-and-disadvantages-of-recursion) 
- [recursion versus iteration](https://stackoverflow.com/questions/15688019/recursion-versus-iteration)

## map()
[一篇博客讲如何用map()，并且与列表推导式对比](https://my.oschina.net/zyzzy/blog/115096)

## 函数可传入的几种参数
- 必选参数	
```python
def func(name):
  pass
```

- 默认参数

  ```python
  def func(name='li', age=24):
  	print('name:', name, 'age:', age)
    
  dt = dict(name='xiami', age=23)
  func('xiami', 25)  # name: xiami age: 25
  func(23, 'xiami')  # name: 23 age: xiami
  func(**dt)  # name: xiami age: 23
  ```

- 可变参数

  - 函数定义时, 使用 `*args`将传入的参数打包为tuple, 可传入不定数量的参数
  - 函数调用时, 使用 `*ls` 可以将 ls(类型为list or tuple) 内全部参数传入

  ```python
  def func(*args):
    print('args:', args, type(args))
    for i in args:
      print(i)
      

  func('xiami', 24)
  """
  结果：
  args:('xiami', 24) <class 'tuple'>
  xiami
  24
  """

  ls = [1,2,3]
  func(ls)
  """
  结果：
  args:([1, 2, 3],) <class 'tuple'>  # 注意仅有 1 个元素的 tuple的写法
  [1, 2, 3]
  """

  func(*ls)
  """
  结果：
  args:(1, 2, 3) <class 'tuple'>
  1
  2
  3
  """
  ```

  ​

- 关键字参数

  - 函数定义时, 使用 `**kwargs` 将传入的参数打包为 `dict`, 可传入不定数量的参数
  - 函数调用时, 使用 `*dt` 可以将 `dt`(类型为`dict`)内全部键值对传入

  ```python
  def func(name,**kwargs):
      print('name:', name, 'kwargs:', kwargs)

  dt = dict(age=23)
  func('xiami', age=23)  # name: xiami kwargs: {'age': 23}
  func('xiami', **dt)  # name: xiami kwargs: {'age': 23}
  ```

  ​

- 命名关键字参数

  - 使用关键字参数可以传入不定数量的变量,但如果希望传入指定参数名的变量,需要使用到命名关键字参数

    ```python
    def func(name, *, age):
        print('name:', name, 'age:', age)


    def func2(name, *args, age):
        print('name:', name, 'age:', age, 'args', args)


    dt = dict(age=23, score=60)
    func('xiami', score=60)  # 会报错，提示 TypeError: func() got an unexpected keyword argument 'score'
    func('xiami', age=23)  # name: xiami kwargs: age: 23
    func('xiami', **dt)  # name: xiami kwargs: age: 23

    dt = dict(age=23, score=60)
    func('xiami', **dt)  # TypeError: func() got an unexpected keyword argument 'score'

    func2('xiami', age=23)  # name: xiami age: 23 args ()
    ```

- ### 参数组合

  在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

  ```python
  def func(a, b=1, *args, d, **kw):
      print('a =', a, 'b =', b, 'args =', args, 'd=', d, 'kw =', kw)
  ```

  函数调用时, 会按顺序读入参数

  ```python
  >>> f1(1, 2, 3, d=4)
  a = 1 b = 2 args = (3,) d= 4 kw = {}
  ```

  神奇的是, 可以使用`*args` `*kw`的形式传入`tuple`和`dict`

  ```python
  >>> args = (1, 2, 3)
  >>> kw = {'d': 99, 'x': '#'}
  >>> f1(*args, **kw)
  a = 1 b = 2 args = (3,) kw = {'d': 99, 'x': '#'}
  ```

  ​
## 哈希表自己实现
实现过程中，当初始化一个新的字典对象时, 根据传入的key,计算出对应key的纯数字的hash值, `index = hash % 10007`(注意这里是取余数的计算) 之后使用list保存数据, `list[index]=value`, 因此需在字典对象创建时新建一个有一定长度的list, `list=[0] * 10007` . 这里的 10007 是素数.
- Q: 为什么需要一个**较大的**,**素数**长度的 list?
- A: 跟 index 的计算有关.首先看为什么是素数
  举例: 如果长度取3,那么当hash=1~10时:
         hash= 1, index = 1;
         hash= 2, index = 2;
         hash= 3, index = 0;
         hash= 4, index = 1;
         hash= 5, index = 2;
    	 hash= 6, index = 0;
         hash= 7, index = 1;
         hash= 8, index = 2;
         hash= 9, index = 3;
         hash= 10, index = 1;
         
         如果长度取4,那么当hash=1~10时:
         hash= 1, index = 1;
         hash= 2, index = 2;
         hash= 3, index = 3;
         hash= 4, index = 0;
         hash= 5, index = 1;
    	 hash= 6, index = 2;
         hash= 7, index = 3;
         hash= 8, index = 0;
         hash= 9, index = 1;
         hash= 10, index = 2;

  举例: 如果长度取5,那么当hash=1~10时:
    	 hash= 6, index = 1;
         hash= 7, index = 2;
         hash= 8, index = 3;
         hash= 9, index = 4;
         hash= 10, index = 0;
         
         如果为了保证不同的key计算出来的 index 尽量不重复.

## 编码
> 搞清楚了ASCII、Unicode和UTF-8的关系，我们就可以总结一下现在计算机系统通用的字符编码工作方式：
> 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
> 用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件：
> ![](https://www.liaoxuefeng.com/files/attachments/001387245992536e2ba28125cf04f5c8985dbc94a02245e000/0)
> 浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器：
> ![https://www.liaoxuefeng.com/files/attachments/001387245979827634fd6204f9346a1ae6358d9ed051666000/0](https://www.liaoxuefeng.com/files/attachments/001387245992536e2ba28125cf04f5c8985dbc94a02245e000/0)
																——廖雪峰 Python 教程

​                                                                


## 有用的资料

- 缩写发音:Youglish 网站
- [python in SICP](http://composingprograms.com/about.html)
- 正则的书：master python regular expression
- 从新手到中手: [Python3标准库的「实例」](https://pymotw.com/3/)
- [「Awesome-python-books」](https://github.com/Junnplus/awesome-python-books)
- [scott教练关于闭包，装饰器的微入门issue](https://github.com/AIHackers/Py101-004/issues/92)，内推荐资料：
  - **装饰器相关**
        - [Pycon演讲](https://us.pycon.org/2017/schedule/presentation/230/)
        - [Python Decorators: A Step-By-Step Introduction – dbader.org](https://dbader.org/blog/python-decorators)
        - [Welcome to decorator’s documentation! — decorator 4.1.2 documentation](http://decorator.readthedocs.io/en/master/)
        - [Primer on Python Decorators](https://realpython.com/blog/python/primer-on-python-decorators/)
        - 有余力看看这里的一些实例，[lord63/awesome-python-decorator: A curated list of awesome python decorator resources.](https://github.com/lord63/awesome-python-decorator)
  - **描述符**
    - 可以看上面的视频，加我的笔记 [Python 中的描述符 - 明生的博客 | Scott's Blog](http://scottming.com/2017/06/07/python_descriptors/)

- Scottming教练推荐的 [Google 开源项目风格指南 (中文版)](http://zh-google-styleguide.readthedocs.io/en/latest/)
- Scottming 教练在微信群分享的代码风格资料————**Clean Code in Python**：
    - #### Video

        * [Mariano Anaya - Clean code in Python - YouTube](https://www.youtube.com/watch?v=7ADbOHW1dTA)
        * [Transforming Code into Beautiful, Idiomatic Python](https://www.youtube.com/watch?v=OSGv2VnC0go)
        * [Raymond Hettinger - Beyond PEP 8 -- Best practices for beautiful intelligible code - PyCon 2015 - YouTube](https://www.youtube.com/watch?v=wf-BqAjZb8M)

    - #### Documents
        * [rmariano/Clean-code-in-Python: As presented in EuroPython 2016](https://github.com/rmariano/Clean-code-in-Python)
        * [Beautiful Idiomatic Python](https://gist.github.com/JeffPaine/6213790)
        * [Code Like a Pythonista: Idiomatic Python](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html)
        * [Code Style — The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/writing/style/)
        * [Clean code in Jupyter notebooks](https://www.slideshare.net/katenerush/clean-code-in-jupyter-notebooks)
        * [Idioms and Anti-Idioms in Python — Python 2.7.13 documentation](https://docs.python.org/2/howto/doanddont.html)
        * [Idiomatic Python — Intermediate and Advanced Software Carpentry 1.0 documentation](http://intermediate-and-advanced-software-carpentry.readthedocs.io/en/latest/idiomatic-python.html)
        * [《Clean Code》代码的整洁之道（一）](http://blog.csdn.net/ljheee/article/details/52619547)

## 软件/插件
- Atom HTML 插件

## 想做的事情
#### os.path https://docs.python.org/3/library/os.path.html
#### try/except 最好except获得一个准确的错误，如打开文件错误
阅读NBR整理的资料：
比 if...else 更好的判断结构
触发
0 在 2 利用字典调用函数 的探索有些阻塞,改换思路
其实利用字典调用函数是@ thxiami 同学的方案
背后更好的问题应该如此定义:
####  比 if...else 更好的判断结构
搜索
- python more effect if else
  =>python - [Most efficient way of making an if-elif-elif-else statement when the else is done the most? - Stack Overflow](https://stackoverflow.com/questions/17166074/most-efficient-way-of-making-an-if-elif-elif-else-statement-when-the-else-is-don)
- python multiple if multiple function
  [An alternative to If-Else and Switch [Python] « [ Curiosity,Experimentation ]](https://appusajeev.wordpress.com/2010/02/04/an-alternative-to-if-else-and-switch-python/)


- 170823想做的
    ####优化提升程序性能?
    - [PerformancePython - SciPy wiki dump](http://scipy.github.io/old-wiki/pages/PerformancePython)
    - [PythonSpeed - Python Wiki](https://wiki.python.org/moin/PythonSpeed)

    - # 计划下接下来1个月的安排
    - ### 文件读取实验

    - ##### 同学作业
      总体情况

    感觉这周大家的作业都完成的非常好，有许多人都是使用了函数来封装了代码，甚至有使用了类的。
    @thxiami 更是对程序做了一个深入的思考 #64
    ，同时看到 @Vwan @NBR-hugh 对问题进行了深入的讨论，对我也是有所启发。还有 @wangluzhou 等也使用类进行了比较好的包装。

    @Hugo1030 对任务难点也做了思考 #42 ，引发各位同学对探索讨论
    @Hugo1030 @elevenera @evanchan92 等代码简洁清晰，几乎没有大痛点

    有同学也对其他模块读取文件的模式进行了探索，比如 @wchengvincent 对 pandas 模块对使用，@SecZhujun 等有对 csv 进行探索。当然这里作业可以不使用到这两个模块，也比较鼓励大家对常用对基础用法先熟悉，根据需要去探索更好更适合的打开方式。

    @sunwenbo 等代码中有些新奇对写法，比如递归来实现连续输入，对城市相似输入的处理

    - #### 教练和大妈的博客


- 170824想做的
    - ## 个人教程jupyter版
    - ## 搭建博客
    - #### 开源程序如何处理从 API JSON 嵌套字典取值的问题
    - reST格式可以增加type
    - Atom 能否代替 Pycharm，因为它能配合CLI

- 170825 Todo:

- 修改两种模式输入为统一入口
- 理解和使用 Vwan 的 `objectjson`
- 添加自动补全功能
- 外国API

- 修改输入格式为 北京,0,1
- 类重构，自己原来的代码太臃肿了！！
- # 个人教程jupyter版
- ## 搭建博客
- ## 计划下接下来1个月的安排