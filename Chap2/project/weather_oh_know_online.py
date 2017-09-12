#!usr/bin/env python3
# -*- coding: utf-8 -*-
"""
该项目提供了国内县级以上级别城市的天气查询功能，目前可查询指定城市：
- 实时天气
- 未来多日天气预报（15天内）
"""

__title__ = "问天online"
__version__ = "V17.08.29.2400"
__author__ = "thxiami<thxiami@gmail.com>"
__license__ = "MIT@2017-08"

from model.user import User
from utils.command_func import (
    # Functions
    command_response,
    # Constant value
    command_set
)
from utils.completer import prompt_input
from utils.config import (
    # Constant value
    program_help_doc,
)
from utils.query_func import (
    # Functions
    is_valid,
    fetch_weather,
    parse_weather_dict
)


# 程序主函数
def main():
    print(program_help_doc)
    user = User()

    while 1:
        try:
            user_input = prompt_input('>>请输入城市名称或指令，输入h/help获取帮助信息:')
            user.input = user_input
        except EOFError:
            print('您选择了退出交互。')
            break

        else:
            if user_input in command_set:
                command_response(user)

            elif is_valid(user):
                # 在判断用户输入的查询格式是否合法时
                # 已将查询模式，查询的城市和天数赋至 user 对应实例属性中，便于后续调用
                # print('user.query_mode:', user.query_mode)
                # print('user.api_url:', user.api_url)
                # print('user.api_params_dict:', user.api_params_dict)
                # 调用 API 查询天气，获取天气数据
                result_dict_from_api = fetch_weather(
                    api_url=user.api_url,
                    api_params_dict=user.api_params_dict)
                if result_dict_from_api is None:
                    continue
                else:
                    # 解析 dict 格式的天气数据，根据查询模式，输出对应格式的天气信息
                    weather_search_result = parse_weather_dict(
                        result_dict_from_api=result_dict_from_api,
                        temperature_unit=user.temperature_unit,
                        query_mode=user.query_mode)

                if weather_search_result is None:
                    continue
                else:
                    user.add_history(weather_search_result)
            else:
                print('   您输入的内容不符合要求，输入h/help查看帮助')


if __name__ == '__main__':
    main()
