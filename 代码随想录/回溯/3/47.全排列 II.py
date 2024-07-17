"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：

输入：nums = [1,1,2]
输出： [[1,1,2], [1,2,1], [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
提示：

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""


def backtracking0(nums, used, path, res):
    if len(path) == len(nums):
        res.append(path[:])
        return
    seen = set()
    for i in range(len(nums)):
        if nums[i] in seen or used[i]:
            continue
        seen.add(nums[i])
        used[i] = True
        path.append(nums[i])
        backtracking(nums, used, path, res)
        path.pop()
        used[i] = False


def permute0(nums):
    res = []
    backtracking0(nums, [False]*len(nums), [], res)
    return res


def backtracking(nums, used, path, res):
    if len(path) == len(nums):
        res.append(path[:])
        return
    for i in range(len(nums)):
        if (i > 0 and nums[i] == nums[i-1] and not used[i-1]) or used[i]:
            continue
        used[i] = True
        path.append(nums[i])
        backtracking(nums, used, path, res)
        path.pop()
        used[i] = False


def permute(nums):
    res = []
    nums.sort()
    backtracking(nums, [False]*len(nums), [], res)
    return res


if __name__ == '__main__':
    print(permute([1,1,1,2]))
