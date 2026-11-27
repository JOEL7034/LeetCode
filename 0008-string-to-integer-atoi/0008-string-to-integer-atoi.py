class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -(2**31), 2**31 - 1
        n = len(s)
        idx = 0

    
        while idx < n and s[idx] == " ":
            idx += 1

        
        sign = 1
        if idx < n and s[idx] in ("+", "-"):
            if s[idx] == "-":
                sign = -1
            idx += 1

        
        res = 0
        while idx < n and s[idx].isdigit():
            digit = int(s[idx])

            if sign == 1:
                if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > INT_MAX % 10):
                    return INT_MAX
            else:
                if res > (-INT_MIN) // 10 or (res == (-INT_MIN) // 10 and digit > (-INT_MIN) % 10):
                    return INT_MIN

            res = res * 10 + digit
            idx += 1

        return sign * res