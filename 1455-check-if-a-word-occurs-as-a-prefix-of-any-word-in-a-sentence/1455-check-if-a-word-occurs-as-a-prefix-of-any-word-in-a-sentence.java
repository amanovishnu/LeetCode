class Solution {
    public int isPrefixOfWord(String sentence, String searchWord) {
        
        String[] sentences = sentence.split(" ");
	    int searchWordLength = searchWord.length();
	    int output = -1;
		
		for(int i=0;i<sentences.length;i++){
		    if (sentences[i].length() >= searchWordLength) {
		        if(sentences[i].substring(0,searchWordLength).equals(searchWord)) {
		            output = i+1;
		            break;
		        }
		    }
		}
        return output;
    }
}