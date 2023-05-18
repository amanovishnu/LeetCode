class Solution:
    def average(self, salary: List[int]) -> float:
        counter, min_sal ,max_sal, sum = 0,float('inf'),float('-inf'),0
        for sal in salary:
            counter+=1
            min_sal = min(min_sal,sal)
            max_sal = max(max_sal,sal)
            sum += sal
        return (sum-min_sal-max_sal)/(counter-2)