"""
剑指Offer05.替换空格
https://gitee.com/programmercarl/leetcode-master/blob/master/problems/%E5%89%91%E6%8C%87Offer05.%E6%9B%BF%E6%8D%A2%E7%A9%BA%E6%A0%BC.md

替换数字
力扣已经将剑指offer题目下架，所以我在卡码网上给大家提供类似的题目来练习

卡码网题目链接

给定一个字符串 s，它包含小写字母和数字字符，请编写一个函数，将字符串中的字母字符保持不变，而将每个数字字符替换为number。

例如，对于输入字符串 "a1b2c3"，函数应该将其转换为 "anumberbnumbercnumber"。

对于输入字符串 "a5b"，函数应该将其转换为 "anumberb"

输入：一个字符串 s,s 仅包含小写字母和数字字符。

输出：打印一个新的字符串，其中每个数字字符都被替换为了number

样例输入：a1b2c3

样例输出：anumberbnumbercnumber

数据范围：1 <= s.length < 10000。

"""
import re


def rep0(s):
    return re.sub('\d','number',s)


def rep(s):
    new_str = ''
    for i in s:
        if '0' <= i <= '9':
            new_str += 'number'
        else:
            new_str += i
    return new_str


if __name__ == '__main__':
    print(rep('a1b2c3'))
