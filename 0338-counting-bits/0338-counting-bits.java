class Solution {    
    public int[] countBits(int n) {
		int [] output = new int[n+1];
		for(int i=0;i<=n;i++) {
		    if(i==0)
		        output[0] = 0;
		    else if(i==1)
		        output[1] = 1;
		    else {
		        int temp = (i%2==0) ? output[i/2] : output[i/2]+1;
		        output[i] = temp;
		    }
		}
        return output;        
    }
}