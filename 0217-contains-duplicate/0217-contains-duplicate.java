class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> hash = new HashSet<>();
	    for(int num : nums) {
	         if(!hash.add(num))  // add method returns false if num is already in the set
	            return true;  
	    }
		return false;
    }
}