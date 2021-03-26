import datetime

def function_log_file(filename):
    def function_log(foo):

        def new_foo(*args, **kwargs):
            dt_now = datetime.datetime.now()
            result = foo(*args, **kwargs)
            func_str = f'Дата и время - {dt_now} - имя - {foo.__name__} - аргументы {args} результат {result}\n'
            with open(filename, "a", encoding="utf-8") as f:
                f.write(func_str)
            return result
        return new_foo
    return function_log

@function_log_file('funclog2.txt')
def foo2(a, b, c, d, e):
    return a*b*c*d - 1 - e

if __name__ == '__main__':
    foo2(1, 2, 3, 4, 4)