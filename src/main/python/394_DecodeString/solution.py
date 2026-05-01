class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        stack = []
        w = ""
        i = 0
        while i < len(s):
            if s[i] == ']':
                el = stack.pop()
                while not el.isnumeric():
                    w = el + w
                    el = stack.pop()
                else:
                    stack.append(w * int(el))
                w = ""
            elif s[i] == '[':
                w = stack.pop()
            elif s[i].isnumeric():
                if w and stack:
                    el = stack.pop()
                    if el.isnumeric():
                        stack.append(el)
                        stack.append(w)
                    else:
                        stack.append(el + w)
                elif w:
                    stack.append(w)
                num = ""
                while s[i].isnumeric() and i >= 0:
                    num = num + s[i]
                    i += 1
                i -= 1
                stack.append(num)
                stack.append("")
            else:
                w = w + s[i]

            i += 1

        if w:
            stack.append(w)

        return "".join(stack)


if __name__ == '__main__':
    solution = Solution()
    assert solution.decodeString("3[a2[c]]") == "accaccacc"
    assert solution.decodeString("abc3[cd]xyz") == "abccdcdcdxyz"
    assert solution.decodeString("100[leetcode]") == 100 * "leetcode"
    assert solution.decodeString(
        "3[z]2[2[y]pq4[2[jk]e1[f]]]ef") == "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
    assert solution.decodeString("2[abc]3[2[cd]]ef") == "abcabccdcdcdcdcdcdef"
