class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans ={}
        
        for i in strs:
            temp_key = str(sorted(i))
            if temp_key in ans.keys():
                ans[temp_key].append(i)
            else:
                ans[temp_key] = [i] # str

        return list(ans.values())