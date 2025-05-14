class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 使用zip函数取出每个单词相同位置的字母
        # *用来解包strs使得zip函数可以将 strs 中每个字符串的对应位置的字符进行配对
        # 使用set转化成集合，集合会去除重复元素
        # 如果字母相同集合长度为1,将字母添加到ans
        # 如果不同就可以直接返回ans
        ans = ''
        for i in list(zip(*strs)):
            if len(set(i)) == 1:
                ans += i[0]
            else:
                break
        return ans