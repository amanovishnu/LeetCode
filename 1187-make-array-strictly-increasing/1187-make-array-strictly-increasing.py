class Solution(object):
    def makeArrayIncreasing(self, arr1, arr2):
        arr2 = sorted(arr2)
        dict_pre = {0: -float("inf")}	
        for num in arr1:
            dict_cur = collections.defaultdict(lambda: float("inf"))
            for n_swap in dict_pre:
                if num > dict_pre[n_swap]:
                    dict_cur[n_swap] = min(dict_cur[n_swap], num)
                loc = bisect.bisect(arr2, dict_pre[n_swap])
                if loc < len(arr2):
                    dict_cur[n_swap+1] = min(dict_cur[n_swap+1], arr2[loc])
                    
            if not dict_cur:
                return -1
            dict_pre = dict_cur
            
        return min(dict_pre.keys())