class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_box = {}
        output = 0
        for stone in stones:
            if stone in jewel_box:
                jewel_box[stone] += 1
            else:
                jewel_box[stone] = 1              
        for jewel in jewels:
            output += jewel_box.get(jewel,0)         
        return output