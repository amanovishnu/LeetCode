class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        HashMap<Integer, String> hash = new HashMap<Integer, String>();  // SC: O(n)
		String[] output = new String[names.length]; // SC: O(n)
		
		for(int idx=0;idx<heights.length;idx++)  // TC: O(n)
		    hash.put(heights[idx], names[idx]);
		
		Arrays.sort(heights);  //TC: O(nlogn)
		
		for(int idx=heights.length-1; idx>=0; idx--) // TC: O(n)
		    output[output.length-idx-1] = hash.get(heights[idx]); // TC: O(1)
		
		return output;
    }
}


// Time Complexity : O(nlogn)
// Space Complexity: O(n)