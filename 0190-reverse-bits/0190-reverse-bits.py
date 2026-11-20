class Solution:
    def reverseBits(self, n: int) -> int:
        # Format n as a 32-bit zero-padded binary string, reverse it, and parse back to int
        return int(f"{n:032b}"[::-1], 2)