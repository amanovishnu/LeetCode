import java.util.*;
import java.io.*;

class Solution {
    
    public static ArrayList splitNumber(int number) {
        ArrayList<Integer> digits = new ArrayList<Integer>();
        while(number != 0) {
            digits.add(number%10);
            number /= 10;
        }
        Collections.reverse(digits);
        return digits;
    }
    
    public int[] separateDigits(int[] nums) {
	    ArrayList<Integer> output = new ArrayList<Integer>();
		for(int i=0; i<nums.length; i++) {
		    output.addAll(splitNumber(nums[i]));
		}
        
        int[] finalArray = new int[output.size()];
        int idx = 0;
        for(Integer I : output)
        {
            finalArray[idx++] = (int)I;
        }
        return finalArray;
    }
}