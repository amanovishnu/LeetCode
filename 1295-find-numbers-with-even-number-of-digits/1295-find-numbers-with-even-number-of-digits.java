class Solution {
    public int findNumbers(int[] nums) {
      int counter = 0;
		for(int num : nums){
		    if(num%10 == 0) {
		        if(Math.floor(Math.log10(num)+1)%2 == 0)
		            counter++;
		    } else {
		        if(num!=1 && Math.ceil(Math.log10(num))%2 == 0)
		            counter++;
		    }
		}
		return counter;  
    }
}