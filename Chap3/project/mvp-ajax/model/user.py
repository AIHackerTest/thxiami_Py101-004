#!usr/bin/env python3
# -*- coding: utf-8 -*-
"""
定义 User 类
"""

from utils.config import (
    # Variables
    now_api_url,
    future_api_url,
    default_now_api_params,
    default_future_api_params,
)

class User(object):
    """用于记录用户查询历史，输出历史"""

    def __init__(self):
        self.input = None
        # 调用 API 时所需相关参数
        self.now_api_url = now_api_url  # 调用实时天气 API 对应URL
        self.now_api_params_dict = default_now_api_params  # 调用实时天气 API 所需 query 参数
        self.future_api_url = future_api_url  # 调用天气预报 API 对应URL
        self.future_api_params_dict = default_future_api_params  # 调用天气预报 API 所需 query 参数
