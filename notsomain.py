import os
import subprocess
import csv
import shutil
import operator
from main import *

option = int(input("Выберите ключ для операции из предложенного списка" + "\n" + "0 - Докинг" + "\n" + "1 - экстракция " + "\n" + "2 - шоткаты " + '\n' + "3 - Инициализация папок " + '\n'))
if option == 0:
    structure = input("Ввод белка для докинга: ")
    ligand = input("Ввод лиганда для докинга: ")
    reference = input("Ввод внеструктурного референса")
    protein = input("Ввод обработанного белка")
    water = input("Ввод колеблющейся воды: ")
    settings = input("Введите настройки: ")
    dockingRepeats = input("Кол во докингов: ")
    if structure == "":
        structure = str(Operation.Bmg("structure"))
    if ligand == "":
        ligand = str(Operation.Bmg("ligand"))
    if reference == "":
        reference = str(Operation.Bmg("reference"))
    if protein == "":
        protein = str(Operation.Bmg("protein"))
    if water == "":
        water = str(Operation.Bmg("water"))
    if settings == "":
        settings = str(Operation.Bmg("settings"))
    if dockingRepeats == "":
        dockingRepeats = int(Operation.Bmg("dockingRepeats"))
    dockingRepeats = int(dockingRepeats)
    Operation.Docking(structure, ligand, reference, protein, water, settings, dockingRepeats)
elif option == 1:
    structure = input("Ввод белка для докинга: ")
    settings = input("Введите настройки: ")
    if structure == "":
        structure = str(Operation.Bmg("structure"))
    if settings == "":
        settings = str(Operation.Bmg("settings"))
    Operation.Extracting(structure, settings)
elif option == 2:
    key = input("Введите ключ из предложенного списка " + str(Operation.lsr("config.json")) + " ")
    value = input("Текующее значение - " + str(Operation.Bmg(key)) + " " + str(type(Operation.Bmg(key))) + '\n' + "Введите новое значение (Если текущее значение вас устраивает,напишите Феликсу) ")
    if value == "Феликсу":
        pass
    else:
        Operation.Sets(key,value)
elif option == 3:
    Operation.Initer(Operation.Bmg("dirPath"))
    print('Инициализировано!')

