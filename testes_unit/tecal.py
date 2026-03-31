import sys

sys.path.append('/storage/emulated/0')

from cal import *

def test_soma():
    for n in range(0, 10000):
        assert soma(n, 1) == n + 1
        print(soma(n, 1))
    
test_soma()