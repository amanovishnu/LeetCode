class Solution {
    public int arraySign(int[] nums) {
        int neg_counter = 0;
        for(int num : nums){
            if(num==0)
                return 0;
            else if(num <0)
                neg_counter++;
        }
        return neg_counter%2==0 ? 1 : -1;
    }
}