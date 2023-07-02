import itertools

class Solution:
    def maximumRequests(self, n, req):
        for k in range(len(req), 0, -1):
            for c in itertools.combinations(range(len(req)), k):
                degree = [0] * n
                for i in c:
                    degree[req[i][0]] -= 1
                    degree[req[i][1]] += 1
                if not any(degree):
                    return k
        return 0