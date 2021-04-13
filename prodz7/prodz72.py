from prodz71 import LIFO

SEQUENCES = ['(((([{}]))))',
             '[([])((([[[]]])))]{()}',
             '{{[()]}}',
             '}{}',
             '{{[(])]}}',
             '[[{())}]']


#Возвращает True если последовательность сбалансирована, а иначе False
def check_sequence(sequence):
    lifo_queue = LIFO()
    for i in sequence:
        if i == '(' or i == '{' or i == '[':
            lifo_queue.push(i)
        elif lifo_queue.isEmpty():
            return False

        if i == ')':
            if lifo_queue.peek() == '(':
                lifo_queue.pop()
            else:
                return False

        if i == '}':
            if lifo_queue.peek() == '{':
                lifo_queue.pop()
            else:
                return False

        if i == ']':
            if lifo_queue.peek() == '[':
                lifo_queue.pop()
            else:
                return False

    if lifo_queue.isEmpty():
        return True
    else:
        return False


if __name__ == '__main__':
    for sequence in SEQUENCES:
        print(f'Последовательность {sequence} {"сбалансирована" if check_sequence(sequence) else "не сбалансирована"}')
