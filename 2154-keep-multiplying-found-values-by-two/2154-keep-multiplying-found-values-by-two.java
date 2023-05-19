class Solution {
    public int findFinalValue(int[] nums, int original) {
	    HashSet<Integer> hash = new HashSet<Integer>();
        for(int num : nums)
            hash.add(num);
        while(hash.contains(original))
            original*=2;
        return original; 
    }
}