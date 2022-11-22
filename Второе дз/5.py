"""создаем массив в котором будем хранить ежедневую цену акции после чего необходимо определить
сколько перепадов цен будут являтся плавными то бишь i-1. Сложность O(n)"""
class Solution(object):
    def getDescentPeriods(self, prices):
        smooth_descent = [1] * len(prices)  # создали массив
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:  # сравниваем
                smooth_descent[i] += smooth_descent[i - 1]      # считаем количество мягких спадов
        return sum(smooth_descent)