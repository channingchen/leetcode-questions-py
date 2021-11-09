# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。 
# 
#  你可以按 任何顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 4, k = 2
# 输出：
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
# 
#  示例 2： 
# 
#  
# 输入：n = 1, k = 1
# 输出：[[1]] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 20 
#  1 <= k <= n 
#  Related Topics 数组 回溯
#  👍 759 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

    def solve(self, s: int, e: int, k: int) -> list[list[int]]:
        ret = []
        for i in range(s, e):
            tmp = self.solve(s - 1, e - 1)
            for t in tmp:
                ret.append([i] + t)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().
