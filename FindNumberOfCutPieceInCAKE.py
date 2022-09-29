'''
It is Edward's birthday today. His friends have bought him a huge circular cake.
Edward wants to find out the maximum number of pieces he can get by making exactly N straight vertical
cuts on the cake.
Your task is to write a function that returns the maximum number of pieces that can be obtained by making
N number of cuts.
Note: Since the answer can be quite large, modulo it by 1000000007
Input Specification:
input1: An integer N denoting the number of cuts
Output Specification:
Return the maximum number of pieces that can be obtained by making N cuts on the cake
'''
class Solution:
 def maximumCuts(self, n):
     M = 1000000007
     num=((n*(n+1))//2) +1
     return num % M
if __name__ == '__main__':
 n = int(input())
 ob = Solution()
 ans = ob.maximumCuts(n)
 print(ans)
