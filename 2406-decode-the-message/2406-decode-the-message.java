class Solution {
    public String decodeMessage(String key, String message) {
        HashMap<Character, Character>decoder = new HashMap<>();
        char alpha = 'a';
        StringBuilder output = new StringBuilder();
        
        for(int i=0; i<key.length();i++) {
            if(decoder.containsKey(key.charAt(i))==false && key.charAt(i) != ' ') {
                decoder.put(key.charAt(i), alpha++);
            }
        }

        for(int i=0; i<message.length(); i++) {
            if(decoder.containsKey(message.charAt(i)))
                output.append(decoder.get(message.charAt(i)));
            else
                output.append(' ');
        }

        return output.toString();
        
    }
}