class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

       
        num = x // 2

     
        while num > x // num:
            num = (num + x // num) // 2

        return num