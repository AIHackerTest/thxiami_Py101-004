~ 用于存放本周任务成果。

## Feature

----天气资料由「心知天气」提供----
- 输入指令 h 或 help，打印帮助文档；
- 输入指令 q 或 quit，退出本程序；
- 输入指令 c 或 C，将温度显示单位设定为摄氏度, 程序启动后默认单位为摄氏度；
- 输入指令 f 或 F，将温度显示单位设定为华氏度；
- 输入指令 now，进入查询实时天气模式， 程序启动后默认为该模式；
	- 该模式下，输入城市中文名或拼音回车，程序返回实时天气情况
	- demo：输入`future`切换至该模式，输入`beijing`后确定, 返回北京的实时天气
- 输入指令 future，进入查询未来多日天气概况查询模式；
	- 该模式下，输入城市中文名或拼音后回车，需继续输入天气查询的起始日期和天数
	- 输入格式：`起始日期,天数`
	- 输入说明
		- `起始日期`为阿拉伯数字，范围为`0-14`，比如`0`代表当天，`1`代表明天，以此类推;
		- `天数`为阿拉伯数字，范围为`1-15`，比如输入`2`代表查询从起始日期算起的 2天的天气
    - demo: 输入`future`切换至该模式，`beijing`后确定，接着输入`0,3`，程序返回北京市今天，明天和后天的天气概况
- 输入指令 history，打印查询过的所有城市。

## Require

- Python 3.6
- requests 2.14.2
- prompt_toolkit 1.0.14

## Usage

- 下载
	- [weather_oh_know_online.py](https://github.com/thxiami/Py101-004/blob/master/Chap2/project/weather_oh_know_online.py)
	- [utils](https://github.com/thxiami/Py101-004/blob/master/Chap2/project/utils)文件夹下所有脚本文件
	- [data](https://github.com/thxiami/Py101-004/blob/master/Chap2/project/data) 文件夹下的所有文件

- 运行
	- 使用 Python 启动 weather_oh_know_online.py
	- 跟随程序提示输入即可

## Development record

- 待补[]()

## Future
- 更改多日查询的输入方式，与实时查询统一在一个入口。输入格式：
	- `北京` ->查询实时；
	- `北京,3` ->未来三天的天气预报;
	- `北京,1,3` ->从明天起未来三天的天气预报
- 城市是否存在的查询可用 和风天气api提供city search api
- json 解析可用 Vwan 改进的 `objectjson`
	- 代码: [objectjson.py](https://github.com/Vwan/Py101-004/blob/master/Chap2/project/objectjson.py)
	- 设计思路：[Exercise Notes](https://github.com/Vwan/Py101-004/blob/master/Chap2/note/Exercise%20Notes%20-%20chap2.md)

## Update


- V17.08.29.2400
	- Features
		- 新建 `User` 类
			- 将与用户相关的变量作为实例属性，包括用户本次输入，查询历史，当前温度显示单位，当前查询模式及调用API时所需参数等
			- 将部分指令功能的实现封装为实例方法
        - 使用 `dict` 储存指令函数变量，指令函数的调用方式由`dict.get(command, default_function)`代替`if/elif/.../else`，可减少条件复杂度
        - 增加了城市拼音名的输入自动补全功能
	- Style
		- 根据 Review 报告，更改代码格式以符合 PEP8 规范

- V17.08.25.1825
	- Features
		- 使用 `os.path` 补全文件路径，便于项目整体迁移
		- 由`print(help_doc)`替换`print_help()`函数实现`help`指令功能
	- Style
		- 根据功能，将主程序脚本内和`utils.py`内函数放入`utils` package下的`command_fun.py`,`query_func.py`,`completer.py`
		- 将定值变量或程序默认配置参数变量放入`const_value.py`中
- V17.08.25.0230
	- Feature
		- 增加了在输入时自动补全功能，目前支持自动补全输入历史，城市中文名，指令
	- Style
		- 去掉 `fetch_weather(api_params_dict, api_url=api_url,)`传入参数最后的逗号
		- 模式 `daily` 改为 `future`

- V17.08.24.1140
	- Style
		- 修改了帮助文档
- V17.08.24.1000
	- Fixed bugs
		- 解决了因重定义`fetch_weather()`传入参数，调用时未作出对应修改而导致的程序查询异常
- V17.08.23.2200
	- Style
		- 程序输出文本时，在文本前后各加入`\n`，可以隔开上下文便于观察本次输出结果
- V17.08.23.1800
	- Features
		- 增加温度转换功能，可指定温度单位为摄氏度或华氏度
		- 增加查询指定日期天气功能，可指定起始日期和从起始日期算起指定天数的天气概况
	- Fixed Bugs
		- 给 requests.get 增加了异常判断，可捕获异常`requests.exceptions.ProxyError` 和 `requests.exceptions.Timeout`

- V17.08.22.1500
	- Features
		- 实时查询制定城市天气, 数据来源为[心知天气](https://www.seniverse.com)