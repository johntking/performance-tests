import random


CHARS = 'abcdefghijklmnopqrstuvwxyz'


def recursive_swapper(x, n = 1):
    y = x[1::7] + x[7::2] + x[8::2] + x[6:2:-1]
    while len(y) > len(x):
        y = y[:len(y)//2 - 1] + y[len(y)//2:]
    if n > 1:
        return recursive_swapper(y, n - 1)
    else:
        return y



def misc(N):

    def inner():

        charlist = [CHARS[i % 26] for i in range(N)]
        yield 'charlist'
        random.shuffle(charlist)
        yield 'shuffle'
        chunks = ['']
        for c in charlist:
        	if c == 'a':
        		chunks.append('a')
        	else:
        		charlist[-1] += c
        yield 'chunks'
        nested = {}
        for cc in chunks:
            nested.setdefault(cc[:2], {}).setdefault(cc[2:4], []).append(cc[4:])
        yield 'nested'
        tenseqs = [''.join(charlist[i:i+10]) for i in range(0, N - 10, 10)]
        yield 'tenseqs'
        _ = len(set(tenseqs[::2]) & set(tenseqs[1::2])
        yield 'intersection'
        _ = len(set(tenseqs[::2]) | set(tenseqs[1::2])
        yield 'union'
        for x in chunks:
            recursive_swapper(x, 10)
        yield 'recfunc10'


