class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr=[]

        for i in nums:
            if i not in arr:
                arr.append(i)
        nums[:]=arr    
        return len(arr)