class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        idx = 0
        ans =[0]*2*len(nums)
        for i in range(0,2*len(nums),1):
            if i == len(nums):
                idx = 0
            
            ans[i] = nums[idx]
            idx += 1
        return ans