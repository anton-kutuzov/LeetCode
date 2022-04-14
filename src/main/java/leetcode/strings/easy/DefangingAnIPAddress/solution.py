class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        res = ''
        for char in address:
            if char == '.':
                res += '[.]'
            else:
                res += char
        return res


solution = Solution()
print(solution.defangIPaddr("13.1.4.1"))