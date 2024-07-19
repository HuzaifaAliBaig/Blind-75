class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = min_product = global_max = nums[0]
        for num in nums[1:]:
            max_product, min_product = max(num, num * max_product, num * min_product), min(num, num * max_product, num * min_product)
            global_max = max(global_max, max_product)
        return global_max