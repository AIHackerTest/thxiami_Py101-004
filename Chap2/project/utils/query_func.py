#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
存放查询天气时需要调用的函数
"""

from string import ascii_letters
from textwrap import dedent

import requests

__all__ = ['is_valid', 'fetch_weather', 'parse_weather_dict']


def is_pinyin(user_input):
    """
        检测字符是否只含有拼音

        :param user_input:(str), 需要判断的字符串
        :return: 字符串全部为拼音时返回 True；否认返回False
        """

    for i in user_input:
        # 使用中文十六进制的 Unicode 字符集范围判断
        if i not in ascii_letters:
            return False

    return True


def is_chinese(user_input):
    """
    检测字符是否只含有中文

    :param user_input:(str), 需要判断的字符串
    :return: 字符串全部为中文时返回 True；否认返回False
    """

    for i in user_input:
        # 使用中文十六进制的 Unicode 字符集范围判断
        if i < '\u4e00' or i > '\u9fa5':
            return False

    return True


def is_city(user_input):
    """
    通过检测字符是否只含有中文，或只含有拼音，粗略判断是否为城市名
    减少无效调用 API 的次数
    :param user_input:(str), 需要判断的字符串
    :return: 字符串全部为中文, 或者全部为拼音时返回 True；否认返回False
    """
    if len(user_input) > 0:
        return is_pinyin(user_input) or is_chinese(user_input)


def is_valid(user):
    """
    检测用户输入是否符合'城市' 或者 '城市 天数'这样的格式
    若符合要求将对应查询模式和调用 API 所用的参数赋给 user 实例对应属性
    :param user: 当前的 User 实例
    :return: 符合要求返回 True;反之返回 False
    """
    # 在判断用户输入的查询格式是否合法时
    # 当合法时就将查询模式，查询的城市和天数赋至 user 对应实例属性中
    # 其目的是不再后续的过程中对用户查询模式进行重新判断
    # 在调用 API 查询时不再单独根据查询模式去重新获得查询城市，天数

    if ' ' in user.input:  # 判断用户是否输入了 '城市 天数' 这样的格式
        city, days = user.input.split(' ', 1)
        print('is_valid()--> city:{} days:{}'.format(city, days))
        if is_city(city) and days.isdigit():
            user.query_mode_switch('future')
            user.api_params_dict['location'] = city
            user.api_params_dict['days'] = days
            return True

    elif is_city(user.input):  # 判断用户是否只输入了城市名
        user.query_mode_switch('now')
        user.api_params_dict['location'] = user.input
        return True

    else:
        return False


def fetch_weather(api_params_dict=None, api_url=None):
    """
    调用心知天气查询 API
    :param api_url: (str), 查询天气时使用的API URL
    :param api_params_dict: (dict), 查询天气时使用的API 参数字典
    :return: (dict), 从 API 获得的天气数据
    """
    try:
        result = requests.get(api_url, params=api_params_dict, timeout=5)
    except requests.exceptions.ProxyError:
        print('网络不通，是不是网络断了？')
        return None
    except requests.exceptions.Timeout:
        print('查询天气的请求超过了5s仍未得到响应，网络可能不太好，请稍后再试')
        return None

    else:
        # 解析 json 数据，获得 dict 格式数据
        result_dict_from_api = result.json()
        return result_dict_from_api


def generate_weather_info(result_dict_from_api=None, temperature_unit=None, query_mode=None):
    """
    从 API 返回的结果文件提取需要数据，根据查询模式返回对应格式的查询结果
    :param result_dict_from_api:
    :param temperature_unit:
    :param query_mode:
    :return:
    """
    # 根据用户设定的温度显示单位，选择输出时对应的文字
    unit_text_dict = {
        'c': '摄氏度',
        'f': '华氏度'
    }
    temperature_unit_text = unit_text_dict.get(temperature_unit, '温度单位异常')

    # 将数据拆分为 3 部分
    # location_dict: 存有天气对应地理位置的字典
    # updated_time_raw: 所获原始格式的天气信息最后更新时间
    # details_dict: 存有该地理位置的详细天气信息的字典，包括晴雨/温度等，需根据模式进行区分
    location_dict = result_dict_from_api['results'][0]['location']
    updated_time_raw = result_dict_from_api['results'][0]['last_update']
    updated_time_print = updated_time_raw.replace('T', ' ').replace('+08:00', '')

    # 定制输出需要的天气信息
    if query_mode == 'now':  # 查询实时天气
        now_details_dict = result_dict_from_api['results'][0]['now']
        result_for_user = dedent("""
                   {city}的实时天气为{text},气温：{tmp} {unit},风向：{wind}
                   更新时间:{time}\n
                   """.format(
            city=location_dict['name'],
            text=now_details_dict['text'],
            tmp=now_details_dict['temperature'],
            unit=temperature_unit_text,
            wind=now_details_dict['wind_direction'],
            time=updated_time_print))
        print(result_for_user)
        return result_for_user

    else:  # 查询的是多日天气
        days_details_dict = result_dict_from_api['results'][0]['daily']
        result_for_user = f"\n{location_dict['name']}未来的天气概况预报:\n"

        for day in days_details_dict:
            daily_result = dedent(
                f"{day['date']}:白天：{day['text_day']},夜间：{day['text_night']}," \
                f"气温: {day['low']}~{day['high']}{temperature_unit_text}," \
                f"风向：{day['wind_direction']}\n")
            result_for_user += daily_result
        result_for_user += f"以上天气信息最后更新时间:{updated_time_print}\n"

        print(result_for_user)
        return result_for_user


def parse_weather_dict(result_dict_from_api=None, temperature_unit=None, query_mode=None):
    """
    解析心知天气API返回的json格式数据，返回固定格式的天气信息
    :param result_dict_from_api: (dict), 天气 API 返回的 json 格式数据转换后的 dict
    :param temperature_unit: (str), 当前温度单位的辨识符.'c'/ 'C'代表摄氏度;'f'/ 'F'代表华氏度
    :param query_mode: (str), 当前天气查询模式的辨识符。 'now'代表实时模式; ''代表单日/多日模式
    :return:(str), 当 API 返回正常时，返回天气信息；
             (None), 当 API 返回错误时，返回 None
    """

    # 判断API 返回数据是否正常
    # 如果返回 json 数据内有 results，说明获得了有效数据
    if result_dict_from_api.get('results', None) is not None:
        result_for_user = generate_weather_info(
            result_dict_from_api=result_dict_from_api,
            temperature_unit=temperature_unit,
            query_mode=query_mode)
        return result_for_user

    # 如果返回 json 数据内有 status，则异常
    elif result_dict_from_api.get('status', None):
        print('\nAPI返回异常,异常信息:{}\n'.format(result_dict_from_api.get('status')))
        return None
    else:
        print('\nAPI返回异常，异常信息:{}\n'.format(result_dict_from_api))
        return None
