class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        min_unfairness = float('inf')
        distribution = [0] * k
        
        def backtrack(i):
            nonlocal min_unfairness, distribution
            
            if i == len(cookies):
                min_unfairness = min(min_unfairness, max(distribution))
                return
            
            # Bounding condition to stop a branch if unfairness already exceeds current optimal solution
            if min_unfairness <= max(distribution):
                return
            
            for j in range(k):
                distribution[j] += cookies[i]
                backtrack(i + 1)
                distribution[j] -= cookies[i]
        
        backtrack(0)
        return min_unfairness