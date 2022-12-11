#Сложность - O(n)
class Solution(object):
    def hasCycle(self, head):
        if head == None: #оптимизация
            return False
        indicator1 = indicator2 = head # создаем два идикатора один из которых ходит на 1 шаг вперед а второй на 2

        while True:
            if indicator1.next != None:
                indicator1 = indicator1.next # это первый индикатор
            else:
                break

            if indicator2.next != None and indicator2.next.next != None:
                indicator2 = indicator2.next.next # второй индикатор
            else:
                break

            if indicator1 == indicator2: # если индикаторы в какой то момент смогли встретиться то выводим тру если нет фолс
                return True

        return False