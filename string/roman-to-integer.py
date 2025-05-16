class Solution:
    def romanToInt(self, s: str) -> int:
        ''' 先把特殊情况都列出来，遍历特殊情况，看s中有没有对应的,有的话添加到结果，并把s中的特殊情况去除,然后再在s中遍历，把常规的都加到结果中'''
        ans = 0
        dic1 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        dic2 = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        for i in dic2:
            if i in s:
                ans += dic2[i]
                s = s.replace(i,'')
        for j in s:
            ans += dic1[j]
        return ans