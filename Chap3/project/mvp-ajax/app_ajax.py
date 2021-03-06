#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
该项目提供了国内县级以上级别城市的天气查询功能，目前可查询指定城市：
- 实时天气
- 未来多日天气预报（15天内）
"""

__title__ = "问天online"
__version__ = "V17.09.07.2250"
__author__ = "thxiami<thxiami@gmail.com>"
__license__ = "MIT@2017-08"

from collections import deque

from flask import (
    Flask,
    render_template,
    request,
)
from model.user import User
from utils import log
from utils.config import (
    program_help_doc,
)
from utils.query_func import (
    # Functions
    is_city,
    fetch_weather,
    fetch_weather_of_visitor_city,
    parse_weather_dict,
    generate_echarts_option,
    data2json,
)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """
    主页的路由函数
    """
    visitor_ip = request.remote_addr
    log('访客IP:', visitor_ip)
    log('-------------用户访问了主页-------------')
    log('index request 的 method:', request.method)
    log('index request 的 query 参数:', request.args)
    weather_result = fetch_weather_of_visitor_city(location=visitor_ip)
    if weather_result is not None:
        response = render_template('index.html', weather_result=weather_result)

    else:
        response = render_template('index.html')

    return response


@app.route('/command', methods=['GET'])
def command_response():
    """
    处理用户点击 帮助/历史记录 button 的路由函数
    """
    command = request.args.get('button', None)
    log('-------------用户点击了指令相关的button-------------')
    log('command_response request.args:', request.args)
    log('command_response 用户点击的button的value:', command)

    if command == "history":
        if len(history_deque) == 0:
            prompt = '您还没有查询过天气'
            return render_template('history.html', prompt=prompt, history=history_deque)
        else:
            return render_template('history.html', history=history_deque)

    elif command == 'help':
        return render_template('help.html', results=program_help_doc)

    else:
        return render_template('help.html', prompt="请求的URL非法")


@app.route('/search_ajax', methods=['POST'])
def search_ajax():
    """
        天气查询的路由函数
    """
    log('前端发来的数据:', request.form)
    form = request.form
    user.input = form.get('user_input', '')
    log('-------------用户发起了一次天气查询请求-------------')
    log('search request.args:', request.args, type(request.args))
    log('search user.input:', user.input)

    if is_city(user.input):
        # 调用 API 查询天气，获取天气数据
        now_weather_dict_from_api = fetch_weather(user, query_mode='now')
        future_weather_dict_from_api = fetch_weather(user, query_mode='future')
        if now_weather_dict_from_api is None:
            prompt = '调取API查询天气时, 出现异常'
            return data2json(type='prompt', value=prompt)
        else:
            # 解析 dict 格式的天气数据，根据查询模式，输出对应格式的天气信息
            now_weather_dict_for_render = parse_weather_dict(
                result_dict_from_api=now_weather_dict_from_api,
                query_mode='now')
            future_weather_dict_for_render = parse_weather_dict(
                result_dict_from_api=future_weather_dict_from_api,
                query_mode='future')

        if now_weather_dict_for_render is None:
            prompt = '无该城市天气信息，请确认城市名称是否正确'
            return data2json(type='prompt', value=prompt)

        else:
            history_deque.append(now_weather_dict_for_render)
            # 解析未来几日天气数据
            # 组成前端 echarts 生成时所需的参数字典，序列化为 json 格式后返回
            add_option_dict = generate_echarts_option(weather_dict=future_weather_dict_for_render)
            return data2json(type='option', value=add_option_dict)
    else:
        prompt = '您输入的城市名不符合要求，请重新输入'
        return data2json(type='prompt', value=prompt)


if __name__ == '__main__':
    # 初始化 User 实例，用于保存用户输入，api参数等变量
    user = User()
    history_deque = deque()

    # 配置服务端参数,上线时 debug 模式为 False
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=3000,
    )

    # 开始记录日志
    log('---------服务端开始启动---------')
    log('启动参数：', config)
    log('app.config', app.config)
    # 启动服务端
    app.run(**config)
