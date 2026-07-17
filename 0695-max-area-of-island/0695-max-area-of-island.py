class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        visited=[]
        for i in range(row):
            visited.append([0]*col)
        count=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and visited[i][j]==0:
                    count=max(count,self.bfs(grid,visited,i,j))
        return count
    def bfs(self,grid,visited,i,j):
        row=len(grid)
        col=len(grid[0])
        q=deque()
        q.append((i,j))
        visited[i][j]=1
        count=0
        while q:
            count+=1
            i,j=q.popleft()
            if i-1>=0 and grid[i-1][j]==1 and visited[i-1][j]==0:
                q.append((i-1,j))
                visited[i-1][j]=1
            if i+1<row and grid[i+1][j]==1 and visited[i+1][j]==0:
                q.append((i+1,j))
                visited[i+1][j]=1
            if j-1>=0 and grid[i][j-1]==1 and visited[i][j-1]==0:
                q.append((i,j-1))
                visited[i][j-1]=1
            if j+1<col and grid[i][j+1]==1 and visited[i][j+1]==0:
                q.append((i,j+1))
                visited[i][j+1]=1
        return count

        