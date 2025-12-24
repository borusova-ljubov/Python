from operator import truediv, length_hint
from wsgiref.validate import PartialIteratorWrapper

candies = (
    [[5,3,3,2,1],3],        #odd
    [[5,3,3,2,1,1],3],      #even
    [[15,14,13,4,3,2,1],2], #odd
    [[15,14,13,13,3,2,1],3],    #odd
    [[1,1,1,1,1,1,1],6],        #odd
    [[1,1,1,1,1,1,1,1],7],      #even
    [[15,5,5,5,5,1], 0],
    [[15,5,5,5,5,5,1], 0],
    [[15,12,12,12,12,12,12,1], 6],      #even

    [[5, 4, 3, 2, 1], 3],
    [[5, 5, 5, 1, 1], 2],
    [[5, 5, 5, 5, 1, 1], 3],        #even
    [[10, 8, 7, 1, 1, 1, 1], 2],
    [[9, 8, 7, 6, 1, 1], 3],        #even
    [[10, 1, 1, 1, 1], 0],
    [[10, 1, 1, 1, 1, 1], 0],       #even
    [[5, 1], 0],        #even
    [[0, 0], 1],  # even
    [[5, 1, 1], 0],
    [[6, 6], 1],        #even
    [[6, 6, 6], 2],
    [[15,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,11,1], 17],      #even
    [[15,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,11,1], 18],
    [[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8], 19],      #even
    [[12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
      8, 8, 8, 8, 8, 8, 8, 8, 8], 19],

)
extraCandies = 3
maxCan = 0


class FindMaxInTree:
    def searchBorder(self, candies: [int], extraCandies: int, maxCan: int, middle: int, binaryLen: int)-> int:

        if candies[middle]+extraCandies >= maxCan:
            if binaryLen == 1: #идем в правую часть
                return middle
            binaryLenOddCorrection = 0
            binaryLen = binaryLen//2
            if binaryLen % 2 == 0:
                binaryLenOddCorrection = 1
            fb = self.searchBorder(candies, extraCandies, maxCan, middle - binaryLenOddCorrection + 1 + binaryLen//2, binaryLen)
            if fb == -1 or (candies[fb] + extraCandies < maxCan) :
                 return middle
            else:
                 return fb
        else: #идем в левую часть
            if binaryLen == 1:
                return -1
            else:
                binaryLenOddCorrection = 0
                if binaryLen % 2 == 0:
                    binaryLenOddCorrection = 1
                fb = self.searchBorder(candies, extraCandies, maxCan, (middle - 1) - binaryLen//4, (binaryLen + binaryLenOddCorrection - 1)//2)
                return fb


solution = FindMaxInTree()
for candieTuple in candies:
    binaryLenOddCorrection = 0
    if len(candieTuple[0]) % 2 == 0:
        binaryLenOddCorrection = 1
    fb = solution.searchBorder(candieTuple[0], 3, candieTuple[0][0], len(candieTuple[0])//2 - binaryLenOddCorrection, len(candieTuple[0]))
    if fb == candieTuple[1]:
        print("\033[32m{} PASSED\033[0m".format(candieTuple[0]))
    else:
        print("\033[31m{} FUCKED UP, expected found border - {}, but {} found \033[0m".format(candieTuple[0], candieTuple[1], fb))
