# -*- coding: utf-8 -*-
"""
存放代码自动补全所需的函数
"""

import os
import csv
from collections import deque

from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import WordCompleter

from .command_func import command_set

__all__ = ['prompt_input']


# 以下是代码补全所用的函数和变量
def get_city_names(path):
    """从存有城市名称中文和拼音版本的 csv 文件中读取数据，放入 collections.deque 中并返回"""
    city_names_deque = deque()

    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for chi, pinyin in reader:
            city_names_deque.append(chi)
            city_names_deque.append(pinyin)
    return city_names_deque


def get_command_completer(list1, list2):
    words_list = list1 + list2
    completer = WordCompleter(words_list, ignore_case=False)
    return completer


# 获取 project 和 resources 的父目录，或者说是代码的根目录
root_dir = os.path.dirname(os.path.dirname(__file__))

# 组成路径, 便于项目迁移不同位置
city_names_file_path = os.path.join(root_dir, 'data/citynames.csv')
inp_history_file_path = os.path.join(root_dir, 'data/inp_history.txt')

# 获取自动补全需要的 word list
commands = deque(list(command_set))
city_names = get_city_names(city_names_file_path)

# 输入函数自动补全时需要的一个参数
weather_completer = get_command_completer(city_names, commands)


# 有自动补全功能的获取用户输入的函数
def prompt_input(prt):
    """
    调用有自动补全功能的 input 函数获取用户输入并返回
    :param prt: 提示语
    :return: 用户输入
    """

    inp = prompt(prt,
                 history=FileHistory(inp_history_file_path),
                 auto_suggest=AutoSuggestFromHistory(),
                 completer=weather_completer)
    return inp
