class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # 当两个序列长度不一样时，更长的序列肯定不是另一个序列的子序列，返回更长序列的长度
        # 当两个序列长度一样时，如果完全相同，返回-1
        # 否则其中一个字符串肯定不是另一个的子序列，返回任一长度
        if len(a) != len(b):
            return max(len(a),len(b))
        elif a == b:
            return -1
        else:
            return len(a)