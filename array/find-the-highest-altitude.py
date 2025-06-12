class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # 设置一个海拔列表，用来返回每个点的海拔，也就是上个点的海拔加上其高度差
        # 返回海拔中最大的值
        res = [0]
        for i in range(len(gain)):
            res.append(res[i] + gain[i])
        return max(res)