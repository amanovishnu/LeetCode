class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        value = arr[0]
        max_frequency = 0
        local_frequency = 0
        for idx in range(len(arr)-1):
            if arr[idx] != arr[idx+1]:
                local_frequency = 0
            local_frequency +=1
            if local_frequency >= max_frequency:
                max_frequency = local_frequency
                value = arr[idx] if max_frequency >= ceil(len(arr)/4) else value
        return value