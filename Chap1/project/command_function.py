#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_help(user):
    """打印帮助信息"""

    help_doc = """
    - 输入城市名，返回该城市的天气数据；
    - 输入指令 h 或 help，打印帮助文档；
    - 输入指令 quit 或 exit，退出本程序；
    - 输入指令 history，打印查询过的所有城市。
    """
    print(help_doc)


def print_history(user):
    """
    将存在于 log 中的历史查询记录打印出来
    """
    user.print_log()


def quit_(user):
    """输出历史记录，然后退出程序"""
    from sys import exit

    user.print_log()
    exit(0)


command_function_dt = {
        'help': print_help,
        'history': print_history,
        'quit': quit_,
    }