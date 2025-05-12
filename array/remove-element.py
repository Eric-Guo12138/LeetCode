class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 把nums看作栈，遍历nums,将不等于val的元素入栈
        s = 0
        for x in nums:
            if x != val:
                nums[s] = x
                s += 1
        return s