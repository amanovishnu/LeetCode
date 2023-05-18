class Solution {
    public char findTheDifference(String s, String t) {
	    int output = 0;
	    output ^= (int)t.charAt(t.length()-1);
	    for(int i=0;i<s.length();i++) {
	        output ^= (int)s.charAt(i);
	        output ^= (int)t.charAt(i);
	    }
	    return (char)output;
        
        // int[] alpha = new int[26];
	    // char res = Character.MIN_VALUE;
	    // for(int i=0;i<s.length();i++)
	    //     alpha[s.charAt(i)-'a']++;
	    // for(int i=0;i<t.length();i++)
	    //     alpha[t.charAt(i)-'a']--;
	    // for(int i=0; i<26;i++) {
	    // if(alpha[i]!=0) {
	    // res = (char)(i+'a');
	    // }
	    // }
	    // return res;
          
    }
}