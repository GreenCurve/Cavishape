import os
import subprocess
import csv
import shutil
import operator
from main import *

option = int(input('Выберите ключ для операции из предложенного списка' + '\n' + '0 - Докинг' + '\n' + '1 - экстракция '))
if option == 0:
    protein = input('Ввод белка для докинга: ')
    ligand = input('Ввод лиганда для докинга: ')
    water = input('Ввод колеблющейся воды: ')
    settings = input("Введите настройки: ")
    dockingRepeats = input('Кол во докингов: ')
    if protein == '':
        protein = '1dwb.pdb'
    if ligand == '':
        ligand = 'ligandSelf.mol'
    if settings == '':
        settings = 'settings.txt'
    if dockingRepeats == '':
        dockingRepeats = int(2)
    dockingRepeats = int(dockingRepeats)
    Operation.Docking(protein, ligand, water, settings, dockingRepeats)
elif option == 1:
    protein = input('Ввод белка для докинга: ')
    settings = input("Введите настройки: ")
    if protein == '':
        protein = '1dwb.pdb'
    if settings == '':
        settings = 'settings.txt'
    Operation.Extracting(protein, settings)
