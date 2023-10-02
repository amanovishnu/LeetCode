class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        count_A = 0
        count_B = 0
        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == 'A':
                    count_A += 1
                else:
                    count_B += 1
        return count_A > count_B