class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # 计算出最多糖果数量
        # 遍历candies，如果元素加上额外糖果数量不小于最多糖果数量，则为真
        res = []
        maxCandy = max(candies)
        for candy in candies:
            if candy + extraCandies >= maxCandy:
                res.append(True)
            else:
                res.append(False)
        return res