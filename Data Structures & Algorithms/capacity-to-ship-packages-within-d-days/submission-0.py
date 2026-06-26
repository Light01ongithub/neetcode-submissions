class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        answer=float('inf')
        while low<=high:
            
            mid=(low+high)//2

            day_used=1
            sume=0
            for i in range(len(weights)):
                if sume+weights[i]<=mid:
                    sume+=weights[i]
                elif sume<=mid:
                    day_used+=1
                    sume=weights[i] 

            if day_used<=days:
                answer=min(answer,mid)
                high=mid-1
            else:
                low=mid+1
            
        return answer
        
