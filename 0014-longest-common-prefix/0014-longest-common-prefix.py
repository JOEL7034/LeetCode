class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
            
        
        first = strs[0]
        
        for i in range(len(first)):
            char = first[i]
            
            for string in strs[1:]:
                
                if i == len(string) or string[i] != char:
                    return first[:i]
                    
        return first