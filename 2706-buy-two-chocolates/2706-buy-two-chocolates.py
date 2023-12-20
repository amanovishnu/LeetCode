class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort() # TC: O(nlogn) AS: O(logn) SC: O(n+logn)
        return money if sum(prices[0:2]) > money else money-sum(prices[0:2])