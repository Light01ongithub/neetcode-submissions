class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1

        answer=float('inf')
        while low<=high:
            mid=(low+high)//2

            answer=min(answer,nums[mid])

            if nums[mid]>nums[high]:
                low=mid+1
            else:
                high=mid-1
            
        return answer