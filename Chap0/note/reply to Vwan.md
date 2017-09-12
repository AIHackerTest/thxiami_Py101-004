## 0 用户输入 4 位数合法性问题
### 0.1 Vwan 同学的点评
> 这可能是一个会有争议的地方，关于用户输入的4位数判断规则，先看一个你的运行结果：
```python
Please type in a 4 digit number.
 >0158
1A3B
第6次猜测，还有4次机会
Please type in a 4 digit number.
 >158
Only a 4 digit number is wanted! e.g. 5
```
> 0158 和 158 被视为两个不同的数字，前者是四位数，后者不是（这个没问题）。关键是前者，之所以判断是四位数，源自输入类型是str
> 
> 个人认为0158这种应该也被排除掉的。
```python
>>> a = 0158
  File "<stdin>", line 1
    a = 0158
           ^
SyntaxError: invalid token
>>> a = 158
>>> a
158
```

### 0.2 我的想法
当初写这部分时候确实也想到过这个问题，我们观点不同，这可能是源于对于游戏的理解：

我是从字符串的角度考虑的，每个数位上的数字都是独立的个体，你可能更多的是从数字的角度出发。所以，我想着从规则出发，首位不为0，那么玩家可通过`0111`，`0222`这种方式来猜测后 3 位，当出现 A或B 时能缩小范围至后3位。这只是一种对规则和玩法的理解，当然也可能是个Bug，哈哈，没有什么对错。

## 1 docstring
### 1.1 Vwan 同学的想法
>关于docstring，同学参考的使是[编码之前碎碎念(工程实践) — python-web-guide 0.1 文档的规范](http://python-web-guide.readthedocs.io/zh/latest/codingstyle/codingstyle.html#id21)，貌似也是google的规范，可是我发现我不太认同咋办，我感觉代码第一眼看过去多是注释，代码被喧宾夺主了，主要是两部分：

```python
def guess(wanted_num, input_num):
    """
    判断给定的两个数字关系，根据判断结果打印必要信息并返回布尔值。
    
    Args：
        wanted_num (int): 程序给定的需要用户去猜测的数字，2位数
        input_num (int)：用户输入的数字,2位数
        
    Return:
        bool : True代表两个数字相等；False代表不相等
        
    Demo：
        result_bool = guess(10, 15), 程序会打印"大了"，并返回 False;
    """
    pass
```
>docstring在代码定义语句之下，代码体之上。当注释很长的时候，分隔的好远，比较跳跃感
docstring内空行太多，所以看着更长，prefer的样式
```python
"""
判断给定的两个数字关系，根据判断结果打印必要信息并返回布尔值。
Args：
    wanted_num (int): 程序给定的需要用户去猜测的数字，2位数
    input_num (int)：用户输入的数字,2位数
Return:
    bool : True代表两个数字相等；False代表不相等
Demo：
    result_bool = guess(10, 15), 程序会打印"大了"，并返回 False;
"""
def guess(wanted_num, input_num):
```

### 1.2 我的想法
- 关于 Style
如果觉得空行比较多，其实你可以选择另一种 style: **reStructuredText (reST)**，关于它的大概样式可以在之前我给的参考资料里可以看到。[What is the standard Python docstring format?](https://stackoverflow.com/a/24385103)[1]
- docstring 放函数内还是函数外？
引用 [PEP257-- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/#id15) 里关于 docstring 定义的一句话：
> A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes the \_\_doc\__ special attribute of that object.

	所以如果放在函数外，函数就没有`__doc__`属性了,会导致：
    - 使用help命令就无法看到函数的 docstring (可以自己试一下)
    - 无法使用工具根据 docstring 自动生成文档（这个是我的猜测，没有自己实践）

## 2 获取用户输入的一些讨论点

下方是我写的初级版猜字游戏的获取用户输入的函数
```python
def get_num():
    # 获得用户输入
    input_num = input('Please type in a number.\n >')

    # 判断用户输入的合法性，当输入仅包含数字时返回该数字；其他情况要求用户重新输入
    if input_num.isdigit():
        return int(input_num)
    else:
        print('Only a number is wanted! e.g. 5')
        return get_num()
```
### 2.1 Vwan 同学的想法
> 判断输入是否合法用到isdigit方法，单纯的想探讨一下，try/except 和这种温和的方法哪种是best practice? 递归方法和循环判断哪种更推荐？感觉递归可能会慢一些把


### 2.2 我的想法
- try/except or if/else?

	目前没接触过复杂的情况，就本次任务练习来说，我上面的这种方式不能捕获异常情况（command+Z），但我看教练们都是使用的try/except，在于这种存在不确定性的地方，应该try/except通用性更强，或代码更健壮。另外，我搜索到下面这个问题和回答，答案中，并没有说方法哪个更好，只是给了一些例子和需要注意的坑，可以看一看。
[Asking the user for input until they give a valid response](https://stackoverflow.com/a/23294659)
- 递归与循环 
在某个 issue [关于递归函数返回值的问题（本周作业碰到的问题）](https://github.com/AIHackers/Py101-004/issues/23#issuecomment-321464607)下教练已经提出了这个问题，他建议从递归程序可能会产生的影响去评估：
    - 健壮性
    - 效率 
    - 可读性
    - 其他可能发生的问题
这部分是花时间最多的地方，我参考了一些资料，但也只学了皮毛，然后从前三点回答了教练提出的问题，希望可以交流：[递归的学习笔记](https://github.com/thxiami/Py101-004/blob/master/Chap1/note/Study_note.md#recursion)

## 3 关于 if/else 的代码习惯
### 3.1 Vwan 同学的建议
>昨天看王垠的[编程的智慧](http://www.yinwang.org/blog-cn/2015/11/21/programming-philosophy)中”优雅的代码“部分，他提到”优雅的代码在逻辑上大体看起来，是枝丫分明的树状结构（tree）“，体现在if else 控制语句中，就是if 语句几乎总是有两个分支。一个分支的代码看起来代码短小了，但逻辑上读起来大脑就费劲了，结合”大脑爱偷懒“的本性，我被他说服了，现在也觉得他说的有道理，准备借鉴实施。摘了一部分你的代码如下：

```python
# 对玩家猜测次数进行判断
        if count > 10:
            print('您没有机会猜测，游戏结束')
            break

        # 获得玩家输入
        print(f'第{count}次猜测，还有{10 - count}次机会')
        input_number = get_num()

        # 对玩家猜测结果进行判断
        if guess(wanted_number, input_number) is True:
            break
```
>如果是王垠，他可能建议这么写：感受一下，您觉得是否认同?

```python
# 对玩家猜测次数进行判断
        if count > 10:
            print('您没有机会猜测，游戏结束')
            break
        else:
            # 获得玩家输入
            print(f'第{count}次猜测，还有{10 - count}次机会')
            input_number = get_num()

            # 对玩家猜测结果进行判断
            if guess(wanted_number, input_number) is True:
                break
            else:
                count += 1
```
### 3.1 我的想法
首先非常感谢你提出这个建议，我思考了一下，这种树状结构的代码确实有助于理解。当初我选择一个分支的代码，是因为我这段代码是放在一个`while True`的循环内的，看到`while True`，我的第一想法就会去找它什么时候`break`，我潜意识里把猜测次数大于10和玩家猜对当作并列的两个`break`的条件，然后写了个Bug：先判断玩家输入，后判断猜测次数，结果玩家可以猜11次。如果携程树状结构的代码，就不会出现这个bug了。

## 4 关于你最新版的代码

- 竟然用类重构整个游戏，赞一个！
- 进阶版的方法 `__check_num` 中的 `count_b = len(set(numlist1) & set(numlist2))`，其实 `count_b`  按我的理解是`len(set(numlist1) & set(numlist2)) - count_a`，看你最后返回的实际意义上B的数量也是这个。所以不知你定义的`count_b` 为何没减 `count_a`，而是在`return`时候减去
- 进阶版的方法 `play()` 的 `docstring` 是不是忘了改了，还是基础版的`docstring` 
- 进阶版当用户猜对时候，使用的是 `sys.exit(0)` 方法完成退出。在脚本开头用 `import sys`导入了`sys`整个包，根据 [PEP8](http://legacy.python.org/dev/peps/pep-0008/#imports) 建议使用`import sys.exit` 或 `from sys import exit`，理由：
>Absolute imports are recommended, as they are usually more readable and tend to be better behaved (or at least give better error messages) if the import system is incorrectly configured (such as when a directory inside a package ends up on sys.path)

	但是尽量不要用`from sys import *`，防止不同模块中有相同名称的函数/类...，但可能不知道或没注意，这时后导入的就会把先导入的覆盖掉。你没用这么用，挺好的，我在这里只是觉得可能需要提醒一下。




