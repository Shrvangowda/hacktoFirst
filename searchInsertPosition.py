#35. Search Insert Position(LeetCode)
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        nums.append(float('inf'))
        left,right = 0,len(nums)-1
        while(left<right):
            mid = (left+right)//2
            if target<=nums[mid]:
                right = mid
            else:
                left = mid+1
        return left


s = Solution()
print(s.searchInsert([1,3,5,6],5))