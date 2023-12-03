class Solution(object):
    def toTime(self, from_point, to_point):
        x_diff = abs(from_point[0] - to_point[0])
        y_diff = abs(from_point[1] - to_point[1])

        return max(x_diff, y_diff)

    def minTimeToVisitAllPoints(self, points):
        time = 0

        for i in range(1, len(points)):
            time += self.toTime(points[i - 1], points[i])

        return time
        