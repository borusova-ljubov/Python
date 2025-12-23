from operator import truediv, length_hint
from wsgiref.validate import PartialIteratorWrapper

#Output: [true,true,true,false,true]
# candies = [15,14,13,4,3,2,1]#happy path
# candies = [15,14,13,13,3,2,1]
# candies = [1,1,1,1,1,1,1]
# candies = [15,5,5,5,5,1]
# candies = [15,5,5,5,5,5,1]
# candies = [15,12,12,12,12,12,12,1]
candies = [5,3,3,2,1]
# candies = [5,5,5,5,5,5]
extraCandies = 3
maxCan = 0


class FindMaxInTree:
    def searchBorder(self, candies: [int], extraCandies: int, maxCan: int, middle: int, binaryLen: int)-> int:

        # if candies[middle]+extraCandies > maxCan and candies[middle + 1] < candies[middle]:
        if candies[middle]+extraCandies >= maxCan:
            if binaryLen == 1: #идем в правую часть
                return middle
            binaryLenOddCorrection = 0
            binaryLen = binaryLen//2
            if binaryLen % 2 == 0:
                binaryLenOddCorrection = 1
            fb = self.searchBorder(candies, extraCandies, maxCan, middle - binaryLenOddCorrection + 1 + binaryLen//2, binaryLen)
            if candies[middle] > candies[fb] + extraCandies:
                 return middle
            else:
                 return fb
            #return fb
        else: #идем в левую часть
            if binaryLen == 1:
                return middle
            else:
                binaryLenOddCorrection = 0
                if binaryLen % 2 == 0:
                    binaryLenOddCorrection = 1
                fb = self.searchBorder(candies, extraCandies, maxCan, (middle - 1) - binaryLen//4, (binaryLen + binaryLenOddCorrection - 1)//2)
                return fb


solution = FindMaxInTree()
binaryLenOddCorrection = 0
if len(candies) % 2 == 0:
    binaryLenOddCorrection = 1
fb = solution.searchBorder(candies, 3, candies[0], len(candies)//2 - binaryLenOddCorrection, len(candies))
print(fb)