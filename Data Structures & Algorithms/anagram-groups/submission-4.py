class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for word in strs:
            key = [0] * 26
            for ch in word:
                index = ord(ch) - ord('a')
                key[index] += 1
            
            ans[str(key)].append(word)
        return list(ans.values())
