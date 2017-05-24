#!/usr/bin/env python3
#coding=utf-8

import py_ext_t

def fun():
    ret, str = py_ext_t.fun_param_0()
    print(ret, str)
    
    ret, str = py_ext_t.fun_param_1(11)
    print(ret, str)
    ret, str = py_ext_t.fun_param_1(-5)
    print(ret, str)

    ret, str = py_ext_t.fun_param_2(34, b"abcde324234531342345345abcd")
    print(ret, str)



if __name__ == "__main__":
    '''
    unit test:
         python.exe -m doctest main.py -v
    '''

#     import doctest
#     doctest.testmod()
    
    fun()
    
    








