# CH1 天气查询程序说明

## Feature

- 输入中文城市名，返回该城市的天气数据
- 输入指令 help，打印帮助文档
- 输入指令 histroy，打印天气查询历史
- 输入指令 quit ，退出程序的交互，并打印天气查询历史

## Require

- Python 3.6

## Using

- 下载程序脚本文件和数据库文件
	- [weather_forecast.py](https://github.com/thxiami/Py101-004/blob/master/Chap1/project/weather_forecast.py)
	- [command_function.py](https://github.com/thxiami/Py101-004/blob/master/Chap1/project/command_function.py)
	- [user.py](https://github.com/thxiami/Py101-004/blob/master/Chap1/project/user.py)
	- [utils.py](https://github.com/thxiami/Py101-004/blob/master/Chap1/project/utils.py)
	- [天气数据文件](https://github.com/thxiami/Py101-004/blob/master/Chap1/project/weather_json.txt)
- 运行
	- 使用 Python 启动 weather_forecast.py



## Development record

- [ch1_Development_record](https://github.com/thxiami/Py101-004/blob/master/Chap1/note/ch1-Exploring%26Record.ipynb)

## Update

### v170821.1150

- Bug fixed
	- command_function.py 
		- 原`quit` 指令对应函数名为 `quit()`，覆盖了内置同名函数，改为`quit_()`
	- utils.py
		- 当用户输入`CTRL+Z`导致异常时，打印的报错信息是空。去掉了`print`

- Optimization
	- 提高文件读取性能
		- 使用 json 格式保存数据文件
		- 使用 `open(path, 'rb')`获得二进制数据，`json.loads(data, encoding='utf-8')` 读取数据提高文件读取性能


### v170816.0120
- 基本版，实现所有功能需求


