class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        String[] alpha = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
		HashSet<String> unique = new HashSet();
		for(String ele : words){
		    StringBuilder morse = new StringBuilder();
		    for(int i=0; i<ele.length(); i++)
		        morse.append(alpha[(int)ele.charAt(i)-97]);
		    unique.add(morse.toString());
		}
		return unique.size();  
    }
}