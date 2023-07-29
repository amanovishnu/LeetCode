class Solution:
    def soupServings(self, n: int) -> float:
        if n>4275:
            return 1
        n/=25    
        @cache
        def dfs(a,b):
            if a<=0 and b>0:
                return 1

            elif a<=0 and b<=0:
                return 0.5

            elif a>0 and b<=0:
                return 0

            return (dfs(a-4,b)+dfs(a-3,b-1)+dfs(a-2,b-2)+dfs(a-1,b-3))*0.25

        
        return dfs(n,n)           