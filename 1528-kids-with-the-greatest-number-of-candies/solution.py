class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []
        for i in candies:
            new = extraCandies + i
            if new >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result
