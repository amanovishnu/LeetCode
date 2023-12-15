class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        if len(paths) == 1:
            return paths[0][1]
        else:
            transposed_paths = zip(*paths)
            source_list, destination_list = map(set, transposed_paths)
            return destination_list.difference(source_list).pop()