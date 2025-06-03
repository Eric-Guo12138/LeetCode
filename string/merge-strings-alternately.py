class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # 取word1和word2中长度较小的值为长度进行遍历，将遍历到的元素添加到空字符串中
        # 如果word1长度更小，则把word2剩余元素添加至末尾
        # 否则把word1剩余元素添加至末尾
        ans = ""
        i,j = len(word1),len(word2)
        for k in range(min(i,j)):
            ans += word1[k]
            ans += word2[k]
        if i < j:
            ans += word2[k+1:]
        else:
            ans += word1[k+1:]
        return ans