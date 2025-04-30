class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 将数组排序，发现下标为len//2的元素就是多数
        # 原因：出现次数>=n/2，那么无论多数位置在数组左、中、右，肯定有一个多数会在中间
        nums.sort()
        return nums[len(nums)//2]