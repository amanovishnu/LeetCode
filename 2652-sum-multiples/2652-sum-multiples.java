class Solution {
    public int sumOfMultiples(int n) {
        int res = 0;
        for(int i=0; i<=n;i++)
            if(i%3==0||i%5==0||i%7==0)
                res+=i;
        return res;
    }
}

// Time Complexity: O(n)
// Space Complexity: O(1)