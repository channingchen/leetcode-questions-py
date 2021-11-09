# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1]
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 6 
#  -10 <= nums[i] <= 10 
#  nums 中的所有整数 互不相同 
#  
#  Related Topics 数组 回溯 👍 1627 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        if len(nums) == 1:
            return [nums]

        for i in nums:
            left = list(filter(lambda item: item != i, nums))
            tmp = self.permute(left)
            for j in tmp:
                ret.append([i] + j)

        return ret


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
