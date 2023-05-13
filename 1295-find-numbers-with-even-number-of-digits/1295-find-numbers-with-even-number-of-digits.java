class Solution {
    public int findNumbers(int[] nums) {
      int counter = 0;
		for(int num : nums)
		    if((int)(Math.log10(num)+1)%2 == 0)
                counter++;
		return counter;  
    }
}