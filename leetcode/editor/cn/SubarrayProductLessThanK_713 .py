# 给定一个正整数数组 nums和整数 k 。 
# 
#  请找出该数组内乘积小于 k 的连续的子数组的个数。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [10,5,2,6], k = 100
# 输出: 8
# 解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
# 需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [1,2,3], k = 0
# 输出: 0 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 3 * 104 
#  1 <= nums[i] <= 1000 
#  0 <= k <= 106 
#  
#  Related Topics 数组 滑动窗口 
#  👍 312 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        mem_dict = {}
        solution = 0
        for n in range(len(nums)):
            if nums[n] < k:
                solution += 1
            mem_dict[str(n) + "_1"] = nums[n]

        for w in range(2, len(nums) + 1):
            i = 0
            while i <= len(nums) - w:
                key=str(i) + "_" + str(w - 1)
                if mem_dict.has_key(key):
                if r and r < k:
                    r *= nums[i + w - 1]
                    if r < k:
                        # print(nums[i:i + w])
                        solution += 1
                        mem_dict[str(i) + "_" + str(w)] = r
                i += 1
        return solution


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().numSubarrayProductLessThanK([10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3], 19))
