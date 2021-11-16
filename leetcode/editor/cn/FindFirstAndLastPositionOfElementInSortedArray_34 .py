# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。 
# 
#  如果数组中不存在目标值 target，返回 [-1, -1]。 
# 
#  进阶： 
# 
#  
#  你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？ 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4] 
# 
#  示例 2： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1] 
# 
#  示例 3： 
# 
#  
# 输入：nums = [], target = 0
# 输出：[-1,-1] 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 105 
#  -109 <= nums[i] <= 109 
#  nums 是一个非递减数组 
#  -109 <= target <= 109 
#  
#  Related Topics 数组 二分查找 
#  👍 1295 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s = 0
        e = len(nums) - 1
        last = -2
        m = -1
        while last != m and s <= e:
            last = m
            m = int((s + e) / 2)
            if nums[m] < target:
                s = m + 1
            elif nums[m] > target:
                e = m - 1
            else:
                s1 = m
                e1 = m
                while s1 - 1 >= 0 and nums[s1 - 1] == target:
                    s1 = s1 - 1
                while e1 + 1 < len(nums) and nums[e1 + 1] == target:
                    e1 = e1 + 1
                return [s1, e1]
        return [-1, -1]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    arr = [1, 8]
    print(Solution().searchRange(arr, 8))
