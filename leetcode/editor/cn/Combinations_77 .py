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
        ret = self.solve(1, n, k)
        return ret

    def solve(self, s: int, e: int, k: int) -> list[list[int]]:
        ret = []
        if k == 1:
            for i in range(s, e + 1):
                ret.append([i])
            return ret

        if e - s + 1 == k:
            return [list(range(s, e + 1))]

        if e - s + 1 < k:
            return []

        for i in range(s, e + 1):
            tmp = self.solve(i + 1, e, k - 1)
            if len(tmp) == 0:
                break
            for t in tmp:
                ret.append([i] + t)

        return ret


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().combine(2, 2))
