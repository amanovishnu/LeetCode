from collections import Counter

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        output = []
        for floor in bank:
            no_of_ones = Counter(floor).get('1',0)
            if no_of_ones != 0:
                output.append(no_of_ones)
        if len(output) == 1:
            return 0
        else:
            beams = 0
            for idx in range(0,len(output)-1):
                beams += (output[idx] * output[idx+1])
            return beams