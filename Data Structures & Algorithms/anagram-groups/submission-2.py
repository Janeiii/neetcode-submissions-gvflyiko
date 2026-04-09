class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for word in strs:
            arr= [0] * 26
            for ch in word:
                index = ord(ch) - ord('a')
                arr[index] += 1
            
            temp_key = str(arr)
            ans[temp_key].append(word)
        return list(ans.values())
