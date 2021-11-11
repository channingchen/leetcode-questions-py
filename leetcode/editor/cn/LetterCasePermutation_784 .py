# 给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。 
# 
#  
# 
#  示例：
# 输入：S = "a1b2"
# 输出：["a1b2", "a1B2", "A1b2", "A1B2"]
# 
# 输入：S = "3z4"
# 输出：["3z4", "3Z4"]
# 
# 输入：S = "12345"
# 输出：["12345"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  S 的长度不超过12。 
#  S 仅由数字和字母组成。 
#  
#  Related Topics 位运算 字符串 回溯 👍 318 👎 0
from builtins import str
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ret = []
        p = [-1] * len(s)
        c = 0
        for i in range(len(s)):
            if ord(s[i]) >= 65:
                p[c] = i
                c += 1

        for i in range(1 << c):
            n = list(s)
            for j in range(c, 0, -1):
                if (i >> j) & 1 == 1:
                    n[p[j]] = n[p[j]].swapcase()
            ret.append(''.join(n))
        return ret


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    str = "a1b2"
    ret = Solution().letterCasePermutation(str)
    print(ret)
