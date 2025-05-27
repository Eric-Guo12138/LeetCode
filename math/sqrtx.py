class Solution:
    def mySqrt(self, x: int) -> int:
        # 从1开始判断平方是否<=x
        sqrt = 1
        while sqrt * sqrt <= x:
            sqrt += 1
        return sqrt - 1