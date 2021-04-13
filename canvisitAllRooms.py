class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = [False] * len(rooms)
        self.dfs(0,rooms,visited)
        return all(visited)
        
    
    def dfs(self,r, rooms,visited):
        visited[r] = True
        for i in rooms[r]:
            if not visited[i]:
                self.dfs(i,rooms,visited)