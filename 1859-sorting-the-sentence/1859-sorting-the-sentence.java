class Solution {
    public String sortSentence(String s) {
	    String[] s_split = s.split(" ");
        String[] res = new String[s_split.length];
        for(String word : s_split){
            res[(int)word.charAt(word.length()-1)-48-1] = word.substring(0, word.length()-1);           
        }
        return String.join(" ", res);
    }
}

// Time Complexity: O(n)
// Space Complexitu: O(n)