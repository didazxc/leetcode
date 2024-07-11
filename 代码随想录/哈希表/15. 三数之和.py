"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意： 答案中不可以包含重复的三元组。

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为： [ [-1, 0, 1], [-1, -1, 2] ]
"""


def tri_sum0(nums):
    res = []
    nums.sort()
    for i in range(len(nums)):
        a = nums[i]
        if i > 0 and a == nums[i-1]:
            continue
        m = set()
        for j in range(i+1, len(nums)):
            c = nums[j]
            b = -a-c
            if b in m:
                res.append((a, b, c))
                m.remove(b)
            else:
                m.add(c)
    return res


def tri_sum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)-2):
        a = nums[i]
        if a > 0:
            break
        if i > 0 and a == nums[i-1]:
            continue
        left = i+1
        right = len(nums)-1
        while left < right:
            if nums[left] + nums[right] == -a:
                res.append((a, nums[left], nums[right]))
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] > -a:
                right -= 1
            else:
                left += 1
    return res


if __name__ == '__main__':
    print(tri_sum0([-1, 0, 1, 2, -1, -4, 0, 1, 0, 1, 0, 1]))
