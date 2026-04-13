class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        r_max = -1
        for i in range(len(arr)-1,-1,-1):
            cur = arr[i]
            arr[i] = r_max
            if cur > r_max:
                r_max = cur
        return arr