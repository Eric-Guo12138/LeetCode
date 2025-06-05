class Solution:
    def tribonacci(self, n: int) -> int:
        # 尝试了递归方法，超时。
        # 设置了一个数组用来存放每个泰波那契数的值，n>=3时，计算出该值加到数组中
        # 返回最后一个元素的值即可
        ans = [0,1,1]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            for i in range(3,n+1):
                ans.append(ans[i-1] + ans[i-2] + ans[i-3])
            return ans[n]