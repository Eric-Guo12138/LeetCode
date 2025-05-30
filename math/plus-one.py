class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 先将digits中数字都转换成字符串，字符串转换成int再+1
        # 再转换成字符串，遍历添加到数组
        s = ''
        ans = []
        for i in digits:
            s = s + str(i)
        for j in str(int(s)+1):
            ans.append(int(j))
        return ans