class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        planted = 0

        for i in range(len(flowerbed)):
            left_empty = (i == 0 or flowerbed[i - 1] == 0)
            right_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)

            if flowerbed[i] == 0 and left_empty and right_empty:
                flowerbed[i] = 1
                planted += 1

        return planted >= n
