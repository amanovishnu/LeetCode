class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int[] res = new int[nums.length];
        int l = 0, r = res.length-1;
        for(int idx=0;idx<nums.length;idx++){
            if(nums[idx]%2==0) {
                res[l] = nums[idx];
                l++;
            } else {
                res[r] = nums[idx];
                r--;
            }
        }
        return res;
    }
}