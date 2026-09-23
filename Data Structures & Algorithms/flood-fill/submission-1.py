class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image 

        def dfs(image, row, col, new_color, curr_color):
            if row < 0 or col < 0 or row >= len(image) or col >= len(image[0]) or image[row][col] != curr_color:
                return

            image[row][col] = new_color
            dfs(image, row + 1, col, new_color, curr_color)
            dfs(image, row, col + 1, new_color, curr_color)
            dfs(image, row - 1, col, new_color, curr_color)
            dfs(image, row, col - 1, new_color, curr_color)

        dfs(image, sr, sc, color, image[sr][sc])

        return image

    
        