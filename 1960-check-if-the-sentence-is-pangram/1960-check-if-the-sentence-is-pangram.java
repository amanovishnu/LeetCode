class Solution {
    public boolean checkIfPangram(String sentence) {
        
        HashMap<Character, Integer> alpha_dict = new HashMap<Character, Integer>();
	    
	    for(int i=0;i<26;i++) {
	        alpha_dict.put((char)(i+97), 0);
	    }
	    
	    for(int i=0; i<sentence.length(); i++) {
	        alpha_dict.put(sentence.charAt(i), alpha_dict.get(sentence.charAt(i))+1);
	    }
	    
	    return !alpha_dict.containsValue(0);
    }
}