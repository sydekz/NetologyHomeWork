import datetime
import hashlib

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

@function_log_file('funclog3.txt')
def md5_hash_gen(filepath):
    with open(filepath) as f:
        for line in f:
            st_f = line.strip()
            yield hashlib.md5(st_f.encode()).hexdigest()

if __name__ == '__main__':
    for i in md5_hash_gen('a.txt'):
        print(i)

