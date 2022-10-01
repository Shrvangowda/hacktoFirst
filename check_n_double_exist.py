class Solution:
    def checkIfExist(self, arr) -> bool:
        
        map = {}
        for i in arr:
            if i*2 in map or i/2 in map:
                return True
            map[i]=1
        return False




s = Solution()
print(s.checkIfExist([1,2,5,3]))
