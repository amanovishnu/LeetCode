class Solution {
    public char findTheDifference(String s, String t) {
	    int[] alpha = new int[26];
        char res = Character.MIN_VALUE;
	    for(int i=0;i<s.length();i++)
	        alpha[s.charAt(i)-'a']++;
	    for(int i=0;i<t.length();i++)
	        alpha[t.charAt(i)-'a']--;
	    for(int i=0; i<26;i++) {
            if(alpha[i]!=0) {
                res = (char)(i+'a');
            }
        }
        return res;
    }
}