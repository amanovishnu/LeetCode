class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        HashMap<Character, Integer> jewelBox = new HashMap<Character, Integer>();
        int output = 0;
        
        for(int i=0; i<stones.length(); i++) {
            if (jewelBox.containsKey(stones.charAt(i)))
                jewelBox.put(stones.charAt(i), jewelBox.get(stones.charAt(i))+1);
            else
                jewelBox.put(stones.charAt(i), 1);
        }
        
        for(int i=0; i<jewels.length();i++){
            if(jewelBox.get(jewels.charAt(i)) != null)
                output += jewelBox.get(jewels.charAt(i));
        }
        return output;
    }
}