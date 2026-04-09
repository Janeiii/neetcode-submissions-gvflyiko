class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans ={}
        for word in strs:
            arr= [0] * 26
            for ch in word:
                index = ord(ch) - ord('a')
                arr[index] += 1
            
            temp_key = str(arr)
            if temp_key in ans.keys():
                ans[temp_key].append(word)
            else:
                ans[temp_key] = [word]
        return list(ans.values())
