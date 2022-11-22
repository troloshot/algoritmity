"""Cоздаем матрицу такой же размерности как и obstacleGrid.
    Каждая ячейка dp[m][n] это кол-во путей до этой ячейки.
    """
def uniquePathsWithObstacles(obstacleGrid):
    if obstacleGrid[0][0]:
        return 0
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if m == 0 and n == 0:  # эта ячейка заполнена, ее пропускаем
                continue
            if obstacleGrid[m][n] == 1:  # если в ячейкм препятствие, в нее не идем
                dp[m][n] = 0
            else:
                if m == 0:  # если передвигаемся по первой строке, ячеек всерху еще не было
                    dp[m][n] = dp[m][n - 1]
                elif n == 0:  # если передвигаемся по первому столбцу, ячеек слева еще не было
                    dp[m][n] = dp[m - 1][n]
                else:
                    dp[m][n] = dp[m - 1][n] + dp[m][n - 1]
        return dp[-1][-1]  # возвращаем значение финишной ячейки с кол-вом путей до нее
