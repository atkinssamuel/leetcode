# First pass solution: 608ms 31.56%
class Solution(object):

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    checks = [[i - 1, j],  # North
                              [i, j + 1],  # East
                              [i + 1, j],  # South
                              [i, j - 1]]  # West
                    for dir_check in checks:
                        if dir_check[0] < 0 or dir_check[0] >= len(grid) or dir_check[1] < 0 or dir_check[1] >= len(
                                grid[0]):
                            continue
                        else:
                            if grid[dir_check[0]][dir_check[1]] == 1:
                                perimeter -= 1
                    perimeter += 4

        return perimeter
