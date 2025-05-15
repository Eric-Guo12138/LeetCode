class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 第一个元素肯定要保留，所以从下标为1开始遍历nums
        # 如果nums[i]!=nums[i-1]，说明不是重复元素，要保留在nums[k]的位置，然后k+1
        # 遍历结束后，k就是去除重复项后的结果
        k = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k+=1
        return k 