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
    
    ret, str = py_ext_t.fun_param_str(34, r"abcde3d大健康24234531342345345abcd")
    print(ret, str.decode('utf8'))
    



if __name__ == "__main__":
    '''
    unit test:
         python.exe -m doctest main.py -v
    '''

#     import doctest
#     doctest.testmod()
    
    fun()
    
    








