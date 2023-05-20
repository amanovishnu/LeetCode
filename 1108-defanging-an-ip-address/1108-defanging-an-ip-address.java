class Solution { 
    public String defangIPaddr(String address) {
        // Approach #1
	    if(address.length() == 0)
	       return address;
		StringBuilder sb = new StringBuilder();
		for(int i=0; i<address.length();i++)
		    sb.append(address.charAt(i) == '.' ? "[.]" : address.charAt(i));
		return sb.toString();
        
        // Approach #2
        // return address.replace(".", "[.]");
        
    }
}

// Time Complexity : O(n) 
// Space Complexity : O(n)