class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] == nums[i] and nums[mid] == nums[j]:
                i = i + 1
                j = j - 1
            elif nums[mid] >= nums[i]:
                if target >= nums[i] and target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            elif nums[mid] <= nums[j]:
                if target > nums[mid] and target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
        return False