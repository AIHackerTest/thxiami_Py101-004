# 170814 1wd1

### 0 任务
#### 0.1 基本任务
- 提交作业
	- [x] 添加程序使用说明和版本更新记录
	- [x] 评价同学作业
- ch1 天气查询程序
	- [ ] 初版程序 卡壳ing
	- [ ] 升级版
		- 记录常用查询的城市名称，打开程序自动输出

### 1 探索记录
- 今天投入多长时间练习编程,探索了哪些技能点,分别花费了多少时间、探索到什么程度
	- 天气查询程序 (3h)

- 建议详细记录自己完成的折腾历程、相应时间，以便挖掘时间黑洞，改善自己的学习效率
	- 整体的折腾过程：

        - 对于程序的框架只有一个模糊的想法，觉得不难，从逻辑最简单的开始入手，决定先实现从 txt 文件读取数据的函数。看了`open()`函数的文档，测试了以`r`和`rb`两种模式读取数据，实现函数 (0.5h)

        - 写程序运行的主函数，按流程走一遍，确定需要的函数以及代码(2.5h)
            - 读取本地 txt 文件的函数
            - 创建日志文件的函数(之后决定改用 list 保存log)
            - 循环
            - 获得用户输入
            - 根据用户输入，选择不同的响应函数（按功能分为执行 command 和 查询天气这两类）
            - 响应函数怎么写
    - 主要卡在了怎么根据用户输入来调用不同的响应函数，以及响应函数如何写。因为不想使用 if/elif/elif/... 来判断，希望使用下面这种方式调用响应函数，这样如果有新的command，只需要定义对应函数，并放入字典即可，易扩充。
    ```python
    dt = {'help': help}
    response = dt['help']
    response()
    ```

### 2 复盘 & 改进：
- 今天有哪些收获？
	- 与 Vwan 进行互评，获得了非常认真的评价，指出了不足和建议！很开心！！
	- 被告知测试的代码与被测试的代码可以分开文件，我觉得是个好的想法

- 有哪些有用的经验、技巧可以在未来复用
	- 不管代码再怎么丑，先实现了再说。因为实现一遍，才能知道里面会有哪些难点，才能在优化的时候有的放矢，效率应该会高。

- 哪些地方做的不好？打算如何改进？
	- 发现自己对于时间的记录不准确，没有记录学习开始和结束的时间，没有什么管理时间的概念。这间接导致写天气查询程序时，觉得时间很多，于是思维会各种发散。自己觉得这样好像更好，那样也能实现需求，不断挖坑，导致今天花了3h还没把天气查询程序写出来。
	- 主要问题有两点，也从这两点入手改进，明天试一下：
		- 如要准备写代码，那么先构思好流程和需要的函数
		- 如果没有很厉害的构思，那么先按直觉来写，不管代码美丑
		- 如果开始写代码，那么限定时间 1h ，像考试一样给自己压力，目标是先实现出来


# 170815 1wd2

#### 0.1 基本任务
- 思考 Vwan 对自己提出的建议并回复
	- [x] 对于输入合法性规则的界定（输入首位可否为0） 
	- [x] docstring 放函数内还是外，以及 style，推荐reST风格 (0.5h)
	- [x] 判断用户输入try/except or str.isdigit()(0.5h)
	- [ ] 判断用户本次输入不合法时，下次判断是递归/循环？效率？易读？其他，结合教练之前提出的问题，即从可能产生的影响评价递归
	- [ ] 从可能产生的影响评价递归程序
        - [ ] 健壮性
        - [ ] 效率
        - [x] 可读性
        - [x] 其他可能发生的事情
	- [x] if是否必须带else？ [编程的智慧](http://www.yinwang.org/blog-cn/2015/11/21/programming-philosophy)。结合情景while True
	- [ ] 测试代码放哪里，以及如何测试。(推荐的关键词：python test framework;pytest和python自带的unittest)

- ch1 天气查询程序
	- 初版程序
		- [ ] ~~if/elif/elif 流派, 没采用~~
		- [x] 函数式
		- [x] 添加类
		- [ ] 看同学代码
			- [x] guo2sky
			- [ ] 

- Python 编码
	- [x] 查询一些编码知识，每天进步一点点(自己查到[源头Unicode编码中文字符表](http://www.unicode.org/charts/PDF/U4E00.pdf))


### 1 探索记录
- 今天投入多长时间练习编程,探索了哪些技能点,分别花费了多少时间、探索到什么程度
	- 思考 Vwan 的建议，查阅资料及编写回答 **(3h)**
	- 思考了天气查询代码思路，用类+函数实现 **(5h) **

- 建议详细记录自己完成的折腾历程、相应时间，以便挖掘时间黑洞，改善自己的学习效率
	- 答复 Vwan
        - docstring 部分，推荐了新的style，指出了其位置放在函数外的问题 **(0.5h)**
        - 判断用户输入使用 try/except or str.isdigit **(0.5h)**
            - 查文档了解 try/except：[Errors and Exceptions](https://docs.python.org/3.6/tutorial/errors.html) 
            - google 看其他人怎么写：[Asking the user for input until they give a valid response](https://stackoverflow.com/a/23294659)
        - 使用递归还是循环获得用户输入，评价下递归程序**(1.5h)**
            - 15:40-16:20，查到递归一些资料并阅读
            - 16:20-16:40 自己使用循环和递归斐波那契数列，比较效率
            - 16:40-17:00 看文章，未完
            	- [比较循环和递归生成Fibonacci数列的效率](http://www.python-course.eu/recursive_functions.php) 代码的效率其实与实现方式也有关，优化前递归比循环慢很多，优化后比循环还快
            	- [Recursion or while loops](https://softwareengineering.stackexchange.com/a/182334) 
        - 正好看到 Vwan 最新的猜字游戏代码，提了2个小建议 **(0.5h)**
            - 变量命名
            - 包的导入，代码用了`import sys`，[PEP8](http://legacy.python.org/dev/peps/pep-0008/#imports) 建议使用`import sys.exit` 或 `from sys import exit`

	- 天气查询程序
		- 17:28-18:00 写到如何判断输入是中文这一步，思路以utf-8编码确定，后改为Unicode **(0.5h)**
		- 18:00-19:30 查资料，记笔记 **(1.5h)**
			- [阮一峰：字符编码笔记：ASCII，Unicode和UTF-8](http://www.ruanyifeng.com/blog/2007/10/ascii_unicode_and_utf-8.html) 从这里面找到下面的对照表的链接
			- [Unicode中文字符与十六进制对照表](http://www.chi2ko.com/tool/CJK.htm)，找到中文编码对照表，定出范围(十六进制4E00-9FA5)，但该网站是2002年
			- [Unicode的官网](http://unicode.org/)，找到最新的标准里中文编码范围(十六进制4E00-9FEA)
			- 测试python3中Unicode字符表中中文的范围是**4E00-9FA5**还是**4E00-9FEA**，结果挺奇怪的，`9FA5`为`龥` ,其他都显示不正常。因为编码知识还不够过硬，我也不知道怎么回事，但是已经知道**4E00-9FA5**是中文编码范围，可以开动了
			- ```
			>>> int('9FA5',16)
40869
>>> chr(40869)
'龥'
>>> int('9FEA',16)
40938
>>> chr(40938)
'\u9fea'
>>> print(chr(40938))
CLI环境下这里显示空行，但是有东西可以复制，复制出来粘贴在这里显示为: 鿪
>>> chr(40870)
' '
>>> print(chr(40870))
CLI环境下这里是空行，但是有东西可以复制，复制出来粘贴在这里显示为:龦
>>> print(chr(40871))
CLI环境下这里是空行，但是有东西可以复制，复制出来粘贴在这里显示为:龧
			 ```
			- 19:30-19:50 关于怎么判断字符这块，也是遇到了坎，涉及用户输入后，python保存下来的字符串如何与'\u4e00'比较，最后以先完成目标为主，先查了别人的方案 **(0.5h)**
        - 20:25-21:44 根据用户的输入，调用不同的响应函数，以及其他细节，初稿完成 **(1.5h)**
        - 22:00-23:00 优化代码，去除重复部分 **(1h)**

### 2 复盘 & 改进：
- 收获
	- 从源头找到了 Unicode 的中文编码字符表，增强信心
	- 初步用类+函数的方法实现了天气查询系统，并且按昨天的复盘时的改进计划，记录了所花时间
	- 开始了解递归
- 经验、技巧
	- 发现Scott教练也用了改建工具，提高效率，想起来上次哪位教练打字好像用的是**双拼**，这个也可以学一下，提高打字速度
- 哪些地方做的不好？打算如何改进？
	- 仍然是效率不是很高，时间很容易就流逝了。比昨天好一点是记录了学习或做每件事时的起始时间，发现花了挺多时间，现在想想很容易在搜索资料时误入知识海洋，迷失当初的方向，可能是今天没有按昨天计划的定个小目标：多少时间内完成什么事，明天要加油呀！！
	- **如果**开始做事，**那么**给手机设置倒计时，时间到记录总结！


# 170816 1wd3

#### 0.1 基本任务

- [x] 继续昨天的递归阅读 [Recursion or while loops](https://softwareengineering.stackexchange.com/a/182334)
- [ ] 完成 Vwan 同学的 comment
- [ ] ~~学会 Github 在 commit log 中 如何@用户~~
- [ ] 了解 leetcode 是什么
- [ ] 图解HTTP的 HTTPS章节

- 程序改进
    - [ ] 打开文件这个可能出错，异常捕获
    - [ ] 思考其他地方有误异常
    - [ ] 教练说提升性能，节省内存。可以看看标准库 `csv` 或 `collections`，当初看到逗号分隔也想过 `csv`的
    	- [x] csv
    	- [ ] coolections
    	- [ ][Pandas 处理上亿数据，分区读取](http://www.justinablog.com/archives/1357) 
    	- [ ] 多线程，分别读取数据和获得用户输入？线程间通信？
    - [ ] 关于导入数据这块如何降低内存使用，可以根据拼音or字符十六进制排序，然后起始范围及分布密度把文件按行分为几部分或者分为几个文件，读取时候只在小范围内搜索；按拼音应该好一点，这样只有至多26部分


### 1 探索记录
- 今天投入多长时间练习编程,探索了哪些技能点,分别花费了多少时间、探索到什么程度
- 建议详细记录自己完成的折腾历程、相应时间，以便挖掘时间黑洞，改善自己的学习效率

今天花时间比较多在怎么优化打开文件，获取数据的代码。
#### 1.1 根据scottming教练建议，采用`csv`模块
```python
def line_read():
    path = '../resource/weather_info.txt'

    dt = {}
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            weather_ls = line[:-1].split(',')
            city = weather_ls[0]
            weather = weather_ls[1]
            dt[city] = weather


def csv_read():
    path = '../resource/weather_info.txt'
    dt_csv = {}
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for k, v in reader:
            dt_csv[k] = v


def test():
    from timeit import timeit
    t1 = timeit(line_read, number=1000)
    t2 = timeit(csv_read, number=1000)
    print(f"line_read duration:{t1}")
    print(f"csv_read duration:{t2}")

if __name__ == '__main__':
    test()
```

结果：
```
line_read duration:4.25393801847622s
csv_read duration:2.73559814727247s
```

#### 1.2 尝试读入二进制数据，不解码

10:14-11:00 继续探索读取文件
- 测试使用`binary`模式读取数据，如果没有用`utf-8`解码，时间上快了一点点；解码，时间很慢。使用`cprofile`测试看到，因为是一行行的解码，需要调用2000+次解码
- csv 读取，`codecs.utf_8_decode`完成`utf-8`解码，时间和使用`binary`模式读取数据但不解码差不多；`cprofile`测试看到，其读取和解码均调用了6次

#### 1.3 继续尝试读入二进制数据，解码

11:00 -11:50 
- 感觉csv是分6次读取了文件，所以试着将 buffering 和 binary 结合在引起，分n次读取，n次解码, n次split，n次放入dt中。代码如下：


```python
def file_read_binary_no_decode_no_buffering():
    path = '../resource/weather_info.txt'

    dt = {}
    with open(path, 'rb') as f:
        for line in f:
            line = line[:-2] #.decode('utf-8')
            weather_ls = line.split(b',')
            city = weather_ls[0]
            weather = weather_ls[1]
            dt[city] = weather
    return dt


def file_read_binary_buffer_and_decode(buff_size):
    path = '../resource/weather_info.txt'
    dt = {}

    with open(path, 'rb', buffering=buff_size) as f:
        binary_data = f.read()
        unicode_str_2 = binary_data.decode('utf-8')
        unicode_ls = unicode_str_2.split('\r\n')
        dt.update(tuple(s.split(',')) for s in unicode_ls)

    return dt


def csv_read():
    path = '../resource/weather_info.txt'
    dt_csv = {}
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for k, v in reader:
            dt_csv[k] = v
    return dt_csv
```
`timeit` 的结果如下，两次结果不同是因为函数调用次数不同，次数更多是想看看会不会差距随次数线性增长，发现自己弄的二进制加解码的函数与csv的差距不是很大，buffering size不同没什么区别
- 每轮调用测试xx次，忘记了，时间如下：
```
csv_read duration:8.76368728597946 s
line_read_binary_buffer_and_decode:0 duration:8.945624853875456 s
line_read_binary_buffer_and_decode:100 duration:8.71083041692042 s
line_read_binary_buffer_and_decode:500 duration:8.174304852368117 s
line_read_binary_buffer_and_decode:1000 duration:8.117085621182781 s
line_read_binary_buffer_and_decode:5000 duration:8.543890444174046 s
line_read_binary_buffer_and_decode:8192 duration:8.366376018110735 s
```

17:00-18:10 测试加提交comment 给上海MeetUp的复盘

- 每轮调用测试1000次，一共测试3轮，平均时间如下：
```
csv_read duration:3.7020451830934626 s # csv.reader
line_read duration:5.692423350374611 s # 按行读取，'r'模式打开
# ’rb‘模式， f.read()->解码->split2次->字典
file_read_binary,decode and buffering size:0 duration:4.391810029110776 s
file_read_binary,decode and buffering size:100 duration:4.518201833737247 s
file_read_binary,decode and buffering size:1000 duration:4.32692256003583 s
file_read_binary,decode and buffering size:8192 duration:4.261893271645978 s
file_read_binary,decode and buffering size:100000 duration:4.190836932504946 s
# ’rb‘模式， f.read()->split2次->字典
file_read_binary, no decode and buffering duration:3.440408401808431 s
```

- 每轮调用测试10w次，一共测试3轮，平均时间如下：
```
csv_read duration:273.49713018486347 s
file_read_binary,decode and buffering size:0 duration:281.93313800086366 s
file_read_binary,decode and buffering size:100 duration:281.1990550241383 s
file_read_binary,decode and buffering size:1000 duration:324.62182393955965 s
file_read_binary,decode and buffering size:8192 duration:295.319070092103 s
file_read_binary,decode and buffering size:100000 duration:307.31232205896777 s
file_read_binary, no decode and buffering duration:278.1384226747744 s
```

#### 1.4 总结：
- 总体时间：`csv`模块 <`'rb'`模式打开然后整块读取转码 < 以`'r'` 模式打开并按行读取
- 问题：buffering=0,1000,10000没感到什么差别，不知为何
- 后来在Jupyter又测了，循环100次取最好3次结果均值，三者速度大概是 3ms:4ms:5ms
- 可以改进的地方：
	- 自定义函数加buffer后读取时候是否是一整块读取的；
	- 使用`collections`

### 2 复盘 & 改进：
- 收获
	- 自定义的打开csv格式文件读取数据放入dict的函数，从时间上看与 模块`csv`差不多，增加了点信心，但是不知道还有没有从其他角度进行评估，内存？
	- 了解了尾递归(tail recursion) 和 一般递归的差异，但是还不够深刻，涉及堆栈这些比较底层的细节概念模糊，准备跳过
- 经验、技巧
	- 看 Hugo1030 的ipynb文件，发现在`cell`头部写上`%%time`可以输出单元代码运行时间，在函数调用前加`%timeit` ，如`%timeit file_read_binary_buffer_and_decode(0)` ，能调用`timeit`模块，这太方便了
	- 百度到了[27个Jupyter Notebook小提示与技巧](http://blog.csdn.net/simple_the_best/article/details/52821136)
	- 从 Vwan 同学那儿借鉴来的 `cprofile` 模块，可以测试函数运行时，对其他函数的调用统计（包括次数和时间），这有助于了解一些标准模块的思路，比如看到 csv.reader 函数读取数据时候使用了`_codecs.utf_8_decode` 完成解码，并调用了7次。猜测是将数据分7次导入，不知道对错，但给我自定义的读取文件的函数提供了思路，即不要一行行读取，当做一个整体分次读取，然后统一解码

```
-----------csv_read-----------
         22 function calls in 0.014 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.014    0.014 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 codecs.py:259(__init__)
        1    0.000    0.000    0.000    0.000 codecs.py:308(__init__)
        7    0.000    0.000    0.001    0.000 codecs.py:318(decode)
        1    0.003    0.003    0.014    0.014 utils.py:180(csv_read)
        7    0.001    0.000    0.001    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.000    0.000 {built-in method _csv.reader}
        1    0.000    0.000    0.014    0.014 {built-in method builtins.exec}
        1    0.010    0.010    0.010    0.010 {built-in method io.open}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```
- 问题
	- 今天投入时间不是很多，有点茫茫然的过了一天，设定的目标完成度也不高，总体来说状态不好。身体有点疲劳。
	- 在提高数据读取上执念过深，然后有`timeit`这个工具后总是测，没按既定路线`csv`-->`collections`->`pandas` --> stackoverflow 走下去；然后自己中断工作次数过多

-  提高
	- 明天上午的安排，今晚做出来。当明天早上开始工作时，按照计划来

# 170817 1wd4

#### 0.1 上午任务


- [x] 递归继续 google，关键词：`python recursion advantage/disadvantage`
- [ ] 完成 Vwan 同学的 comment中递归部分，提交

#### 0.2 下午任务
- [ ] ~~把 `get_input()` 放入 `User` 类~~
- [ ] 阅读 [27个Jupyter Notebook小提示与技巧](http://liuchengxu.org/pelican-blog/jupyter-notebook-tips.html)，换下脑袋，轻松下
- [ ] 文件读取按既定路线`csv`-->`collections`->`pandas` --> stackoverflow 走下去
- [ ] 了解`open()的参数buffering`有什么用，为何之前的测试改变它对时间影响几乎为零
- [ ] 了解 leetcode 是什么

#### 0.3 晚上任务
- [ ] 图解HTTP的 HTTPS章节
- [ ] pytest + [doc](https://docs.pytest.org/en/latest/getting-started.html#grouping-multiple-tests-in-a-class)
- [ ] 天气查询网络版，网络请求+数据保存


### 1 探索记录
- 今天投入多长时间练习编程,探索了哪些技能点,分别花费了多少时间、探索到什么程度
- 建议详细记录自己完成的折腾历程、相应时间，以便挖掘时间黑洞，改善自己的学习效率

	- 递归 (3h)
        - 11:20-12:20 谷歌->Stack Overflow -> [wisc大学cs课程教案](http://pages.cs.wisc.edu/~vernon/cs367/notes/6.RECURSION.html)
        - 17:33-19:00 继续理解教案，做笔记；看Stack Overflow一些回答
            - [What are the advantages and disadvantages of recursion?](https://stackoverflow.com/questions/5250733/what-are-the-advantages-and-disadvantages-of-recursion) 
            - [recursion versus iteration](https://stackoverflow.com/questions/15688019/recursion-versus-iteration)
            - [Guido's blog:Tail Recursion Elimination](http://neopythonic.blogspot.jp/2009/04/tail-recursion-elimination.html)
        - 22:20-23:00 《Python数据结构与算法》 学习递归部分，实现背包取物满足一定的重量的算法

### 2 复盘 & 改进：
 - 简单记录一下，今天主要时间花在了递归上，差不多从表象上明白了递归与循环二者在使用时候的优劣
 - 经验技巧：发现一些大学的教案文件写的挺清晰易懂的，对比之下《python数据结构与算法》一书同样的知识点表述的能力就稍差一点；Stack Overflow大家回答里给的参考资料往往会更有价值
 - 做的不好的地方：跟昨天一样的状态无力，任务大量没有完成，不知如何解决，明天尝试完成递归的总结后，推进今天遗留的任务吧


# 170818 1wd5

#### 0.1 上午任务


- [x] 完成 Vwan 同学的 comment中递归部分，提交

#### 0.2 下午任务
- [x] 图解HTTP的 HTTPS章节
- [ ] ~~把 `get_input()` 放入 `User` 类~~
- [x] 阅读 [27个Jupyter Notebook小提示与技巧](http://liuchengxu.org/pelican-blog/jupyter-notebook-tips.html)，换下脑袋，轻松下
- [ ] 文件读取按既定路线`csv`-->`collections`->`pandas` --> stackoverflow 走下去
- [ ] 了解`open()的参数buffering`有什么用，为何之前的测试改变它对时间影响几乎为零
- [ ] 了解 leetcode 是什么

#### 0.3 晚上任务
- [ ] 天气查询网络版，网络请求+数据保存
- [ ] pytest + [doc](https://docs.pytest.org/en/latest/getting-started.html#grouping-multiple-tests-in-a-class)



### 1 探索记录

- 回答 commandfunc 设计的问题 (0.5h 查 + 0.5h 写)
	- [Vwan 同学提出来的程序设计思路中的问题](https://github.com/thxiami/Py101-004/commit/bae7e515f0fedccf8eca5dbd566ced53028a6306#commitcomment-23695277)，，她看问题的点很准，沉下心去思考思考，还是很难回答完整。
		- 关于代码中commandfunc的类似路由的封装设计，她提出来的funcname or commandname 是写死在 code中，这的确是个问题，她希望能找到best practice，比如参考一些其他的程序是如何设计。今天谷歌了一些关键词：python CLI input interactive program，花了约 0.5h 没找到合适的例子，暂时搁置了。
        ```
        command_function_dt = {
            'help': print_help,
            'history': print_history,
            'quit': quit,
        }
        ```
		- 给了她使用 json 保存一些程序配置文件的例子，如天气数据的 path 可以放入 json 中，然后在脚本中导入为 dict。写例子大约 0.5h


- 递归总结 （1h)
	- 终于完结了递归的查询和小结，并回复给了Wangjunyu教练之前参与的一个[issue](https://github.com/AIHackers/Py101-004/issues/23#issuecomment-323377521)中，但感觉仍不得门道，可能需要看一些书籍+实际问题码代码才能了解更多
- 看了 ch0 作业讲解的卡包 （0.5h）

### 2 复盘

- 卡包学习
    - 从 Scottming 教练学到了看官方文档的方法
    - 从 Scottming 教练学到了一种使用 yield 方法的猜数字游戏方案，准备再看看
    - 从 Wangjunyu 教练学到了头部添加`__version__ = v170819.0005`,（v+日期+时间），`__author__=thxiami`，便于自动生成文档时调用

- 与同学讨论
	- 尝试寻找别人写的命令行程序，目的是为了看看别人是怎么实现当用户输入`help`，`quit`,`history`命令，程序作出对应的处理。时还没有摸到门路，但是有了方向



# 170819 1wd6

#### 0.1 上午

- 与教练沟通学习
- 文件读取添加方法`json`

#### 0.2 下午

- 搜索查找Pyrhon中文社区--> 应该是 [华蟒](https://groups.google.com/forum/#!forum/python-cn)
- `json`方法配合二进制打开文件，测试文件读取不同方法速度

#### 0.3 晚上
-  提出[issue：ch1 任务难点「如何更好实现用户指令查询功能」的思考](https://github.com/AIHackers/Py101-004/issues/64), 理解教练的建议方法



### 1 探索记录
- 文件读取
	- 14:20-15:40 新增了 json 读取的想法，封装了测试时间函数，增加了 json, read(readsize)两种方法
        - 测试参数：共 3 轮，每轮调用函数 5000 次的，每轮平均用时
        - 总结：按行读取影响速度，如果按行解码会更影响速度，缓冲好像有用。
        - 速度由快至慢：
        	- json
        	- csv >= open(缓冲+'rb')+一次性读取+str解码
        	- open(不缓冲+'rb')+一次性读取+str解码
        	- open(不缓冲+'r')+ 按行读取
    - 15:40 -18:00 对于 json 以二进制方式读取数据，看看是否会更快。主要时间用来封装测试函数，改变输出时的文字格式，真是失误。
    	- 测试参数：共 3 轮，每轮调用函数 5000 次的，每轮平均用时
    	- 测试结果：
        ```
        ----------以下采取缓冲方式打开文件----------
        -----'rb'模式 打开 | read方式: f.read() | 是否解码：是-----
        buffering=0,     时间=14.496 s
        buffering=1,     时间=15.132 s
        buffering=100,   时间=13.780 s
        buffering=1000,  时间=14.502 s
        buffering=10000, 时间=13.269 s
        buffering=50000, 时间=14.343 s
        最快：buffering=10000, 时间=13.269 s

        ----------以下均采取不缓冲方式打开文件，自己操作字符串获得数据----------
        ---'r' 模式 打开| read方式: for line in file | 是否解码：open时解码| 时间= 22.391 s---
        ---'rb'模式 打开| read方式: for line in file | 是否解码：是| 时间= 33.336 s---
        ---'rb'模式 打开| read方式: for line in file | 是否解码：否| 时间= 14.972 s---
        ---'rb'模式 打开| read方式: f.read(readsize) | 是否解码：是|---
        readsize = 1000 | 时间= 17.245 s-----
        readsize = 5000 | 时间= 17.586 s-----
        readsize = 10000| 时间= 15.160 s-----
        readsize = 50000| 时间= 14.776 s-----
        最快：'rb'模式+f.read(50000)+str解码，时间= 14.776 s

        ----------以下均采取不缓冲方式打开文件，采用csv/json模块处理数据----------
        ---'r' 模式 打开 | csv.reader 模块 | 是否解码：open 时解码    | 时间= 13.773 s----
        ---'r' 模式 打开 | json.loads 模块 | 是否解码：open 时解码    | 时间= 9.522 s----
        ---'rb'模式 打开 | json.loads 模块 | 是否解码：json 载入时解码 | 时间= 8.747 s----
        最快：'rb'+json.loads(data, encoding="utf-8"), 时间= 8.747 s 
        ```

    	对比 json两种方法：`'r'`模式打开文件，`open()`时解码；`'rb'`模式打开文件，`json.loads(data, encoding='utf-8')`解码。二者时间差异很短，为确认速度差异是否存在, 调用次数由5000次 -> 60000次，才能比较出差异是由误差导致还是的确存在，结果如下：
        ```
        ---'r' 模式 打开 | json.loads 模块 | 是否解码：open时已解码|  时间= 116.788 s---
        ---'rb'模式 打开 | json.loads 模块 | 是否解码：json载入时解码| 时间= 104.865 s---
        ```
		二者的确会有差异
- 总结：
	- 最快的方式：将数据保存为 json 格式，以二进制方式open文件，配合json.loads(data, encoding="utf-8") 读取数据获得字典。（但使用前需将数据以json格式存至文件）
	- 待补充


### 复盘之收获
- 今天是学编程以来**里程碑式**的一天，和 Wangjunyu 教练进行了沟通，增强了自己的信心，将教练建议总结如下：
    **教练的建议：**
    - 短期：
        - [ ] Mac or Linux 编程
            - 虚拟机+Ubuntu 
        - [ ] 可以发起一个在线活动
    - 17.08-17.11 约3个月时间
        - 全勤做出高质量项目
            - 文献追踪软件
        - 写高质量技术博客
            - [ ] 搭建个人博客： Python + Pelican + 托管Github
            - [ ] 记录探索过程：系统记录自己探索新知识的过程
    - 长期
        - 需要更了解开源社区，知道如何借助这种力量做更多实践
            - [Zoom.Quiet 荔枝FM](https://www.lizhi.fm/box#play)
            - [Zomm.Quiet博客](http://zoomquiet.io/)
            - [Python中文社区]()
            - [浚宇的博客](http://blog.junyu.io/)
        - 如果目标是顶级程序猿，熟悉英文环境，告别中文
            - 用 google，弃 百度
            - 看文档

- 提出了开课来自己的第一个issue：[ch1 任务难点「如何更好实现用户指令查询功能」的思考](https://github.com/AIHackers/Py101-004/issues/64), 与教练讨论了如何封装用户指令查询函数，获得了宝新方法：可封装在User类，学到了一种设计理念和`getattr`,`hasattr`,`callable`三个内置方法。
> 关于如何实现用户指令查询功能，教练提供了另一种思路（详见上方代码），把指令对应的功能封装在实例方法里（），通过hasattr, getattr 和 callable 方法，根据给出的command name 判断实例是否有对应实例方法，有的话就调用，没有就说明时查询天气。这个方法很棒！学习啦！以下为根据教练的思路写的代码：

    ```python
    class User():
        def __init__(self):
            pass

        def help(self):
            doc = "Help doc"
            print(doc)

    user = User()
    command_input = 'help'
    command_func = getattr(user, command_input, None)
    if command_func and callable(command_func):
        command_func()
    else:
        ... # 调用查询天气的函数
    ```

    运行结果：```Help doc```

- Scottming 教练在微信群分享了一些[代码风格资料](https://github.com/thxiami/Py101-004/blob/master/Chap1/note/Study_note.md)

### 复盘之改进
- 问题：正如 NBR-hugh 同学在 issue [ch1 任务难点「返回该城市天气数据」的思考](https://github.com/AIHackers/Py101-004/issues/42#issuecomment-323530954)下的回答里指出的：当前阶段不应该把主要时间花在性能评价及提升上，而应该学习范例，看文档，完成个人 MVP 开发。因为目前阶段属于坐井观天阶段，对于性能：如何评估；如何提升及是否有价值都无法做出准确的判断
- 改进：应当及时止损，对于文件读取的坑止步于
	- 了解`open`的`buffering`有何作用
	- 了解运用`collection`内提供的数据类型`deque`
	- 总结探索的过程，链接形式放入个人教程

# 170820 1wd7

### 0 探索记录
- 上午
	- Jupyter 中 reload moudle 问题 (1.5h)
- 下午
    - buffering 的作用 (1h)
    - open() 以 'r' 和 'rb' 真的会有速度差异吗 (1.5h)
- 晚上
    - 查看 issue，与同学讨论ch1实现 (0.5h)
    - 整理 ch1 个人教程 (4h)
    - 当天记录 (1h)


#### 0.1 Jupyter 中 reload moudle 问题
问题及探索过程见 [问题：ch0作业《LPTHW》ex25，调用函数报错“变量未声明](https://github.com/AIHackers/Py101-004/issues/65)
#### 0.2 buffering 的作用

- 概念通过官方文档和[What is the use of buffering in python's built-in open() function?](https://stackoverflow.com/a/29712601)了解 0.5h
- 看视频[Python: How to open Big Data Files Buffering Tutorial](https://www.youtube.com/watch?v=i2DHWxtRqpE)（17min），记录别人实战读取大文件（文件大小：2.5G和50G，内存：16G），真实感受其作用 0.5h
- 疑问点：还不知缓冲大小对处理数据是否有影响？在什么情况下有影响？影响多大？

#### 0.3 open() 以 'r' 和 'rb' 真的会有速度差异吗
- Google到个人博客并阅读 1h
	- [Reading ASCII file in Python3.5 is 2-3x faster as bytes than string](http://www.dalkescientific.com/writings/diary/archive/2016/08/03/bytes_and_unicode_read_performance.html) 'r' 和 'rb'打开文件，比较速度差异，思路较科学严谨，但作者也不知速度差异原因。
	- [python-file-reading-benchmarks](https://nelsonslog.wordpress.com/2015/02/26/python-file-reading-benchmarks/) 做了Python2，3 不同打开模式的速度比较，包括以前我未知的方式codecs.open()
	- [io.open vs. codecs.open](https://mail.python.org/pipermail/python-list/2015-March/687124.html)，In Python 2, built-in open doesn't take an encoding argument,
so if you want to use something other than binary mode or the default
encoding, you were supposed to use codecs.open
- 个人探索 0.5h
    - 测试结果
        - open('r'):0.36s
        - open('rb'):0.14s
        - codecs.open('r'): 0.29 s
        - codecs.open('rb'):0.14 s
    - 总结
        - codecs.open('r') 比 open('r') 要快
        - codecs.open('rb') 与 open('rb') 同样速度
- 这一部分进一步讨论待补充，会放在专门的笔记中

### 1 复盘之收获
- 知道了 buffering 在读取大文件（GB级别或超过内存大小）的作用，以及如何使用
- 看Youtube英文视频可选择生成字幕，准确度还算不错
- 除了Stack overflow，一些个人博客会详细记录发现问题、解决问题的过程，可适当增加看个人博客的权重，不用一直盯着Stackoverflow
- 发现学友 [NBR-hugh](https://github.com/NBR-hugh/Py101-004/) 不管[回答问题](https://github.com/AIHackers/Py101-004/issues/64#issuecomment-323538602)还是[记录笔记](https://github.com/NBR-hugh/Py101-004/blob/master/Chap1/note/CH1_WeatherInquiry_ExploringRecord.ipynb)，逻辑清晰，结构也很好，模仿学习其框架。他给出笔记要点：
    - overview 整体概览
    - 运行环境
    - 代码为先,少说废话
    - 多写思路,少写情绪
    - 错误解决记录
    - timelog
- 发现可以通过浏览器历史记录来帮助自己回忆当天探索的内容和大概起止时间


### 2 复盘之改进
发现自己花在记笔记的时间有点多，个人教程一项就花了4个多小时，还未完成。当日笔记也花了1h左右。
在未来几周的任务完成过程中，是不是也应该像学友 NBR-hugh 在Jupyter中完成调试，并记录一些思路，这样最后总结个人教程时就不至于从0开始。当日探索也是，应该探索完简单记录几句话和代码，代码运行结果等碎片记录。
如果在探索，探索中碎片记录放入md文档。
如果在写当日笔记时，先不管格式问题，先填内容，最后解决格式。