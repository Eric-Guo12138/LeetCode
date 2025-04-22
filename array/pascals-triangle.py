class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 初始化一个二维数组，所有元素设为1，其中每个数组的首元素和尾元素都 符合要求，其余元素a[i][j]=a[i-1][j-1]+a[i-1][j]
        a = [[1] * (i+1) for i in range(numRows)]
        for i in range(2,numRows):
            for j in range(1,i):
                a[i][j] = a[i-1][j-1] + a[i-1][j]
        return a