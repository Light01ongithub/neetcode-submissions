from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)

        answer=float('inf')
        while low<=high:
            mid=(low+high)//2

            total_hr=0

            for i in range(len(piles)):
                total_hr+=ceil(piles[i]/mid)

            if total_hr>h:
                low=mid+1
            else:
                answer=min(mid,answer)
                high=mid-1
        return answer