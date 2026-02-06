class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        fizzbuzz=[]
        for num in range(1,n+1):
            if num%3==0 and num%5==0:
                fizzbuzz.append("FizzBuzz")
            elif num%3==0:
                fizzbuzz.append("Fizz")
            elif num%5==0:
                fizzbuzz.append("Buzz")
            else:
                fizzbuzz.append(str(num))
        return fizzbuzz

        