class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 从后往前遍历，i为最后一个单词的最后一个字母位置，j+1为最后一个单词的第一个字母位置
        # i-(j+1)+1=i-j就是其长度
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        j = i - 1
        while j >= 0 and s[j] != ' ':
            j -= 1
        return i - j