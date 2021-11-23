# 给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，请你判断二者是否相等。# 代表退格字符。 
# 
#  如果相等，返回 true ；否则，返回 false 。 
# 
#  注意：如果对空文本输入退格字符，文本继续为空。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "ab#c", t = "ad#c"
# 输出：true
# 解释：S 和 T 都会变成 “ac”。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "ab##", t = "c#d#"
# 输出：true
# 解释：s 和 t 都会变成 “”。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "a##c", t = "#a#c"
# 输出：true
# 解释：s 和 t 都会变成 “c”。
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "a#c", t = "b"
# 输出：false
# 解释：s 会变成 “c”，但 t 仍然是 “b”。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length, t.length <= 200 
#  s 和 t 只含有小写字母以及字符 '#' 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  你可以用 O(N) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？ 
#  
# 
#  
#  Related Topics 栈 双指针 字符串 模拟 
#  👍 332 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        si = len(s) - 1
        ti = len(t) - 1
        while si >= 0 or ti >= 0:
            si_next = self.process(s, si)
            ti_next = self.process(t, ti)
            if si_next * ti_next < 0 or s[si_next] != t[ti_next]:
                return False
            else:
                si = si_next - 1
                ti = ti_next - 1

        return si == ti

    def process(self, s: str, i: int) -> int:
        if i < 0 or s is None or len(s) == 0:
            return -1
        del_cnt = 0
        while (s[i] == '#' or del_cnt > 0) and i >= 0:
            if s[i] == '#':
                del_cnt += 1
            else:
                del_cnt -= 1
            i -= 1
        return i


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(
        Solution().backspaceCompare("j##yc##bs#srqpfzantto###########i#mwb", "j##yc##bs#srqpf#zantto###########i#mwb"))
