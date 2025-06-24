class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # 遍历字符串t，如果某个元素出现次数比s中的多1，结果就是该元素
        for i in t:
            if t.count(i) - s.count(i) == 1:
                return i