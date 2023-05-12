class Solution {
    public int sumOfUnique(int[] nums) {
       HashMap<Integer, Integer>dict = new HashMap<Integer, Integer>();
		for(int num : nums){
		    if (dict.containsKey(num)==true)
		        dict.put(num, dict.get(num)+1);
		    else
		        dict.put(num, 1);
		}
		
		ArrayList<Integer> unique = new ArrayList<Integer>();
		for(int i : dict.keySet()){
		    if(dict.get(i) == 1)
		        unique.add(i);
		}
		
		int output = 0;
		for(int i=0; i<unique.size();i++)
		    output += unique.get(i);
		 
		return output; 
    }
}