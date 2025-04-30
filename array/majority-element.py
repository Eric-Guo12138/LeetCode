class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 将数组排序，发现下标为len//2的元素就是众数
        nums.sort()
        return nums[len(nums)//2]