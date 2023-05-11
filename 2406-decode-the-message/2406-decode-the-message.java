class Solution {
    public String decodeMessage(String key, String message) {

        // Approach 1 Using Hashing
        // HashMap<Character, Character>decoder = new HashMap<>();
        // char alpha = 'a';
        // StringBuilder output = new StringBuilder();
        
        // for(int i=0; i<key.length();i++) {
        //     if(decoder.containsKey(key.charAt(i))==false && key.charAt(i) != ' ') {
        //         decoder.put(key.charAt(i), alpha++);
        //     }
        // }

        // for(int i=0; i<message.length(); i++) {
        //     if(decoder.containsKey(message.charAt(i)))
        //         output.append(decoder.get(message.charAt(i)));
        //     else
        //         output.append(' ');
        // }

        // return output.toString();

        // Approach 2 Without Using Hashing
        ArrayList<Character> decoder = new ArrayList<Character>();
	    StringBuilder output = new StringBuilder();
	    
	    for(int i=0;i<key.length();i++) {
	        if(key.charAt(i) != ' ' && decoder.indexOf(key.charAt(i)) == -1)
	            decoder.add(key.charAt(i));
	    }
	    
	    for (int i=0; i<message.length(); i++) {
	        if(message.charAt(i) == ' ')
	            output.append(' ');
	        else
	            output.append((char)(decoder.indexOf(message.charAt(i))+97));
	    }
	    
        return output.toString();
        
    }
}