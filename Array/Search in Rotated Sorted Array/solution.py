class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1



        if not nums:
            return -1
        
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        pivot = left
        if target >= nums[pivot] and target <= nums[-1]:
            return binary_search(pivot, n - 1)
        return binary_search(0, pivot - 1)
        