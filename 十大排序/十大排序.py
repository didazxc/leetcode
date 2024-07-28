

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


if __name__ == '__main__':
    nums = [26, 77, 28, 43, 95, 91, 59, 85, 82, 69, 4, 1, 11, 57, 80, 54, 25, 63, 79, 61]
    bubble(nums)
    print(nums)
