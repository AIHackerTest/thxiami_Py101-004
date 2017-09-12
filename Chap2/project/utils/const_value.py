# -*- coding: utf-8 -*-
"""
存放需要调用的变量
"""

from textwrap import dedent

now_api_url = 'https://api.seniverse.com/v3/weather/now.json'
future_api_url = 'https://api.seniverse.com/v3/weather/daily.json'
api_key = '4r9bergjetiv1tsd'
default_unit = 'c'
default_language = 'zh-Hans'
default_query_mode = 'now'

program_help_doc = dedent("""
    ------------天气资料由「心知天气」提供------------
    --------指令帮助--------
    - 输入指令 h 或 help，打印帮助文档；
    - 输入指令 q 或 quit，退出本程序；
    - 输入指令 c 或 C，将温度显示单位设定为摄氏度, 程序启动后默认单位为摄氏度；
    - 输入指令 f 或 F，将温度显示单位设定为华氏度；
    - 输入指令 history，打印查询过的所有城市天气。
    --------天气查询帮助--------
    1, 如想查询北京实时天气，可依据引号内格式输入:"北京"，同时也支持输入城市名的拼音:"beijing"
    2, 如想查询北京接下来3日内天气预报，可依据引号内格式输入:"北京 3",请注意"北京"与"3"之间以空格隔开；
       同理，也可输入"beijing 3"进行查询
    3, 在您输入过程中，程序会自动提供补全功能，也可以使用键盘的上下箭头按键方便调出历史指令，提高输入效率
    """)
