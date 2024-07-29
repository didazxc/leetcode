

def insert(nums):
    for cur in range(len(nums)):
        num = nums[cur]
        i = cur - 1
        while i >= 0 and nums[i] > num:
            nums[i + 1] = nums[i]
            i -= 1
        nums[i+1] = num


def shell(nums):
    length = len(nums)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            cur = nums[i]
            while nums[i] < nums[i-gap]:
                nums[i] = nums[i-gap]
                i -= gap
            nums[i] = cur
        gap //= 2


def select(nums):
    for cur_index in range(len(nums)-1):
        min_index = cur_index
        for i in range(cur_index+1, len(nums)):
            if nums[i] < nums[min_index]:
                min_index = i
        nums[cur_index], nums[min_index] = nums[min_index], nums[cur_index]


class HeapSort:

    def __init__(self, nums):
        self.length = len(nums)
        self.arr = nums
        for i in range(self.length // 2, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        largest = i
        left = 2*i+1
        right = 2*i+2
        if left < self.length and self.arr[left] > self.arr[largest]:
            largest = left
        if right < self.length and self.arr[right] > self.arr[largest]:
            largest = right
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(largest)

    def sort(self):
        for i in range(self.length-1, -1, -1):
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            self.length -= 1
            self.heapify(0)


def heap(nums):
    HeapSort(nums).sort()


def bubble(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


def quick(nums, left=0, right=None):
    """
    先排中间节点，然后分两部分分别排
    """
    def part(nums, left, right):
        pivot = left
        index = pivot + 1
        for i in range(pivot + 1, right):
            if nums[i] < nums[pivot]:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1
        nums[pivot], nums[index-1] = nums[index-1], nums[pivot]
        return index - 1
    right = len(nums) if right is None else right
    middle = part(nums, left, right)
    if middle > left:
        quick(nums, left, middle)
    if middle < right - 1:
        quick(nums, middle+1, right)


def merge(nums):
    """
    合并两个有序数组时，排序
    """

    def combine(arr1, arr2):
        arr = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                arr.append(arr1[i])
                i += 1
            else:
                arr.append(arr2[j])
                j += 1
        while i < len(arr1):
            arr.append(arr1[i])
            i += 1
        while j < len(arr2):
            arr.append(arr2[j])
            j += 1
        return arr

    if len(nums) < 2:
        return nums
    middle = len(nums)//2
    left = merge(nums[:middle])
    right = merge(nums[middle:])
    return combine(left, right)


def count(nums):
    max_value = max(nums)
    cnt = [0] * (max_value+1)
    for num in nums:
        cnt[num] += 1
    arr = []
    for i in range(max_value+1):
        for _ in range(cnt[i]):
            arr.append(i)
    return arr


def radix(nums):
    max_digit = len(str(max(nums)))
    mod = 10
    dev = 1
    for _ in range(max_digit):
        buckets = [[] for _ in range(10)]
        for num in nums:
            b_index = (num % mod) // dev
            buckets[b_index].append(num)
        i = 0
        for bucket in buckets:
            for num in bucket:
                nums[i] = num
                i += 1
        mod *= 10
        dev *= 10


def bucket(nums, bucket_size=5):
    min_value = min(nums)
    # 比实际个数少1，意味着行为左移，即令能被整除的数据和前面不能被整除的数据所得商一致
    # 可以从序号角度考虑，min_value的序号为0，(max(nums) - min_value)//bucket_size为最后一个桶的序号
    bucket_count = (max(nums) - min_value) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]
    for num in nums:
        buckets[(num - min_value) // bucket_size].append(num)
    arr = []
    for b in buckets:
        insert(b)
        for num in b:
            arr.append(num)
    return arr


if __name__ == '__main__':
    nums = [26, 77, 28, 43, 95, 91, 59, 85, 82, 69, 4, 1, 11, 57, 80, 54, 25, 63, 79, 61]
    arr = bucket(nums)
    print(arr)
    print(nums)
