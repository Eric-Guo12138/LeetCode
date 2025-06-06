# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # 二分查找，设置中间值mid，如果guess(mid)为0，说明mid就是答案
        # 如果guess(mid)为-1，说明mid比答案大，设置right=mid-1，继续二分查找
        # 如果guess(mid)为1，说明mid比答案小，设置left=mid+1，继续二分查找
        # 循环直到left>right
        left = 1
        right = n 
        while left <= right:
            mid = (left+right)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid - 1
            else:
                left = mid + 1