class Solution {
    public double average(int[] salary) {
        int min_sal = Integer.MAX_VALUE, max_sal = Integer.MIN_VALUE, counter = 0;
		double sum = 0;
		for(int sal : salary){
		    min_sal = Math.min(min_sal, sal);
		    max_sal = Math.max(max_sal, sal);
		    sum += sal;
		    counter++;
		}
		return (sum-min_sal-max_sal)/(counter-2);   
    }
}