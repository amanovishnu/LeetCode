class Solution {
    
    public static int Bits(int n){
        int c=0;
        while(n!=0){
            c+=(n&1);
            n=n>>1;
        }
        return c;
    }
    
    public int[] countBits(int n) {
		int[] output = new int[n+1];
		for(int i=0;i<=n;i++){
		    System.out.println("Value of i->"+i);
		    output[i] = Bits(i);
		}  
        return output;        
    }
}