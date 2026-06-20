class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        var1=list(s)
        var2=list(t)

        if len(var1)!= len(var2):
            return False
        
        for ch in var2:
            if ch not in var1:
                return False
            var1.remove(ch)

        if not var1:
            return True
        return False