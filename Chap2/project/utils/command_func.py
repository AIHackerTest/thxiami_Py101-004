# -*- coding: utf-8 -*-
"""
存放 指令对应的功能函数
"""
from utils.config import program_help_doc

__all__ = ["command_set", "command_response"]


def print_help():
    print(program_help_doc)


def quit_():
    """退出程序"""
    # print_history(his_deque)
    print("正在退出程序...")
    exit(0)


def command_response(user):
    """
    根据用户输入的指令调用对应函数或实例方法
    :param user: User 实例
    :return:
    """

    command_func_dt = {
        'h': print_help,
        'help': print_help,
        'q': quit_,
        'quit': quit_,
        'history': user.print_history,
        'c': user.temperature_unit_switch,
        'f': user.temperature_unit_switch,
    }
    command_not_found_msg = "抱歉，您输入的指令未能识别"
    func = command_func_dt.get(user.input, lambda: print(command_not_found_msg))
    func()


command_set = ([
    'h', 'help',
    'q', 'quit',
    'history',
    'c', 'f',
])
