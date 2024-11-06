#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


class Soldiers():
    id_ = 1
    def __init__(self):      
        self.id_ = Soldiers.id_ 
        Soldiers.id_ += 1
 
    def go_hero(self, hero):
        print(f'Солдат с id {self.id_} следует за героем {hero.id_}.')
        
    def __str__(self):
        return f'{self.id_}'
    
class Heroes():
    id_ = 1
    def __init__(self, team):
        self.id_ = Heroes.id_
        Heroes.id_ += 1

        self.team = team
        self.level = 1

    def change_team(self):
        self.team = input("Укажите цвет героя: ")
        return self.team
 
    def level_up(self):
        self.level += 1
        print(f'Герой с id {self.id_} достиг {self.level} уровня.')


if __name__ == '__main__':
    hero_1 = Heroes('красный')
    hero_2 = Heroes('синий')

    list_1 = []
    list_2 = []
    for _ in range(50):
        if random.choice(['красный', 'синий']) == 'красный':
            list_1.append(Soldiers())
        elif random.choice(['красный', 'синий']) == 'синий':
            list_2.append(Soldiers())
    print(len(list_1), len(list_2))

    if len(list_1) > len(list_2):
        hero_1.level_up()
    else:
        hero_2.level_up()

    random.choice(list_1).go_hero(hero_2)

    hero_3 = Heroes('красный')
    hero_3.change_team()

    list_3 = []
    for _ in range(25):
        list_3.append(Soldiers())
    print(len(list_3))

    if (len(list_1) > len(list_2)) and (len(list_1) > len(list_3)):
        hero_1.level_up()
    elif (len(list_1) < len(list_2)) and (len(list_2) > len(list_3)):
        hero_2.level_up()
    else:
        hero_3.level_up()

    random.choice(list_3).go_hero(hero_1)