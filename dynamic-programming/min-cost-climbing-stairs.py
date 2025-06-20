class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # f[i]为爬到下标i的台阶的最小花费，初始全设为0
        # 台阶0和1最小花费就是0，所以从台阶2开始遍历
        # 由于每次只能爬1或2个台阶，f[i]也就是f[i-1]+cost[i-1]和f[i-2]+cost[i-2]中更小的那个
        # 直到递归结束，返回f[n]
        n = len(cost)
        f = [0] * (n+1)
        for i in range(2,n+1):
            f[i] = min(f[i-1]+cost[i-1],f[i-2]+cost[i-2])
        return f[n]