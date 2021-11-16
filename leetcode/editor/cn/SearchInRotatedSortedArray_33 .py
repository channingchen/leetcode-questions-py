# 整数数组 nums 按升序排列，数组中的值 互不相同 。 
# 
#  在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[
# k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2
# ,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。 
# 
#  给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1 
# 
#  示例 3： 
# 
#  
# 输入：nums = [1], target = 0
# 输出：-1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 5000 
#  -10^4 <= nums[i] <= 10^4 
#  nums 中的每个值都 独一无二 
#  题目数据保证 nums 在预先未知的某个下标上进行了旋转 
#  -10^4 <= target <= 10^4 
#  
# 
#  
# 
#  进阶：你可以设计一个时间复杂度为 O(log n) 的解决方案吗？ 
#  Related Topics 数组 二分查找 
#  👍 1672 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        r = self.findRotate(nums)
        s = 0
        e = len(nums) - 1
        if r >= 0:
            if nums[0] <= target:
                e = r
            elif nums[-1] >= target:
                s = r

        while s <= e:
            m = int((s + e) / 2)
            if e - s == 1:
                if nums[e] == target:
                    return e
                if nums[s] == target:
                    return s
                return -1
            if nums[m] < target:
                s = m + 1
            elif nums[m] > target:
                e = m - 1
            else:
                return m
        return -1

    def findRotate(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return -1
        s = 0
        e = len(nums) - 1
        while s < e:
            m = int((s + e) / 2)

            if nums[m] > nums[s]:
                s = m
            elif nums[m] < nums[e]:
                e = m
            else:
                if e - s == 1:
                    return s

    # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    arr = [3, 1]
    # print(Solution().findRotate(arr))

    print(Solution().search(arr, 1))
