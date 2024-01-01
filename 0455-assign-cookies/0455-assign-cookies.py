class Solution(object):
    def findContentChildren(self, g, s):
        cookiesNums = len(s)
        if cookiesNums == 0:
            return 0
        g.sort()
        s.sort()

        maxNum = 0
        cookieIndex = cookiesNums - 1
        childIndex = len(g) - 1
        while cookieIndex >= 0 and childIndex >= 0:
            if s[cookieIndex] >= g[childIndex]:
                maxNum += 1
                cookieIndex -= 1
                childIndex -= 1
            else:
                childIndex -= 1

        return maxNum
