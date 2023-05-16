class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            if i == 0:
                output.append(0)
            elif i == 1:
                output.append(1)
            else:
                res = output[i//2] if i%2==0 else output[i//2]+1
                output.append(res)
        return output