class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        max_stop = max(max(route) for route in routes)
        if max_stop < target:
            return -1

        n = len(routes)
        min_buses_to_reach = [float('inf')] * (max_stop + 1)
        min_buses_to_reach[source] = 0

        flag = True
        while flag:
            flag = False
            for route in routes:
                mini = float('inf')
                for stop in route:
                    mini = min(mini, min_buses_to_reach[stop])
                mini += 1
                for stop in route:
                    if min_buses_to_reach[stop] > mini:
                        min_buses_to_reach[stop] = mini
                        flag = True

        return min_buses_to_reach[target] if min_buses_to_reach[target] < float('inf') else -1