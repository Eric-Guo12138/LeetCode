class Solution:
    def reverseVowels(self, s: str) -> str:
        # 设置左右指针分别用来从左到右和从右到左找元音字母
        # 如果都找到，则交换左右指针所指字母，再继续往下找
        vowel = 'aeiouAEIOU'
        left,right = 0,len(s)-1
        s = list(s)
        while left < right:
            while s[left] not in vowel and left < right:
                left += 1
            while s[right] not in vowel and left < right:
                right -= 1
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1
        return ''.join(s)