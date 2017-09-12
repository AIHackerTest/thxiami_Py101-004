#!usr/bin/env python3
# -*- coding: utf-8 -*-
"""
定义 User 类
"""
from collections import deque

from utils.config import (
    # Variables
    now_api_url,
    future_api_url,
    api_key,
    default_unit,
    default_language,
    default_query_mode,
)


class User(object):
    """用于记录用户查询历史，输出历史"""

    def __init__(self):
        self.input = None
        self.history = deque()
        self.query_mode = default_query_mode  # 默认为查询实时天气模式
        self.temperature_unit = default_unit  # 用户选择的温度显示单位，'c' 是摄氏度，'f' 是 华氏度。 默认为摄氏度
        # 调用 API 时所需相关参数
        self.api_url = now_api_url  # API 请求地址
        self.api_params_dict = dict(
            key=api_key,  # API key
            unit=default_unit,  # 查询结果的温度显示单位
            language=default_language,  # 查询结果的语言
        )

    def add_history(self, search_result):
        """当用户使用城市名查询获得结果后，调用本方法添加至 log 属性中"""
        self.history.append(search_result)

    def print_history(self):
        """
        打印天气查询历史
        """
        if len(self.history) == 0:
            print('您还没有查询过天气')
        else:
            print('您的天气查询历史记录是：')
            for i in self.history:
                print('-' * 30)
                print(i)

    def temperature_unit_switch(self):
        """
        温度显示单位转换的函数
        """
        self.temperature_unit = self.input
        self.api_params_dict['unit'] = self.input
        if self.input == 'c':
            print('\n您已经选择温度显示单位为:摄氏度\n')
        else:
            print('\n您已经选择温度显示单位为:华氏度\n')
        pass

    def query_mode_switch(self, mode):
        """
        天气查询模式转换的函数
        根据当前环境初始化 API 参数字典
        根据用户选择的模式改变 API URL
        """
        self.query_mode = mode
        # 当模式转换时，API 参数字典也应该重新初始化
        # 防止 future -> now 模式转换后，api_params_dict 中 key start 和 days 未去掉
        self.api_params_dict = dict(
            key=api_key,
            unit=self.temperature_unit,
            language=default_language,
        )
        if self.query_mode == 'now':  # 切换查询模式为：实时天气
            self.api_url = now_api_url
        else:  # 切换查询模式为：未来多日天气概况预报
            self.api_url = future_api_url
            self.api_params_dict['start'] = 1  # 默认设置为查询从明日起的天气预报情况，比较人性化
