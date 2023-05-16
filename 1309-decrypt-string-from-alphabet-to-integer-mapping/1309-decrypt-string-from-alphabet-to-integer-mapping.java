class Solution {
    public String freqAlphabets(String s) {
        int l = s.length();
	    StringBuilder sb = new StringBuilder();
	    while(l>0) {
	        int temp;
	        if(s.charAt(l-1) == '#') {
	            temp = Integer.parseInt(s.substring(l-3,l-1))+96;
	            sb.append((char)temp);
	            l-=3;
	        } else {
	            temp = Character.getNumericValue(s.charAt(l-1))+96;
	            sb.append((char)temp);
	            l--;        
	        }
	    }
	    return sb.reverse().toString();
    }
}