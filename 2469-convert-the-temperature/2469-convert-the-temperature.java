class Solution {
    public double[] convertTemperature(double celsius) {
        return new double[]{celsius+273.15, celsius*1.80+32.00};
    }
}
// Time Complexity = O(1)
// Space Complexity = O(1)