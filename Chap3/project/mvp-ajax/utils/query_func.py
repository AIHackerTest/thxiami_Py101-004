#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
存放查询天气时需要调用的函数
"""
import json
from string import ascii_letters

import requests
from model.user import User

from . import log

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
    else:
        return False


def fetch_weather(user, query_mode=None):
    """
    根据查询模式 query_mode 调用对应的 API 查询天气,返回数据
    :param user: user 实例,储存了本次调用所需的 api url 和 api params
    :param query_mode: now 或者 future
    :return: api 返回的 json 格式数据反序列化后的 dict
    """
    if query_mode == 'now':
        api_url = user.now_api_url
        api_params_dict = user.now_api_params_dict
    else:
        api_url = user.future_api_url
        api_params_dict = user.future_api_params_dict

    try:
        api_params_dict['location'] = user.input
        result = requests.get(api_url, params=api_params_dict, timeout=5)
    except requests.exceptions.ProxyError:
        log('fetch_weather 异常：requests.exceptions.ProxyError。可能是网络不通')
        return None
    except requests.exceptions.Timeout:
        log('fetch_weather 异常：requests.exceptions.Timeout。查询天气的请求超过了5s仍未得到响应')
        return None

    else:
        # 解析 json 数据，获得 dict 格式数据
        result_dict_from_api = result.json()
        return result_dict_from_api


def extract_weather_info(result_dict_from_api=None, query_mode=None):
    """
    当调用 API 获得了有效的天气信息后,提取需要的数据放入 dict 并返回
    :param result_dict_from_api: (dict), 天气 API 返回的 json 格式数据转换后的 dict
    :param query_mode: 天气查询模式, now 或者 future
    :return: dict, 包含几个需要的天气信息，供前端 jinja2 渲染页面时使用
    """
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
        now_weather_dict = dict(
            city=location_dict['name'],
            text=now_details_dict['text'],
            temperature=now_details_dict['temperature'],
            updated_time=updated_time_print,
        )

        return now_weather_dict

    else:  # 查询的是未来几日的天气预报
        days_details_list = result_dict_from_api['results'][0]['daily']

        future_weather_dict = dict(
            city=location_dict['name'],
            updated_time=updated_time_print,
            days_weather_details =[],
        )

        for day_detail_dict in days_details_list:
            day_weather_wanted = dict(
                date=day_detail_dict['date'],
                text_day=day_detail_dict['text_day'],
                text_night=day_detail_dict['text_night'],
                tep_low=day_detail_dict['low'],
                tep_high=day_detail_dict['high'],
            )
            future_weather_dict['days_weather_details'].append(day_weather_wanted)

        return future_weather_dict


def parse_weather_dict(result_dict_from_api=None, query_mode=None):
    """
    解析心知天气 API 返回的 json 格式数据，判断是否获得有效天气信息,若有效则提取所需天气信息并返回
    :param result_dict_from_api: (dict), 天气 API 返回的 json 格式数据转换后的 dict
    :param query_mode: 天气查询模式, now 或者 future
    :return: dict, 包含几个需要的天气信息，供前端 jinja2 渲染页面时使用
    """
    # 判断API 返回数据是否正常
    # 如果返回 json 数据内有 results，说明获得了有效数据
    if result_dict_from_api.get('results', None) is not None:
        weather_dict_for_render = extract_weather_info(result_dict_from_api=result_dict_from_api, query_mode=query_mode)
        return weather_dict_for_render

    # 如果返回 json 数据内有 status，则异常
    elif result_dict_from_api.get('status', None):
        log('API返回异常,异常信息:{}'.format(result_dict_from_api.get('status')))
        return None
    else:
        log('API返回异常，异常信息:{}'.format(result_dict_from_api))
        return None


def fetch_weather_of_visitor_city(location=None):
    """
    根据访客IP地址，获取其所在地当前天气信息
    :param location: 访客的 IP 地址
    :return: 天气信息
    """
    user = User()
    user.input = location
    result_dict_from_api = fetch_weather(user, query_mode='now')
    try:
        weather_dict_for_render = parse_weather_dict(
            result_dict_from_api=result_dict_from_api,
            query_mode='now'
        )
        return weather_dict_for_render
    except KeyError:
        return None





# 跟前端生成 Echarts 图表有关的函数
def generate_echarts_option(weather_dict=None):
    """
    从心知天气 API 返回的多日天气数据中取出每日天气信息和对应的日期
    组成前端 echart 生成时所需额外增加的参数字典(主要是数据)
    :param weather_dict: 从心知天气 API 返回的多日天气数据
    :return: 前端 echarts 生成时所需的参数字典
    """
    # echarts 生成时所需额外增加的参数字典中, 数据以数组形式保存
    # 故初始化下列数组
    dates = []
    low_teps = []
    high_teps = []
    low_tep_markPoint_datas = []
    high_tep_markPoint_datas = []
    days_weather_details = weather_dict['days_weather_details']

    for i, day_detail in enumerate(days_weather_details):
        date = day_detail['date']
        tep_low = day_detail['tep_low']
        tep_high = day_detail['tep_high']
        # text_day = day_detail['text_day']
        # text_night = day_detail['text_night']
        dates.append(date)
        low_teps.append(tep_low)
        high_teps.append(tep_high)
        high_tep_markPoint_dict = {
            "name": date,
            "value": tep_high,
            "xAxis": i,
            "yAxis": tep_high,
        }
        low_tep_markPoint_dict = {
            "name": date,
            "value": tep_low,
            "xAxis": i,
            "yAxis": tep_low,
        }
        high_tep_markPoint_datas.append(high_tep_markPoint_dict)
        low_tep_markPoint_datas.append(low_tep_markPoint_dict)

    option_dict = {
        "xAxis": [
            {
                "data": dates
            }
        ],
        "series": [
            {
                "name": "最高气温",
                "data": high_teps,
                "markPoint": {
                    "data": high_tep_markPoint_datas
                }
            },
            {
                "name": "最低气温",
                "data": low_teps,
                "markPoint": {
                    "data": low_tep_markPoint_datas
                }
            },
        ]
    }
    return option_dict


def data2json(type=None, value=None):
    """
    将天气查询错误时返回的提示语或正确时的 option 参数字典
    放入一个含有返回数据类型的字典中, 转为 json 格式饭给前端
    前端根据类型决定生成提示语还是生成图表
    """
    dt = dict(type=type, value=value)
    json_data = json.dumps(dt, ensure_ascii=False)
    return json_data