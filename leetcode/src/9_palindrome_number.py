class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        valid = False
        s = str(x)
        s1 = ""
        length = len(s) - 1
        while length >= 0:
            s1 = s1 + s[length]
            length = length - 1
        if str(x) == s1:
            valid = True
        return valid


solution = Solution()
solution.isPalindrome(21212)
