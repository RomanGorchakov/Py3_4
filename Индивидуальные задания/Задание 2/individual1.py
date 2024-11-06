#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Pair():
    def __init__(self, first, second):
        self._first = 0
        self._second = 0
    
    def p(self):
        first = int(input("Введите первое число пары: "))
        self._first = first
        second = int(input("Введите второе число пары: "))
        self._second = second
    
    def compare(self):
        if (p1._first > p2._first) or ((p1._first == p2._first) and (p1._second > p2._second)):
            return "Первая пара больше второй"
        else:
            return "Вторая пара больше первой"
    
class Fraction(Pair):
    def __init__(self, first, second):
        super().__init__(self, first)
        self._full_first = int(first // 1)
        self._frac_first = round((first % 1), 2)
        self._full_second = int(second // 1)
        self._frac_second = round((second % 1), 2)
    
    def change_grade(self):
        new_grade = input("Новый год обучения: ")
        self.grade = new_grade
    
    def add_grade(self, plus):
        self.grade += plus
        self.age += plus

if __name__ == "__main__":
    p1 = Pair(20, 50)
    p2 = Pair(40, 30)
    print(p1.compare())

    p3 = Fraction(20.6, 50.1)
    p4 = Fraction(40.3, 30.4)
    print(p3._frac_second)