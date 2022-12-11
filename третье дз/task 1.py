class Solution:
    def isPalindrome(self, head: ListNode):
        arr = []
        cur = head
        while cur:  # пока есть значения в cur будет выполняться ->
            arr.append(cur.val)   # добавляем в пустой список значения head или cur кому как удобней
            cur = cur.next  # идем дальше по cur которое равно head
        return arr == arr[::-1]  # делаем проверку на палиндром