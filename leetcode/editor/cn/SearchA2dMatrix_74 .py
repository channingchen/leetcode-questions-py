# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性： 
# 
#  
#  每行中的整数从左到右按升序排列。 
#  每行的第一个整数大于前一行的最后一个整数。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 100 
#  -104 <= matrix[i][j], target <= 104 
#  
#  Related Topics 数组 二分查找 矩阵 
#  👍 531 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s = 0
        e = len(matrix) - 1
        row = 0
        while len(matrix) > 1 and s <= e:
            m = int((s + e) / 2)
            if e - s <= 1:
                row = s if matrix[e][0] > target else e
                break

            if matrix[m][0] <= target < matrix[m + 1][0]:
                row = m
                break
            elif target < matrix[m][0]:
                e = m
            elif target >= matrix[m + 1][0]:
                s = m

        s = 0
        e = len(matrix[row]) - 1
        while s <= e:
            m = int((s + e) / 2)
            if e - s <= 1:
                return True if matrix[row][s] == target or matrix[row][e] == target else False

            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                e = m
            elif matrix[row][m] < target:
                s = m
        return False


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    arr = [[1], [3], [5]]
    print(Solution().searchMatrix(arr, 5))
