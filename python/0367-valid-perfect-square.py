class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num

        while (left <= right):
            mid = (left + right) >> 1
            sq = mid * mid
            
            if sq > num:
                right = mid - 1
            elif sq < num:
                left = mid + 1
            else:
                return True
        
        return False
