__author__ = 'ugunipati'

import threading

def example():
    for i in range(1,100):
        print i*i
    return


if __name__=='__main__':
    for i in range(3):
        t = threading.Thread(target=example())
        t.start()