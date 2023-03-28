# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    file = open(config_filename).read()
    k=''
    v='' 
    mode=''
    access_res={}
    trunk_res={}
    for line in file:
        chek=False
        if 'interface' in line:
            k=line.split()[-1]
        elif 'vlan' in line:
            mode=line.split()[1]
            if mode=='trunk':
                v='['+line.split()[-1]+']'
            else:
                v=line.split()[-1]
            chek=True
        if chek and mode=='access':
            access_res[k]=v
        elif chek and mode=='trunk':
            trunk_res[k]=v
    return (access_res, trunk_res)

print(get_int_vlan_map('config_sw1.txt'))