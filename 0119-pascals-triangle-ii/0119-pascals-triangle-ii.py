class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1] * (rowIndex + 1)
        
        for r in range(2, rowIndex + 1):
            for c in range(r - 1, 0, -1):
                row[c] += row[c - 1]
                
        return row