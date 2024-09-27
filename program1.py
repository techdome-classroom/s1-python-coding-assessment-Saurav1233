from typing import List

class Solution:
    def getTotalIsles(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W' or visited[r][c]:
                return
            visited[r][c] = True
            
            dfs(r-1, c)  
            dfs(r+1, c)  
            dfs(r, c-1)  
            dfs(r, c+1)  

        island_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L' and not visited[r][c]:
                    
                    dfs(r, c)
                    island_count += 1

        return island_count


def get_user_input() -> List[List[str]]:
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    grid = []
    print("Enter the grid row by row (use 'L' for land and 'W' for water):")
    for i in range(rows):
        row = input(f"Row {i+1}: ").split()
        if len(row) != cols:
            raise ValueError("Each row must have the exact number of columns entered.")
        grid.append(row)
    
    return grid


if __name__ == "__main__":
    solution = Solution()
    grid = get_user_input()
    result = solution.getTotalIsles(grid)
    print(f"Number of distinct islands: {result}")

