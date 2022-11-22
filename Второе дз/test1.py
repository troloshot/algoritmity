"""Сложность: O(mn)"""


def countSquares(matrix):
    """Создаем список такой же размерности, как и матрица.
        Каждая ячейка dp[m][n] - это кол-во единичных матриц, чей правый нижний угол совпадает с этой ячейкой.
    """
    dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    res = 0 # переменная считает конечное кол-во матриц
    for i in range(len(matrix)): # проходимся по матрице
        for j in range(len(matrix[0])):
            if i == 0 or j == 0: # заполняем первую строку и столбец такими же значениями как в матрице
                dp[i][j] = matrix[i][j]
                if dp[i][j] == 1:
                    res += 1
            else:
                if matrix[i][j]: # если в данной ячейке стоит 1
                    """Кол-во матриц, правая нижняя ячейка которых находится в dp[m][n], вычисляется так:
                        Минимальное значение из правой ячейки, верхней ячейки и ячейки dp[m - 1][n - 1] плюс 1.
                    """
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    res += dp[i][j] # прибавляем полученное значение к результату
    return res
