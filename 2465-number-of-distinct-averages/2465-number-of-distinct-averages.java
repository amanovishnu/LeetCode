class Solution {
    public int distinctAverages(int[] nums) {
       int l = 0, r = nums.length-1;
	   HashSet<Double> res = new HashSet<>();
       Arrays.sort(nums);
       while(l<r){
           res.add((nums[l]+nums[r])/2.0);
           l++;
           r--;
       }
       return res.size();
    }
}