#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
存放需要调用的函数
- 从天气信息文件获得数据的函数
- 天气查询函数
- 指令确认函数
- 中文检查函数
- 获得用户合法输入的函数
- 对用户输入作出响应的函数
"""

import json


def data_from_file(path):
    """
    从本地 json 格式的文件中读取格式为"city, weather"的数据
    返回以 {city:weather} 格式的 dict
    :param path: (str), 含有天气数据的 txt 文件绝对/相对路径
    :return: (dict), key:value = city:weather 的 dict

    """
    with open(path, 'rb') as f:
        s = f.read()
        return json.loads(s, encoding='utf-8')


def weather_search(city, data_dt):
    """
    根据城市名查询对应的天气

    :param city: (str), 中文城市名
    :param data_dt: (dict), 以{city:weather} 格式存储城市天气信息的字典
    :return: 如果查到，返回 "city:weather" 格式的字符串;
              如果没查到，返回 None
    """
    weather = data_dt.get(city, None)

    if weather is None:
        print('抱歉，没有找到该城市，请确认城市名称输入正确')
        return None

    else:
        search_result = '{} :{}'.format(city, weather)
        return search_result


def iscommand(user_input):
    """
    判断输入是否在已存指令中
    :param user_input (str): 用户输入
    :return: 如果输入在指令集中，True；反之，False
    """
    from command_function import command_function_dt

    # command_set = set(command_function_dt.keys())
    if user_input in command_function_dt:
        return True
    else:
        return False


def ischinese(user_input):
    """
    检测字符是否只含有中文

    :param user_input:(str), 需要判断的字符串
    :return: 字符串全部为中文返回 True；否认返回False
    """

    for i in user_input:
        # 使用中文十六进制的 Unicode 字符集范围判断
        if i < '\u4e00' or i > '\u9fa5':
            return False

    return True


def get_user_input(prompt):
    """
    用于获得用户输入的合法命令或中文
    :param prompt (str): 提示语句
    :return: (user_input, 'command') 当user_input在是命令时；
              (user_input, 'chinese') 当user_input在是中文时；
    """

    while True:
        try:
            # 获得用户输入
            user_input = input(prompt)
        except:
            from sys import exit
            print('你输入了什么？！..！@#￥%……&')
            print('程序崩溃了，退出ing...')
            exit(0)

        else:
            # 用户输入了命令
            if iscommand(user_input):
                return user_input, 'command'
            # 用户输入了中文
            elif ischinese(user_input):
                return user_input, 'chinese'
            # 非命令非中文
            else:
                print('输入非法')
                continue


def response_by_input(user, command_response_dt, weather_info_dt):
    """
    根据用户请求的关键词，调用对应函数
    :param user (instance): 用户实例
    :param command_response_dt (dict): 存放指令名称及对应功能函数变量的字典
    :param weather_info_dt (dict): 存放城市天气信息的字典
    :return: None
    """

    # 如果用户输入的请求是指令
    if user.key_type == 'command':
        response_func = command_response_dt[user.key]
        response_func(user)

    # 不是指令，那用户输入的请求就是中文
    else:
        weather_result = weather_search(user.key, weather_info_dt)
        # 如果查到了结果
        if weather_result is not None:
            print(weather_result)
            user.add_log(weather_result)
