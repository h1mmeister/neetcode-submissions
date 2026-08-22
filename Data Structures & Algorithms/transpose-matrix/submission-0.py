import numpy as np

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        matrix_np = np.array(matrix)
        return list(matrix_np.T)
        