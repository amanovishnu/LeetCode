class Solution {
    public int thirdMax(int[] nums) {
        TreeSet<Integer> sorted_nums = new TreeSet<Integer>();
        for(int num : nums) {
            if(sorted_nums.contains(num))
                continue;
            if(sorted_nums.size()==3) {
                if(sorted_nums.first()<num) {
                    sorted_nums.pollFirst();
                    sorted_nums.add(num);
                }
            }
            else {
                sorted_nums.add(num);
            }
        }
        if(sorted_nums.size()==3)
            return sorted_nums.first();
        else
            return sorted_nums.last();
    }
}

// Time Complextiy: O(nlogn)
// Space Complexity: O(n)