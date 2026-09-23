class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        curr_color = image[sr][sc]
        if curr_color == color:
            return image

        ROWS = len(image)
        COLS = len(image[0])

        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or image[row][col] != curr_color:
                return
            
            image[row][col] = color
            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row - 1, col)
            dfs(row, col - 1)

        dfs(sr, sc)
        return image
        