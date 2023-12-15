class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        if len(paths) == 1:
            return paths[0][1]
        else:
            source = set([path[0] for path in paths])
            destination = set([path[1] for path in paths])
            return ''.join(destination.difference(source))