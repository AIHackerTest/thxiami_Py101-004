# 170821 2wd1
### 探索 `3.5h`
#### 0.1 上午

- [x] 补充ch1个人教程的文件读取部分 `1.5h`
- [x] [NBR-hugh格式](https://github.com/NBR-hugh/Py101-004/tree/master/Chap1/project)+[闪闪建议](https://github.com/AIHackers/Py101-004/issues/47#issuecomment-323584531)=个人ch1天气查询软件的[README](https://github.com/thxiami/Py101-004/tree/master/Chap1/project) `0.5h`
闪闪建议：
> readme 里面对用户的组块和面对开发者的组块归一下类，比如 开篇即是 「 Feature、Require、Using 」 这三个面对用户的组块，之后再是面对开发者的组块，这样更清晰：P

#### 0.2 下午
- [x] 学习使用Gifcam录屏 `0.5h`
效果如图：
![](https://raw.githubusercontent.com/thxiami/Py101-004/master/Chap1/project/ch1.gif?token=AZTlP7Rw9EZDq77knXlMNmWkRy_A2BRzks5Zo6uWwA%3D%3D)

#### 0.3 晚上
- 回复 [Vwan 昨晚的 comment](https://github.com/thxiami/Py101-004/commit/bae7e515f0fedccf8eca5dbd566ced53028a6306#commitcomment-23754430)，提交 pull request `1h`
- **留有一个坑**：如何与别人协作开发，提交代码到对方仓库；若无push权限，如何在命令行提交pull request 到别人仓库呢，完成协作开发，非网页端。还有待挖掘

### 复盘之收获
- 学习了[Gitcam](http://blog.bahraniapps.com/gifcam/)，了解一大心愿，可以录屏保存为Gif，便于交作业和与别人讨论

# 170822 2wd2

## 探索 `5.5h`
#### 0.1 上午
- 10:50 - 11:50 探索Github上如何给同侪协作编程 `1h`
	即通过pull request 贡献自己版本的代码，同侪看到后可以comapare 变化，选择接受或不接受。
    昨晚在网页端在Vwan的仓库上的页面，点击某个脚本文件，然后点编辑，编辑后按提示 create pull reqeust。我仓库页面也显示了 pull request，但是Vwan反映那边看不到。之后我搜索github 给别人贡献代码，参考[阮一峰博客](http://www.ruanyifeng.com/blog/2017/07/pull_request.html)，了解常规步骤为：Fork别人仓库->自己仓库->自己修改完代码->点击New pull request->选择提交到哪个分支->提交修改->等待对方选择接受或拒绝
    然后就卡在了第一步Fork上，根据提示应该是已经Fork过这个仓库了，可能是说从AIHacker那儿Fork过同名仓库，不能再Fork。
    ![image](https://user-images.githubusercontent.com/26535231/29577333-998ff140-879d-11e7-8e7d-1059ae5af80c.png)
    最后只能选择将代码提交到自己仓库，然后@对方，对方有两种看代码方法：
    - 在线查看脚本文件，不能对比变化
    - 或者对方下载下来后push到自己仓库，可对比变化

- 扫了下[阮一峰博客：Commit message 和 Change log 编写指南](http://www.ruanyifeng.com/blog/2016/01/commit_message_change_log.html)，没有完全学习，知道了Angular 规范和写commit log的工具，之后应该学习。
- 
#### 0.2 下午
- 14:50 - 15:45 ch2 网络版天气查询程序 MVP `1h`
	- 从ch1处拿来了 command的几个函数,ischinese函数
	- 以伪代码形式，整体框架列出，需要做反应的地方就以 `print('这是xxx')`代替
	- 逐步将伪代码替换为真实代码
		- 判断输入
		- 学习心知API python demo，下载至本地自己不断测试学习
		- 天气查询函数
    - 整体测试

- 15:50 - 16:10 因发现天气API不仅可以通过城市的中文查询，可以通过城市的拼音查询，改进用户输入可为拼音（英文）。`ischinese()`+`ispinyin()`=`iscity()`  `0.5h`
- 16:10 - 16:30 看大妈的最佳MVP视频，参考廖雪峰网站教程修改 git命令，使更短。 `0.5h`
	- 修改的命令：`git config --global alias.st status`
	- 效果: `git status` -> `git st`
	- 其他：
        - `git commit -m ""` -> `git ci -m ""`
        - `git reset HEAD filename` -> `git unstage filename` 从工作区撤销 add

#### 0.3 晚上
- 18:00 -19:00 阅读文章，问答 `1h`
    - [PythonSpeed - Python Wiki](https://wiki.python.org/moin/PythonSpeed) 发现一些平时编程中可使用的提高性能的技巧，不用很复杂，习惯就好。
        - 循环或遍历时使用生成器省内存
            - Python2中用xrange，不用range；Python3的range默认就是2的xrange
            - map and itertools.imap
            - dict.items and dict.iteritems
            - file = open(path), for line in file 好像也是的？
        - 数据类型
            - collections.deque 在开头插入或删除元素的时间复杂度是O(1)，list是O(n)
        - 方法
            - string 的拼接： ''.join(seq) which is an O(n) process. In contrast, using the '+' or '+=' operators can result in an O($n^2$) process because new strings may be built for each intermediate step.
        - Take advantage of interpreter optimizations
            - Starting with Py2.3, the interpreter optimizes while 1 to just a single jump. In contrast, prior to Python 3, while True took several more steps. Starting in Python 3, True, False, and None are reserved words, so there is no longer any performance difference here. 
            - Multiple assignment is slower than individual assignment. For example "x,y=a,b" is slower than "x=a; y=b". However, multiple assignment is faster for variable swaps. For example, "x,y=y,x" is faster than "t=x; x=y; y=t".
            - Chained comparisons are faster than using the "and" operator. Write "x < y < z" instead of "x < y and y < z".
        - 第三方模块
            - Numpy Numpy is essential for high volume numeric work.比如矩阵运算
            - Scipy [速度对比实验](http://scipy.github.io/old-wiki/pages/PerformancePython)
    - [Most efficient way of making an if-elif-elif-else statement when the else is done the most? - Stack Overflow](https://stackoverflow.com/questions/17166074/most-efficient-way-of-making-an-if-elif-elif-else-statement-when-the-else-is-don) 
        未看完，这个应该与之前提的[issue：ch1 任务难点「如何更好实现用户指令查询功能」的思考](https://github.com/AIHackers/Py101-004/issues/64) 指令函数变量放在字典内调用 或 if/elif/../else有关，讲的是效率方面

- 21:40 - 23:20 回复[同侪评论](https://github.com/thxiami/Py101-004/commit/bae7e515f0fedccf8eca5dbd566ced53028a6306#commitcomment-23794348)，对代码[提出建议](https://github.com/thxiami/Py101-004/commit/bae7e515f0fedccf8eca5dbd566ced53028a6306#commitcomment-23798283) `1.5h`
	主要讨论ch1作业中的同侪的方案，不该使用User类

- 23:20 - 23:30 看同侪作业发现python库`textwrap`中的`dedent`完美解决之前的
```python
"""\
    line1
    line2
"""
```
    多行文本输出时会把每行前面的空格也输出出来的问题
代码：
```python
from textwrap import dedent
s = dedent(
"""\
    line1
    line2
"""
)
print(s)
```
结果：
```
line1
line2
```

### 复盘之收获
- 学习大妈编程风格，不断完成最小成果，用了1h就把ch2作业基本版搞定了
- 解决了多行文本的输出每行前置空格问题


# 170823 2wd3

### 探索 `7h`
#### 0.1 上午
- [x] ch2 进阶之温度转换

- 温度单位转换问题解决，引入变量保存当前温度单位参数'c'or'f' `1h`
    - 用于调用API时使用
    - 用于输出时判断是输出摄氏度还是华氏度

- 构思如何解决实时天气查询 和 单日/多日天气概况查询的转换 `0.5h`
    - 设想主函数分两条路，实时模式 和 单日/多日模式
    - 每条路都包含了 获取输入->从API拿数据->解析数据输出

#### 0.2 下午
- [x] ch2 进阶之指定日期查询天气
- [x] 修改git 上一次的 commit log

- 程序进阶功能: 兼容实时天气查询 和 单日/多日天气概况查询 `2.5h`
    - 软件流程：
    根据用户输入选择api接口url，组成api参数字典  -> request.get 拉取天气数据 -> 解析天气数据并输出
    - 目标：
    放弃了上午构思的思路，虽然更好实现。现在的目标是：
    不管哪种模式，每一步的传入和传出变量类型及意义相同，模式的不同根据传入参数的具体值来判断，然后在每一步的内部函数内完成不同模式的处理过程，输出固定类型和意义的变量供下一步使用。
    比如：
    第1步，不管哪种模式，它接受参数都是用户输入的`城市名` 和 `当前的环境变量`（温度单位是'c'还是'f',查询模式是now还是daily），输入的都是对应`API URL` 和 `API 参数字典`
    - 难点:
        - api 接口 url 不同，如何修改和传递该参数
        - api 查询时参数不同，判断用户输入是城市后，如果是daily模式，如何要求用户输入日期
        - 求用户输入日期的如何定
        - 输出时的文字格式不同
    - 实现：
    	- 定义一个变量保存当前模式 query_mode = 'now' 或者 'dairy'
    	- 定义一个基本的 api 查询时使用的参数字典
    	```python
        default_api_params_dict = dict(
                key = '4r9bergjetiv1tsd', # API key
                unit = 'c',  # 单位 c 是摄氏度，f 是 华氏度
                language = 'zh-Hans',  # 查询结果的返回语言
            )
        ```
    	- 每一步都传入`query_mode`和`default_api_params_dict`，根据对应模式做出对应操作

- 学习怎么修改 git 上一次的 commit log `0.5h`
    - 在git bash 内`git commit --amend`
    - 进入 Vim 编辑器，`esc`切换编辑与命令模式，编辑后，切换至命令模式，输入`: x` 保存编辑并退出。记得`:`和`x` 之间有个空格
    - git log 查看

#### 0.3 晚上

- 搜索`*args` 和 `**kwargs`的作用，以及怎么用,随后延伸到 API返回的字典中嵌套多层列表和字典，如何取得想要的信息？ `2.5h`
    - 激发 `0.5h`
        - Vwan 关于使用`**kwarg`解析字典的两次comment
            - [comment](https://github.com/thxiami/Py101-004/commit/01768b3e6d675848848f3fd01b6eb041cb579b8c#commitcomment-23821483)
            - [comment]()
        - [API返回的字典中嵌套多层列表和字典，如何取得想要的信息？](https://github.com/AIHackers/Py101-004/issues/66#issuecomment-324340413)，Vwan 以**独特的思路**解决了这个问题，使得当切换api或者api返回数据格式变化时，可以以很小的代价完成转换。
    - 搜索 `0.5h`
        - 配合代码理解`*args` 和 `**kwargs`的作用，以及怎么用：[*args and **kwargs-StackOverflow](https://stackoverflow.com/questions/3394835/args-and-kwargs)
    - 思考 `1.5h`
        - 看懂Vwan的代码是如何从嵌套多层列表和字典中取得数据的，探索结果如下

        ```python
        def parse_json(json_data,**required_data):
            # 该函数作用是从 json_data 按 required_data 所需取数据，组成新的字典并返回
            # json_data 是 API 返回的json数据处理后的字典
            # required_data 是精妙所在，规定了如何从 json_data 取所需数据
            extracted_data = {}
            for data,key in required_data.items():
                tmp = json_data
                if ("." in data):
                    temp_keys = data.split(".")
                    for temp_key in temp_keys:
                        tmp = tmp[temp_key]
                    extracted_data[key] = tmp
                else:
                    extracted_data[key] = json_data[data]
            return extracted_data
        ```

        ```python
        json_data = {
          "HeWeather5": [
            {
              "basic": {
                "city": "北京",
                "cnty": "中国",
                "id": "CN101010100",
                "lat": "39.90498734",
                "lon": "116.40528870",
                "update": {
                  "loc": "2017-08-23 23:46",
                  "utc": "2017-08-23 15:46"
                }
              },
              "now": {
                "cond": {
                  "code": "100",
                  "txt": "晴"
                },
                "fl": "28",
                "hum": "73",
                "pcpn": "0",
                "pres": "1007",
                "tmp": "26",
                "vis": "7",
                "wind": {
                  "deg": "275",
                  "dir": "西风",
                  "sc": "微风",
                  "spd": "6"
                }
              },
              "status": "ok"
            }
          ]
        }

        # .式结构类似于.式语法访问对应属性，精妙
        required_data = {
          'basic.city': 'City',
          'now.cond.txt': 'Weather',
          'now.wind.dir': "WInd",
          'now.tmp': "Temperature",
          'basic.update.utc': 'Last Updated On',
        }

        # 使用方法
        extracted_data = parse_json(json_data['HeWeather5'][0],**required_data):
        ```
        返回结果:
        ```
        extracted_data:{
        'City': '北京',
        'Weather': '晴',
        'WInd': '西风',
        'Temperature': '26',
        'Last Updated On': '2017-08-23 15:46'
        }
        ```

### 复盘之收获
- 看到 Vwan 处理嵌套字典的方法，觉得很棒。然后冒出了一个想法，JSON 是通用的数据传输格式，一些开源程序肯定也会遇到这种问题，应该看看他们是如何解决的

### 复盘之改进
- 今天本可以使用ch1的框架来完成的，但考虑到之前一个同学提议：先完成MVP，Vwan也说过这样大家可以交流代码，然后再优化或者重构。原来ch1的框架使用的是类，担心没看过的人第一次看会吃力，大妈当时也疑惑需要用类吗？所以使用函数从零开始写了ch2。
- 思考一下，使用 User 类应该会更快完成ch2。因为ch2 MVP 中为解决温度单位和模式转换新增的`temperature_unit`,`query_mode`和`default_api_params_dict`都可以作为 User 的实例属性的。其次，复用 ch1 的框架，只需改查询天气部分的代码，就不需要重头写一遍程序其他的函数了
- 需要定下来一个版本，用作之后几周的框架

# 17824 2wd4

## 探索 `4.5h`
### 0.1 上午
#### 概况
- 修改输出格式，仿张之洞学友，为单行输出
- 提交作业

#### 过程
- 10:00-10:20 昨天修改完程序未运行，导致了一个bug，解决后push，修改README `0.5h`
- 10:20-10:40 当需要将文字在屏幕上以单行输出，但文字过长，如何在代码中分为多行，且无多余空格出现？`0.5h`
    - 激发:受昨天张之洞学友的输出影响，决定修改多日天气输出格式为一行一天
    - 探索: 
        - 为了一行不至于过长，使用多行字符串
        ```python
        from textwrap import dedent
        s = dedent("""\
          line1\
          line2
        """)
        print(s)
        ```
        ```
        line1      line2
        ```

        - 发现 line1 和 line2 之间会有空格，因为这是一个多行字符串，想去掉两行之间的空格，发现可以使用 `"string"`+ `\`拼接
        ```python
        s = "line1"\
            "line2"
            print(s)
        ```
        输出结果：
        ```
        line1line2
        ```
- 11:00 - 11:40 修改帮助文档说明，把多日模式的使用方法添加至程序启动后的帮助文档中 `0.5h`
- 11:50 - 12:40 下载cmder，录gif，提交作业 `1h`

### 0.2 下午

#### 概况
- 根据用户输入猜测城市
- 浅探 一场由`+=` 引发的`bug`
- 学习 Pycon2017 的分享：[Awesome Command Line Tools](https://us.pycon.org/2017/schedule/presentation/518/)

#### 过程
- 15:00-15:30 sunwenbo 同学相似城市判断功能的代码阅读与[建议](https://github.com/sunwenbo/Py101-004/commit/8824fb1f009f635839b94b21c32719a384590767##commitcomment-23840328) `0.5h`
    - 贡献代码 15min
    - 写 comment 15min
- 15:30-15:45 改代码时,无意触发一个python的语法“bug” 

    ```python
    ls1 = []
    ls2 = ['ab'] * 3

    print('ls2:', ls2)
    for i in ls2:
        print('-'*10)
        print('i:', i, type(i))
        ls1 += i  # list 和 str 怎么可以这样加？
        print('ls1:', ls1, type(ls1))
    print('ls1:',ls1)
    # 运行结果如下：
    """
    ls2: ['ab', 'ab', 'ab']
    ----------
    i: ab <class 'str'>
    ls1: ['a', 'b'] <class 'list'>
    ----------
    i: ab <class 'str'>
    ls1: ['a', 'b', 'a', 'b'] <class 'list'>
    ----------
    i: ab <class 'str'>
    ls1: ['a', 'b', 'a', 'b', 'a', 'b'] <class 'list'>
    """
    ```
    修改一下`ls1 += i` 为 `ls1 = ls1 + i`，再次运行,看来二者不完全等效
    ```python
    ls1 = []
    ls2 = ['ab'] * 3

    print('ls2:', ls2)
    for i in ls2:
        print('-'*10)
        print('i:', i, type(i))
        ls1 = ls1 + i
        print('ls1:', ls1, type(ls1))
    print('ls1:',ls1)
    """
    ls2: ['ab', 'ab', 'ab']
    ----------
    i: ab <class 'str'>
    Traceback (most recent call last):
      File "C:/py/Py104/t.py", line 8, in <module>
        ls1 = ls1 + i
    TypeError: can only concatenate list (not "str") to list
    """
    ```
    在此修改 `ls2 = [1] * 3`，报错，根据报错`'int' object is not iterable`，猜想`+=`要求等号右边是一个可迭代对象
    ```python
    ls = []
    ls2 = [1] * 3

    print('ls2', ls2)
    for i in ls2:
        print('i:', i, type(i))
        print('ls', ls, type(ls))
        ls += i
    print(ls)
    # 运行结果如下：
    """
    ls2 [1, 1, 1]
    i: 1 <class 'int'>
    ls [] <class 'list'>
    Traceback (most recent call last):
      File "C:/py/Py104/t.py", line 8, in <module>
        ls += i
    TypeError: 'int' object is not iterable
    """
    ```
	- 搜索：
		- 搁置

- 17:40 - 18:30 如何实现命令行自动补全功能？ `1h`
	- 激发：我给sunwenbo comment中提到了猜测用户输入的城市并返回可能的城市列表，scottming 教练在看到后推荐命令行自动补全更人性化，并**再次**推荐Pycon2017 的演讲 Awesome Command Line Tools
    - 探索：
        - [Pycon演讲介绍](https://us.pycon.org/2017/schedule/presentation/518/)
        - [Pycon演讲视频](https://www.youtube.com/watch?v=hJhZhLg3obk)，28min的视频(10min左右可学会设计一个自动补全的命令行程序)
    - 收获：
    	- 知道了如何用 `prompt-toolkits`这个包给命令行程序增加自动补全功能
    		- How to make a interactive program?
                - Read
                - Eval
                - Print
                - Loop
            - Check List
                - Persistent history
                - History search
                - Emacs Keybingdings
                - ~~Paged Output~~ 视频中未实现，但给出实现方案所需的库
                - Auto-Completion
                - Minimal Config
                - Syntax Coloring

    	- 第一次听说设计 CLI 程序遵守一定的原则，会让你的程序变得更棒
    		- **Discoverablity**  让程序的一些特色功能更容易被人发现，比如代码补全不用tab，在输入时就会提示
			- **User focus** 永远 user 第一，如何实现才是第二
			- **Configurablity** 如不需要，尽量减少配置文件，因为它的存在说明你不能准确把握什么样的配置对用户最佳（除了一些如色彩搭配的个人喜欢配置文件）
	- 代码： 更新至仓库

### 0.3 晚上
#### 概况
- [互评阅读与回复](https://github.com/thxiami/Py101-004/commit/799549ba304bb8253b2109fad9895f2520250a13#commitcomment-23846964)

#### 过程
Vwan同学点评主要集中在程序设计理念和产品理念方面,还有一些代码细节问题，阅读并回复。 `0.5h`
- 程序设计理念
	- 问：`api_params_dict` 为何没放在程序主函数脚本文件
	- 答：分离主程序与配置文件
- 产品理念
	- > 昨天跑你的daily的时候，玩了一下 0,1这种command, 一点个人感觉哈，用户一般需求会是：我想知道未来几天的天气如何。那这里只有一个变量，就是“几天”，而不是一个区间。那如果用户想知道“从明天起3日内天气”，可能会这么说“未来四天天气”
	- 答：很有道理，需要改变。

### 复盘之收获
- Pycon2017 的演讲 Awesome Command Line Tools 让我迅速知道如何实现命令行代码补全，同时传递给我程序设计的理念，尤其是User focus，这个很重要！

### 复盘之改进

- 问题1：没有及时消化之前教练推荐的资源，后来回想，教练推荐的方案必定是经过自己筛选的高质量资源，优先级应该放在比较高的地方，有时间应先看这些资源。

- 改进方案：如果当时没时间看教练推荐的资源，那么放在Stydy note 中的教练推荐资源区，利用`#`的多少作优先级排序

- 问题2：最近自己挖的坑有点多啊，不知如何安排。


# 170825 2wd5

### 探索 `6.5h`
#### 0.1 上午
- 10：00-12:30 Git 本地如何同步别人仓库 `2.5h`
	- 激发：想本地 Git clone 同学仓库，然后同学有改动时候 git pull 同学仓库，发现拉取后没有任何改变
	- 搜索：
		- 搜索 git clone other's repo 网上都是推荐的先clone，再 pull，与自己方法一样，但使用后本地提示下面情况，而且仓库内文件并没有全部同步
        ```
        From github.com:thxiami/learngit
         * branch            master     -> FETCH_HEAD
        error: Your local changes to the following files would be overwritten by merge:
                License.txt
        Please commit your changes or stash them before you merge.
        Aborting
        Updating 6622913..2dd1e77
        ```

        - 搜索 git FETCH_HEAD
        	- 它是一个文件，路径：.git/FETCH_HEAD，保存了从远程拉取的仓库分支最新的commit id 的记录
待整理，思路就是使用git 命令 -> 查看.git/FETCH_HEAD文件，对比github上最新的commit id，理解下面的几句话。
            FETCH_HEAD： 是一个版本链接，记录在本地的一个文件中，指向着目前已经从远程仓库取下来的分支的末端版本。
			- 为了理解它，先了解下 [git fetch](https://git-scm.com/docs/git-fetch) 和 git pull ([Difference-personal blog](https://blog.mikepearce.net/2010/05/18/the-difference-between-git-pull-git-fetch-and-git-clone-and-git-rebase/)) [Difference-stackoverflow](https://stackoverflow.com/questions/3620633/what-is-the-difference-between-pull-and-clone-in-git)
			- git fetch
                git fetch 有四种基本用法
                1. git fetch            →→ 这将更新git remote 中所有的远程repo 所包含分支的最新commit-id, 将其记录到.git/FETCH_HEAD文件中

                2. git fetch remote_repo         →→ 这将更新名称为remote_repo 的远程repo上的所有branch的最新commit-id，将其记录。

                3. git fetch remote_repo remote_branch_name        →→ 这将这将更新名称为remote_repo 的远程repo上的分支： remote_branch_name

                4. git fetch remote_repo remote_branch_name:local_branch_name       →→ 这将这将更新名称为remote_repo 的远程repo上的分支： remote_branch_name ，并在本地创建local_branch_name 本地分支保存远端分支的所有数据。
			- git pull
				- 运行`git pull origin master`后等效于
                    ```
                    git fetch origin master
                    git merge FETCH_HEAD
                    ```
				- 首先, 基于本地的FETCH_HEAD记录，比对本地的FETCH_HEAD记录与远程仓库的版本号
				- 然后, `git fetch origin master` 获得当前指向的远程分支的后续版本的数据，然后再利用`git merge FETCH_HEAD`将其与本地的当前分支合并。

	- 问题分析：当使用 `git pull origin master` 拉取远程仓库 origin 的 master 分支到当前分支(`git fetch  origin master`)并合并(`git merge FETCH_HEAD`)时，因我本地修改了`License.txt`这个文件，工作区文件发生变化，但又没有commit（也没有权限commit）, git为了防止你的修改丢失，会要求你对工作区修改进行`commit`或`stash`。
	- 解决方案
		1. `git clone git@github.com:Hugo1030/Py101-004.git` 克隆学友仓库，假设此时最新版本的commit id:1
		2. 在`master`分支上进行调试，会涉及工作区文件的修改
		3. 学友仓库有更新时，此时最新版本的commit id:2
        	3.1 撤销本地仓库工作区修改：
                - `git reset --hard` 将工作区内文件回退到 commit id 为 1 的版本
        	3.2 `git pull origin master`拉取远程仓库 origin 的 master 分支到当前分支并合并
        4. 若忘了第3.1步，先进行第3.2步，此时回到3.1步重新走一遍流程即可

### 0.2 下午&晚上
- 如何安排自己项目的脚本结构，不同功能函数放不同文件 `4h`
	- 激发：[Wangjunyu 教练的疑问](https://github.com/thxiami/Py101-004/commit/314b68485d729cdcdcbe84f9108f7cfa3bccec64#commitcomment-23863478) 教练提出我的项目中是如何区分函数放在`utils.py`还是主程序文件. 当初设计时候自己没有很详细的规划，一个简单的想法就是：只看主程序文件中的**主函数**和**几个主线关键函数**就可以明白程序运行的主要逻辑，其他支线所需的函数放在utils.py中，让用户看到函数名大概可以指导它的作用，如需知道怎么实现，再去utils.py中去找。
	- 主线关键函数2类：
		- 实现指令功能的函
			- `print_help()`
			- `print_history()`
			- `quit_()`
			- `query_mode_switch()`
		- 查询天气相关
			- 调用 API 获取数据
			- 解析 JSON 数据并输出天气
	- 支线函数：
		- 判断用户输入
			- `ispinyin()`
			- `ischinese()`
			- `iscity()` 结合以上两者初步判断是否为城市
        - 温度单位转换后输出提示
			- `temperature_switch_prompt()`
        - 根据用户输入组成 API 参数字典
			- `append_city_and_date()`
		- 代码自动补全相关
			- `get_city_list()`
            - `get_command_completer()`
            - `prompt_input()` `# 一个有自动补全城市名,指令,输入历史功能的input 函数` 15:30
	- 探索
		- 15:50-17:00 阅读关于代码结构的问答，看pgcli的项目结构
	- 初步方案
		- 17:30-19:30 更改自己代码，函数和定值变量分开放在utils包下,更改README

### 复盘之收获
- 探索了Git 本地如何同步别人仓库，对于git 的工作原理进一步加深

### 复盘之改进
- 未按照原计划进行写个人教程，中途被其他事情分散了注意力
- 应该试着先按自己计划执行，如果有突发事情，纳入计划，划分优先级


# 170826 2wd6

### 探索 `6.5h`
#### 0.1 下午
- 14:00 - 16:22 为了能发到issue内,完善昨天的克隆学友仓库教程 `2.5h`
    - 自己通过 git 反复实践，加深对工作区的理解

- 个人教程`1.5h`
	- 16:50-18:24 完成 MVP 的书写

#### 0.2 晚上
- 个人教程 `2.5h`
	- 21：10-23：48 教程除了 JSON 和 API未查资料补充，其余部分均完成
	- 写教程指定日期查询部分时，又对程序进行改进

### 复盘之收获
- 撰写个人计划时候，又对原来的函数进行思考，进一步优化了代码中调用API拉取天气的函数，使之与解析JSON数据输出天气的函数保持类似的风格

### 复盘之改进
- 上午学习时间过短，需要加强上午时间的安排和利用，保证明天9：30可以开始在电脑前工作


# 170827 2wd7
## 探索 `1.5h`
### 0.1 下午
- 12:10-12:30 看代码Review的意见，对应修改风格部分 `0.5h`
- 16:10-16:38 开智学堂 ch2 卡包 `0.5h`
	- 关于API和JSON还是要再细看补充一下

### 0.2 晚上

- 18：12-18：55 看到教练发布issue：[关于代码审查中的建议抽象](https://github.com/AIHackers/Py101-004/issues/92)，阅读学习 `0.5h`
	-  通过读和自己上手写代码学习lambda，map，reduce，闭包


# Timelog
- 2wd1 `3.5h`
- 2wd2 `5.5h`
- 2wd3 `7h`
- 2wd4 `4.5h`
- 2wd5 `6.5h`
- 2wd6 `6.5h`
- 2wd7 `1.5h`