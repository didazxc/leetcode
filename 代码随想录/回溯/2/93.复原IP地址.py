"""
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。

示例 1：

输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
示例 2：

输入：s = "0000"
输出：["0.0.0.0"]
示例 3：

输入：s = "1111"
输出：["1.1.1.1"]
示例 4：

输入：s = "010010"
输出：["0.10.0.10","0.100.1.0"]
示例 5：

输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
提示：

0 <= s.length <= 3000
s 仅由数字组成
"""


def valid_id_track(raw_str, start_index, path, res):
    if len(path) == 4:
        if start_index >= len(raw_str):
            res.append('.'.join(path))
        return
    for i in range(start_index, min(start_index+3, len(raw_str))):
        ip = raw_str[start_index:i+1]
        if 0 <= int(ip) <= 255 and (i == start_index or ip[0] != '0'):
            path.append(ip)
            valid_id_track(raw_str, i+1, path, res)
            path.pop()


def valid(raw_str):
    res = []
    valid_id_track(raw_str, 0, [], res)
    return res


if __name__ == '__main__':
    print(valid('101023'))
