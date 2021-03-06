from time import time

def timer(func):
    def wrapper(*args):
        t1 = time()
        result = func(*args)
        t2 = time()
        print(f'{func.__name__} took {t2 - t1} seconds')
        return result
    return wrapper


def __read_stopwords(name):
    f = open(name)
    content = f.read()
    r = content.split('\n')
    return r


verbal = __read_stopwords('./ir/verbal')

nonverbal = __read_stopwords('./ir/nonverbal')
