class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -(2**31), 2**31 - 1
        sign = -1 if x < 0 else 1
        num = abs(x)
        rev = 0

        while num != 0:
            digit = num % 10
            num //= 10

            
            if sign == 1:
                if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > INT_MAX % 10):
                    return 0
            else:
                if rev > (-INT_MIN) // 10 or (rev == (-INT_MIN) // 10 and digit > (-INT_MIN) % 10):
                    return 0

            rev = rev * 10 + digit

        return sign * rev