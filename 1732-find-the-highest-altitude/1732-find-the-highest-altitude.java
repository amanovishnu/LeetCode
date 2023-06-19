class Solution {
    public int largestAltitude(int[] gain) {
        int current_altitude = 0, max_altitude = 0;
		for(int altitude : gain) {
		    current_altitude += altitude;
		    max_altitude = Math.max(current_altitude, max_altitude);
		}
	    return max_altitude;
    }
}