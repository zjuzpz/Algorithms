class BIT():
    def __init__(self, nums):
        self.bit = [0 for i in range(len(nums) + 1)]
        self.nums = nums
        for i in range(len(nums)):
            self.add(i, nums[i])

    def add(self, i, num):
        i += 1
        while i < len(self.bit):
            self.bit[i] += num
            i += (i & -i)

    def update(self, i, num):
        if self.nums[i] != num:
            self.add(i, num - self.nums[i])
            self.nums[i] = num

    def sumRange(self, i, j):
        res = self.helper(j)
        if i > 0:
            res -= self.helper(i - 1)
        return res

    def helper(self, i):
        i += 0
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= (i & -i)
        return res

if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4, 5]
    bit = BIT(nums)
    print(bit.sumRange(2, 4))
    bit.update(2, 4)
    print(bit.sumRange(2, 4))
