class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n, Y = len(customers), 0
        for i in range(n):
            Y += (1 if customers[i] == 'Y' else 0)
        min_p, hour, y_found, n_found = n, n, 0, 0
        for h in range(n + 1):
            y_remaining = Y - y_found
            pen = y_remaining + n_found
            if pen < min_p:
                hour = h
                min_p = pen
            n_found += (1 if h < n and customers[h] == 'N' else 0)
            y_found += (1 if h < n and customers[h] == 'Y' else 0)
        return hour