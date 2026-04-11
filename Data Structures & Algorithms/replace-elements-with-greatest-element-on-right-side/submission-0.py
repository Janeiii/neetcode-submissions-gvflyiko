class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            t_max = 0 
            for j in range(i+1,len(arr)):
                if arr[j] > t_max:
                    t_max = arr[j]
            arr[i] = t_max
        arr[-1] = -1
        return arr