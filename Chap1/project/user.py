#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class User(object):
    """用于记录用户查询历史，输出历史"""

    def __init__(self):
        self.key = None
        self.key_type = None
        self.logs = []

    """
    def iscommand(self):
        ""
        判断获得的合法的用户输入是否是指令
        ""
        print('debug Request: request.key=', self.key)
        print('debug Request: request.command_set={},iscommand:{}'.format(self.command_set, self.key in self.command_set))

        if self.key in self.command_set:
            return True
        else:
            return False

    def is_chinese(self):

        判断获得的合法的用户输入是否是中文

        return not self.iscommand()
    """
    def add_log(self, search_result):
        """当用户使用城市名查询获得结果后，调用本方法添加至 log 属性中"""
        self.logs.append(search_result)

    def print_log(self):
        """打印logs内所有历史记录"""
        if len(self.logs) == 0:
            print('抱歉，今天您还没查过天气呢')
        else:
            for log in self.logs:
                print(log)
