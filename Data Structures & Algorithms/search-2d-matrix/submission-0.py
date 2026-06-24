class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        g=len(matrix[0])
        f=len(matrix)
        low=0
        high=(g*f)-1

        while low<=high:
            mid=(low+high)//2
            r=mid//g
            c=mid%g
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]>target:
                high=mid-1
            else:
                low=mid+1
        return False