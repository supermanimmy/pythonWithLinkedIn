'''
Module practise
'''
import sys
import os
import random

def main():
    v = sys.version_info
    p = sys.platform
    os_name = os.urandom(24).hex() # getcwd(), get
    print('Python version {}.{}.{}'.format(*v))
    print(p)
    print(os_name)

    p = random.randint(10,100)
    print(f'random number: {p}')

if __name__ == '__main__': main()