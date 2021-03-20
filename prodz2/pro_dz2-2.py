import hashlib

def md5_hash_gen(filepath):
    with open(filepath) as f:
        for line in f:
            st_f = line.strip()
            yield hashlib.md5(st_f.encode()).hexdigest()

if __name__ == '__main__':
    for i in md5_hash_gen('a.txt'):
        print(i)