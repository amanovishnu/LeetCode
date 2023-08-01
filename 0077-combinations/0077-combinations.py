class Solution:
    def __init__(self):
        self.res = []

    def solve1(self, num, tot, k, ans):
        if num == tot + 1:
            if len(ans) == k:
                self.res.append(ans[:])
            return

        ans.append(num)
        self.solve1(num + 1, tot, k, ans)
        ans.pop()
        self.solve1(num + 1, tot, k, ans)

    def solve2(self, num, tot, k, ans):
        if len(ans) == k:
            self.res.append(ans[:])
            return
        for i in range(num, tot + 1):
            ans.append(i)
            self.solve2(i + 1, tot, k, ans)
            ans.pop()

    def combine(self, n, k):
        ans = []
        self.solve2(1, n, k, ans)
        return self.res