class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
		    return false;
		} else {
		    int[] array = new int[26];
		    for(char ch : s.toCharArray())
		        array[ch-'a']++;
		    for(char ch : t.toCharArray())
		        array[ch-'a']--;
		    for(int ele : array)
		        if(ele != 0)
		            return false;
		    return true;
		}
    }
}