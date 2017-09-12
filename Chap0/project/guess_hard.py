#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Program name: Bulls And Cows
Author: thxiami
Github: https://github.com/thxiami/
Edition：v1.0
Edit date: 2017.08.14
"""

from random import (randint,
                    sample
                    )


def generate_randnum():
    """
    函数用于生成符合游戏规则的随机数，并返回该数字的字符串
    游戏规则：随机数为 4 位，首位不为 0 且各数位不重复
    
    Args:
    
    Return：
        string : 符合游戏规则的随机数

    """
    # 生成一个含有 str 类型数字 0~9 的list,用于从中依次取数拼接随机数
    optional_numbers = [str(i) for i in range(10)]

    # 分两次生成随机数，第 1 次生成首位
    # 首位不为 0，故从 optional_numbers 中后 9 个数字随机选择 1 个数返回
    # 并从列表 optional_numbers 中删掉这个数字，防止后续取到重复数字
    first_num = optional_numbers.pop(randint(1, 9))
    
    # 第 2 次生成后3位
    three_num_ls = sample(optional_numbers, 3)
    three_num = ''.join(three_num_ls)
    
    # 返回最终的 4 位随机数
    random_num = first_num + three_num
    return random_num

    """
    # 后三位数字的生成还有下面这种方案
    # 仿照生成首位数字的流程循环 3 次
    # 从 optional_numbers 这个 只有 9 个数的 list 中取数拼接随机数字符串
    for i in range(3):
        num = optional_numbers.pop(randint(0, len(optional_numbers) - 1))
        random_num += num

    return random_num
     """



def get_num():
    """
    用于获得玩家输入的合法数字，并返回。

    Args:
    
    Return:
        string : 玩家输入的 4 位数字

    """
    # 玩家输入数字
    input_num = input('Please type in a 4 digit number.\n >')

    # 判断玩家输入的合法性
    # 若仅含数字且长度为 4 ，返回该字符串;其他情况则使用递归要求用户重新输入
    if input_num.isdigit() and len(input_num) == 4:
        return input_num
    else:
        print('Only a 4 digit number is wanted! e.g. 5')
        return get_num()


def guess(wanted_num, input_num):
    """

    判断给定的两个数字型字符串的匹配程度，根据判断结果打印匹配程度的相关信息。
    匹配程度用 A 和 B 的个数表示，A 表示数字和位置都正确，B 表示数字正确但位置错误。

    Args:
        wanted_num (str): 程序随机生成的 4 位数，需要用户来猜测
        input_num (str)：用户输入的 4 位数

    Return:
        tuple : (bool, string)
                True 代表二者完全匹配，即相等; False 代表二者部分匹配或完全不匹配
                string 表示两个字符串匹配程度，如 "2A1B"，返回这个为了让单元测试更准确
    Demo:
        result_bool = guess('1234', '1245')
        程序打印出 "2A1B",并返回 (False, "2A1B")
        
        result_bool = guess('1234', '1234')
        程序打印出 "恭喜猜对，游戏结束",并返回 (True,"4A0B")

    """
    
    # 初始化变量，分别用于存储 A 和 B的个数
    count_of_a = 0
    count_of_b = 0
    
    # 遍历程序生成的随机数 wanted_num 
    # 记录它与玩家输入的数字的匹配程度
    for i, num in enumerate(wanted_num):

        if num == input_num[i]:
            count_of_a += 1
        elif num in input_num:
            count_of_b += 1
        else:
            continue
    
    # 初始化变量，分别存储判断结果的布尔值和匹配程度
    result_bool = False
    result_str = '{}A{}B'.format(count_of_a, count_of_b)
    
    # 判断是否完全匹配
    if count_of_a == 4:
        print('猜对，游戏结束')
        result_bool = True

    else:
        print(result_str)
        
    # 返回判断结果的布尔值和匹配程度
    return (result_bool, result_str)


def play(allowable_count):
    """
    游戏运行逻辑的函数，获得玩家输入并判断是否
    allowable_count: int 型，为允许玩家猜测的次数
    """
    # 生成随机数
    wanted_number = generate_randnum()

    # 玩家开始猜测，计数开始
    count = 1

    while True:
    
        if count > allowable_count:
            print(f'您没有机会猜测，游戏结束!正确答案：{wanted_number}\n要不充点钱再来？')
            break
            
        print(f'第{count}次猜测，还有{10 - count}次机会')
        input_number = get_num()

        if guess(wanted_number, input_number)[0] is True:
            break
        
        count += 1

    


# 单元测试

def test_generate_randnum():
    """
    generate_randnum() 的测试函数，测试通过规则:
    generate_randnum()返回的值中，第1位不为0且每一位各不相同
    """
    print('--------随机数生成函数测试开始--------')
    for i in range(100 * 100):
        random_num = str(generate_randnum())

        assert len(random_num) == 4, '首位为0，random_num:{}'.format(random_num)
        for i in range(10):
            assert random_num.count(str(i)) <= 1, '有相同的值出现，random_num:{}'.format(random_num)
    print('--------随机数生成函数测试通过--------')

def test_of_guess():
    """
    guess() 函数的测试函数，测试通过规则:
    返回的A,B值与预期相符
    """
    wanted_num = '1234'
    test_input_num = [
        # 无重复
        ('5678', '0A0B'),
        ('5671', '0A1B'),
        ('5617', '0A1B'),
        ('5167', '0A1B'),
        ('5612', '0A2B'),
        ('5312', '0A3B'),
        ('4312', '0A4B'),
        ('1567', '1A0B'),
        ('4256', '1A1B'),
        ('4531', '1A2B'),
        ('3124', '1A3B'),
        ('5634', '2A0B'),
        ('1253', '2A1B'),
        ('1243', '2A2B'),
        ('1235', '3A0B'),
        ('1234', '4A0B'),
        # 有重复
        ('4444', '1A0B'),
        ('2244', '2A0B'),
        # 首位有0
        ('0000', '0A0B'),
    ]
    print('--------guess 函数测试开始--------')
    for i in test_input_num:
        result_str = guess(wanted_num, i[0])[1]
        assert result_str == i[1], 'guess 函数出错，wanted_num:{}, test_num:{}, \n' \
                               'result_getted:{}, result_wanted:{}'.format(wanted_num, i[0], result_str, i[1])
    print('--------guess 函数测试通过--------')

def test():
    test_generate_randnum()
    test_of_guess()


def main():
    rules = """
        - 程序随机生成一个 4 位数，每个数位上的数字不重复，且首位数字不为0，如1942
        - 玩家输入 4 位数进行猜测，有 10 次机会猜测
        - 程序会根据玩家输入， 给予相应提示
            - 用 A 表示数字和位置都正确，用 B 表示数字正确但位置错误
            - 玩家猜测后，程序返回 A 和 B 的数量
            - 比如： 2A1B 表示玩家所猜数字，有 2 个数字，数字和位置都正确，有 1 个数字，数字正确但位置错误 
        - 猜对或用完 10 次机会，游戏结束
        """
    print('游戏规则：\n', rules)
    print('-----------游戏开始咯------------')
    # 运行游戏主函数
    play(10)


if __name__ == '__main__':
    #test()
    main()
