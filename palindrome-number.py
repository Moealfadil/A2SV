def isPalindrome( x):
        """
        :type x: int
        :rtype: bool
        """
        string= str(x)
        reversed_str= ''.join(reversed(string))
        return string== reversed_str
print(isPalindrome(12121))