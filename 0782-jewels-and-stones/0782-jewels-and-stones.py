class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        # Apporach 1 Using Dictionary
        # jewel_box = {}
        # output = 0
        # for stone in stones:
        #     if stone in jewel_box:
        #         jewel_box[stone] += 1
        #     else:
        #         jewel_box[stone] = 1              
        # for jewel in jewels:
        #     output += jewel_box.get(jewel,0)         
        # return output

        # Apporach 2 Using Regular Expressions
        output = 0
        for jewel in jewels:
            output += len(re.findall(jewel, stones))
        return output