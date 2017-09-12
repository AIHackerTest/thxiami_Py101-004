#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Program name: 问天
Author: thxiami
Github: https://github.com/thxiami/
Edition：v1.0
Edit date: 2017.08.15
"""

__version__ = 170821.1150
__author__ = 'thxiami'

from command_function import command_function_dt
from user import User
from utils import (data_from_file,
                   get_user_input,
                   response_by_input
                   )


def run(data_path):
    """
    主函数，调用后运行天气查询程序
    :param data_path: (str) 存有天气数据文件的绝对或相对路径
    :return: None
    """

    # 读取天气数据
    weather_info_dt = data_from_file(data_path)

    # 初始化用户请求实例，需传入
    user = User()

    while True:
        # 获得用户输入的查询字符串
        prompt = '请输入城市名或指令,输入 help 获得帮助信息：  >'
        user_input = get_user_input(prompt)

        user.key = user_input[0]
        user.key_type = user_input[1]

        # 根据用户请求调用不同函数调用不同函数
        response_by_input(user, command_function_dt, weather_info_dt)


def main():
    data_path = 'weather_json.txt'
    run(data_path)


if __name__ == '__main__':
    main()
