class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = {}
        for i in nums:
            if i in ans.keys():
                ans[i] += 1
            else: 
                ans[i] = 1
        flag=False
        for k,v in ans.items():
            if v > 1:
                flag = True
        return flag
    


        