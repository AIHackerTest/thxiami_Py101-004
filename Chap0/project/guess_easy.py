#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Program name: Bulls And Cows Advanced Edition
Author: thxiami
Github: https://github.com/thxiami/
Edition：v1.0
Edit date: 2017.08.14
"""

from random import randint


def get_num():
    """
    用于获得用户输入的合法数字，并返回
    
    Args:
    
    Return:
        integer : 用户输入的数字
    """
    # 获得用户输入
    input_num = input('Please type in a number.\n >')

    # 判断用户输入的合法性，当输入仅包含数字时返回该数字；其他情况要求用户重新输入
    if input_num.isdigit():
        return int(input_num)
    else:
        print('Only a number is wanted! e.g. 5')
        return get_num()


def guess(wanted_num, input_num):
    """
    判断给定的两个数字关系，根据判断结果打印必要信息并返回布尔值。
    
    Args：
        wanted_num (int): 程序给定的需要用户去猜测的数字，2位数
        input_num (int)：用户输入的数字,2位数
        
    Return:
        bool : True代表两个数字相等；False代表不相等
        
    Demo：
        result_bool = guess(10, 15), 程序会打印"大了"，并返回 False;
    """
    if input_num > wanted_num:
        print("大了")
        return False

    elif input_num < wanted_num:
        print("小了")
        return False

    elif input_num == wanted_num:
        print("正确，游戏结束")
        return True


def play(allowable_count):
    """
    游戏运行逻辑的函数，调用函数则游戏开始，无返回
    
    Args:
        allowable_count (int): 表示允许玩家猜测的次数
    """
    # 生成随机数，让玩家猜测
    wanted_number = randint(0, 21)

    # 玩家猜测的次数，初始为 1
    count = 1
    
    # 使用 while True 开始循环获得玩家输入并判定猜测结果
    # 循环结束条件为：猜测次数大于 10，或者玩家猜测正确
    while True:
    
        # 对玩家猜测次数进行判断
        if count > 10:
            print('您没有机会猜测，游戏结束')
            break
        
        # 获得玩家输入
        print(f'第{count}次猜测，还有{10 - count}次机会')
        input_number = get_num()
        
        # 对玩家猜测结果进行判断
        if guess(wanted_number, input_number) is True:
            break

        count += 1


def main():
    rules = """
        - 程序随机生成一个 20 以内的数字，用户有 10 次机会猜测
        - 程序根据用户输入， 给予一定提示 （大了、小了、正确）
        - 猜对或用完 10 次机会，游戏结束
        """
    print('游戏规则：\n', rules)
    play(10)


if __name__ == '__main__':
    main()
