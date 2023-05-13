class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            output.append(len(re.findall('1',str(bin(i)))))
        return output