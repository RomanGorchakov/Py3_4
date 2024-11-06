#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math, abc

class Number(abc.ABC):
    
    @abc.abstractmethod

    def add(self, n):
        pass

    def dis(self, n):
        pass
    
    def mult(self, n):
        pass
    
    def depl(self, n):
        pass
    
    def pow(self, n):
        pass

class Integer(Number):
    def __init__(self, num):
        self._num = int(num)
    
    def add(self, n):
        return self._num + n

    def dis(self, n):
        return self._num - n
    
    def mult(self, n):
        return self._num * n
    
    def depl(self, n):
        return self._num / n
    
    def pow(self, n):
        return self._num ** n

class Real(Number):
    def __init__(self, num):
        self._num = float(num)
    
    def add(self, n):
        return self._num + n

    def dis(self, n):
        return self._num - n
    
    def mult(self, n):
        return self._num * n
    
    def depl(self, n):
        return self._num / n
    
    def pow(self, n):
        return self._num ** n

if __name__ == "__main__":
    p1 = Integer(50)
    print(p1.add(4))

    p2 = Real(43.5)
    print(p2.pow(2))