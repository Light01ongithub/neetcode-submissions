class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        duplicate=0
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                duplicate=nums[i]
        
        actual_sum=(len(nums)*(len(nums)+1))/2
        nums_sum=sum(set(nums))
        missing=actual_sum-nums_sum

        return [duplicate,int(missing)]
# i tried so many methods and wasted two days on it 