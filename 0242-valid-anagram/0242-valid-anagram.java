class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
		    return false;
		} else {
		    int[] array = new int[26];
		    for(int i=0; i<s.length(); i++)
		         array[s.charAt(i)-'a']++;
		    for(int i=0; i<s.length(); i++)
		        array[t.charAt(i)-'a']--;
		    for(int ele : array)
		        if(ele != 0)
		            return false;
		    return true;
		}
    }
}