# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重
# 复的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 3000 
#  -10⁵ <= nums[i] <= 10⁵ 
#  
#  Related Topics 数组 双指针 排序 👍 3980 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = nums
        l.sort()
        if len(l) < 3 or l[0] > 0 or l[-1] < 0:
            return []
        if l[0] == 0 and l[-1] == 0:
            return [[0, 0, 0]]

        minv = l[0] + (l[1] if l[1] < 0 else 0)
        maxv = l[-1] + (l[-2] if l[-2] > 0 else 0)
        domain = min(-minv, maxv)

        ret = []
        la = 100
        for i in range(0, len(l) - 2):
            if l[i] == la or l[i] < -domain:
                continue
            a = l[i]
            if a > 0:
                break
            la = a
            s = i + 1
            e = len(l) - 1
            while s < e:
                b = l[s]
                c = l[e]
                sum = a + b + c
                if sum > 0:
                    e = self.move(-1, e, c, l)
                elif sum < 0:
                    s = self.move(1, s, b, l)
                else:
                    ret.append([a, b, c])
                    s = self.move(1, s, b, l)
                    e = self.move(-1, e, c, l)
        return ret

    def move(self, step: int, ci: int, cv: int, l: List[int]):
        ci += step
        while 0 <= ci < len(l) and l[ci] == cv:
            ci += step
        return ci


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    arr = [-1, 0, 1]
    print(Solution().threeSum(arr))
