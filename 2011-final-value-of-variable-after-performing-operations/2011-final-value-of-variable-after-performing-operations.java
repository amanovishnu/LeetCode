class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int x = 0;
        for(String op : operations)
            x+= op.charAt(1)=='+' ? 1 : -1;
        return x;
    }
}
// Time Complexity = O(n)
// Space Complexity = O(1)