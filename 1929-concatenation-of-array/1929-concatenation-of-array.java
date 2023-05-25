class Solution {
    public int[] getConcatenation(int[] nums) {
        int num_len = nums.length;
        int[] output = new int[2*num_len];
        for(int i=0; i<num_len; i++) {
            output[i] = nums[i];
            output[i+num_len] = nums[i];
        }
        return output;
    }
}
// Time Complexity : O(n)
// Space Complexity : O(n)