class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> hash = new HashSet<>();
	    for(int num : nums) {
	         if(hash.contains(num)==true)
	            return true;
	        else
	            hash.add(num);   
	    }
		return false;
    }
}