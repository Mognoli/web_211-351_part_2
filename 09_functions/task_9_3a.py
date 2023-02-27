# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    file = open(config_filename)
    k=''
    v='' 
    mode=''
    access_res={}
    trunk_res={}
    for line in file:
        chek=False
        if 'interface' in line:
            k=line.split()[-1]
            v=1
            mode=''
        elif 'vlan' in line:
            mode=line.split()[1]
            if mode=='trunk':
                v='['+line.split()[-1]+']'
            else:
                v=line.split()[-1]
            chek=True
        elif 'mode' in line and mode=='':
            mode=line.split()[-1]
            chek=True
        if chek and mode=='access':
            access_res[k]=v
        elif chek and mode=='trunk':
            trunk_res[k]=v
    return (access_res, trunk_res)

print(get_int_vlan_map('config_sw2.txt'))