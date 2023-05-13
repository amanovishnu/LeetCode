class Solution {
    public int vowelStrings(String[] words, int left, int right) {
        char one , two;
		int output = 0;
		for (int i=left;i<=right;i++) {
		    one = words[i].charAt(0);
		    two = words[i].charAt(words[i].length()-1);
		    if((one=='a'||one=='e'||one=='i'||one=='o'||one=='u')&&(two=='a'||two=='e'||two=='i'||two=='o'||two=='u'))
		        output++;
		}     
        return output;     
    }
}