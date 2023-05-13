class Solution {
    public boolean halvesAreAlike(String s) {
		// Set VOWELS = Set.of('a','e','i','o','u','A','E','I','O','U');
		// int left = 0, right = s.length()-1;
		// int lCount = 0, rCount = 0;
		// while(left<right){
		//     lCount += VOWELS.contains(s.charAt(left)) ? 1 : 0;
		//     rCount += VOWELS.contains(s.charAt(right)) ? 1 : 0;
		//     left++;
		//     right--;
		// }
		// return lCount==rCount;
        
        Set VOWELS = Set.of('a','e','i','o','u','A','E','I','O','U');
		int lCount = 0, rCount = 0;
		for(int i=0;i<s.length()/2;i++){
		  lCount += VOWELS.contains(s.charAt(i)) ? 1 : 0;
		  rCount += VOWELS.contains(s.charAt(i+s.length()/2)) ? 1 : 0;
		}
		return lCount==rCount;
    }
}