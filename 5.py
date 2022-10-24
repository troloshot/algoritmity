# Cказано, что s - валидная строка => закрывающая скобка на первом месте встречаться не будет, могу не проверять на это
# Решать буду через стек, нужно считать открывающие скобки в моменте.
# Сложность O(N) т.к. просто перебор элементов

def removeOuterParentheses(s):
    stack = []                          # создаю стек
    true = ""                           # ответ - строка
    score = 0                           # счетчик для скобок(нужно закрыть)

    for i in s:                         # прохожусь по строке
        if i == "(":                    # если скобка открывающая
            stack.append(i)             # добавляю ее в стек
            score += 1                  # счетчик +1
            if score > 1:               # если счетчик больше 1 => есть незакрытая скобка
                true += "("             # добавляем ее в стек

        if i == ")":                    # если скобка закрывающаяся
            stack.pop(-1)               # из стека ее удаляю
            score -= 1                  # счетчик -1 т.к. нашли закрывающую скобку
            if score > 0:               # если счетчик больше одного
                true += ")"             # в ответ добавляем закрывающую скобку

    return true                         # ответ


print(removeOuterParentheses('(()())(())'))
print(removeOuterParentheses('(()())(())(()(()))'))
print(removeOuterParentheses('()()'))