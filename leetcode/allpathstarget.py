#797. All Paths From Source to Target

from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        self.allPathsSourceTargetSub(graph, 0, [], paths)
        return paths


    def allPathsSourceTargetSub(self, graph, visit, cur_path, paths):
        cur_path.append(visit)
        if visit == len(graph) - 1:
            paths.append(list(cur_path))
        else:
            adjs = graph[visit]
            for adj in adjs:
                self.allPathsSourceTargetSub(graph, adj, cur_path, paths)
        cur_path.pop()


s = Solution()

print(s.allPathsSourceTarget([[]]))
print(s.allPathsSourceTarget([[1,2],[3],[3],[]]))
print(s.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))