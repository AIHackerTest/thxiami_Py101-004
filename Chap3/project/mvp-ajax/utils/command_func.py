# -*- coding: utf-8 -*-
"""
存放 指令对应的功能函数
"""

# __all__ = ["print_history"]


def print_history(history):
    """
    返回 jinja2 渲染页面时所需的提示语和查询记录
    """
    if len(history) == 0:
        render_params_dict = dict(prompt='您还没有查询过天气', history=history)
        prompt='您还没有查询过天气'
    else:
        render_params_dict = dict(prompt='您的查询记录为:', history=history)
    return render_params_dict
