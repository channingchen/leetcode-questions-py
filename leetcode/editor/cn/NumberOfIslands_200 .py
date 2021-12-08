# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  grid[i][j] 的值为 '0' 或 '1' 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 1449 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        x = 0
        y = 0
        h = len(grid)
        w = len(grid[0])
        for i in range(h):
            for j in range(w):
                if grid[x][y] == '1':
                    x = i
                    y = j
                    break

        if x == h - 1 and y == w - 1 and grid[x][y] == "0":
            return 0

        cnt = 0
        while x < h and y < w:
            marked = dict()
            self.bfsAndDeleteAnIsland((x, y), grid, marked)
            for p in marked.keys():
                grid[p[0]][p[1]] = "0"
            cnt += 1

            i = x
            j = y
            for i in range(x, h):
                for j in range(w):
                    if grid[i][j] == "1":
                        break
            if i == h - 1 and y == w - 1 and grid[x][y] == "0":
                return cnt
            else:
                x = i
                y = j

    def bfsAndDeleteAnIsland(self, point: tuple, grid: List[List[str]], marked: dict) -> dict:
        marked[tuple] = 1
        next = []
        x = point[0]
        y = point[1]
        if self.isVerginLand(x - 1, y, grid, marked): next.append((x - 1, y))
        if self.isVerginLand(x + 1, y, grid, marked): next.append((x + 1, y))
        if self.isVerginLand(x, y - 1, grid, marked): next.append((x, y - 1))
        if self.isVerginLand(x, y + 1, grid, marked): next.append((x, y + 1))

        if len(next) > 0:
            map(lambda p: self.bfsAndDeleteAnIsland(p, grid), next)

        return marked

    def isVerginLand(self, x: int, y: int, grid: List[List[str]], marked: dict) -> bool:
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return False
        if grid[x][y] == "0":
            return False
        if (x, y) in marked:
            return False

        return True


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(Solution().numIslands(grid))
