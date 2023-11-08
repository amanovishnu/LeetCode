class Solution:
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        if sx == fx and sy == fy:
            return t != 1
        return max(abs(sx - fx), abs(sy - fy)) <= t