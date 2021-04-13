class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = {}
        
        for i,t in enumerate(points):
            
            dist[i] = t[0]*t[0] + t[1]*t[1]
        
        dist = sorted(dist.items(), key=lambda item: item[1])
        
        return [points[dist[i][0]] for i in range(k)]