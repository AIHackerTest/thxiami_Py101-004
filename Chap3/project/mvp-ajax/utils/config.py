# -*- coding: utf-8 -*-
"""
存放需要调用的变量
"""
from os.path import dirname
from textwrap import dedent

now_api_url = 'https://api.seniverse.com/v3/weather/now.json'
future_api_url = 'https://api.seniverse.com/v3/weather/daily.json'
api_key = '4r9bergjetiv1tsd'
default_unit = 'c'
default_language = 'zh-Hans'
default_query_mode = 'now'

# 以下 default_now_api_params, default_future_api_params 为调用API时所用的 query 参数,仅缺少1个参数 location
# 使用时只需根据用户在前端输入的城市,将其添加为 dict 中 location 的 value
# 调用 API 所需的参数就够了
default_now_api_params = dict(
    key=api_key,  # API key
    unit=default_unit,  # 查询结果的温度显示单位
    language=default_language,  # 查询结果的语言
)

default_future_api_params = dict(
    key=api_key,  # API key
    unit=default_unit,  # 查询结果的温度显示单位
    language=default_language,  # 查询结果的语言
    start=1,  # 表示从未来哪天开始查询天气预报概况, 1 代表明天,0 代表今天
    days=5,  # 表示查询未来几天的天气预报概况, 默认为5天
)

program_help_doc = dedent("""\
    1, 如想查询北京市天气，在输入框内输入: "beijing"或者"北京",点击〖查询天气〗按钮，\
    将会显示北京市实时天气和未来5日天气预报
    2, 点击〖历史记录〗按钮，获得查询历史
    3, 点击〖帮助〗按钮，将显示程序使用帮助
    注意：输入引号内文字，不含引号。\
    """).split('\n')

log_path = dirname(dirname(__file__)) + "/log.txt"

