class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i = 0
        j = len(arr) - 1
        n = len(arr)
        while i <= j:
            mid = (i + j) // 2
            if (mid == 0 or arr[mid - 1] < arr[mid]) and (mid == n - 1 or arr[mid + 1] < arr[mid]):
                return mid
            elif mid > 0 and arr[mid - 1] > arr[mid]:
                j = mid - 1
            else:
                i = mid + 1
        return -1