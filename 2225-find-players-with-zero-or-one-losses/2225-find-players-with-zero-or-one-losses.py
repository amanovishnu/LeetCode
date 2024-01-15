class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # Convert matches to [[winner, winner, ...], [loser, loser, ...]]
        wl = list(zip(*matches))
        
        # Initialize lostZero to all winners.
        # We will remove a winner if he/she loses a match.
        lostZero = set(wl[0])
        
        # We will append if he/she lost exactly one match.
        lostOne = []
        
        # count the number of matches he/she losts.
        countLost = Counter(wl[1])
        
        
        for key in countLost.keys():
            # Remove a winner if he/she lost a match.
            if countLost[key] > 0 and key in lostZero: lostZero.remove(key)
            # Append if he/she lost exactly one match.
            if countLost[key] == 1: lostOne.append(key)
        
        # Sort the two lists before return
        return [sorted(list(lostZero)),sorted(lostOne)]