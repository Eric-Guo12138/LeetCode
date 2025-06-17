class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 花能种的地方必须是i-1,i,i+1都为0，为了方便可以在数组前后都加个0
        flowerbed = [0] + flowerbed +[0]
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[i] = 1
                n -= 1
        if n <= 0:
            return True
        else:
            return False