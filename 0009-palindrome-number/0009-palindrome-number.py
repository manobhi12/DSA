class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        s=[]
        s1=[]
        s2=[]
        for i in range(len(str(x))):
            n=x%10
            s.append(n)
            x=x//10
        s1=s[:]
        s2=s[::-1]
        if s1==s2:
            return True
        return False