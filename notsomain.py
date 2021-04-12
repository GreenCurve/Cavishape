import os
import subprocess
import csv
import shutil
import operator
from main import *

option = int(input("Выберите ключ для операции из предложенного списка" + "\n" + "0 - Докинг" + "\n" + "1 - экстракция " + "\n" + "2 - шоткаты "))
if option == 0:
    protein = input("Ввод белка для докинга: ")
    ligand = input("Ввод лиганда для докинга: ")
    water = input("Ввод колеблющейся воды: ")
    settings = input("Введите настройки: ")
    dockingRepeats = input("Кол во докингов: ")
    if protein == "":
        protein = str(Operation.Bmg("protein"))
    if ligand == "":
        ligand = str(Operation.Bmg("ligand"))
    if settings == "":
        settings = str(Operation.Bmg("settings"))
    if water == "":
        water = str(Operation.Bmg("water"))
    if dockingRepeats == "":
        dockingRepeats = int(Operation.Bmg("dockingRepeats"))
    dockingRepeats = int(dockingRepeats)
    Operation.Docking(protein, ligand, water, settings, dockingRepeats)
elif option == 1:
    protein = input("Ввод белка для докинга: ")
    settings = input("Введите настройки: ")
    if protein == "":
        protein = str(Operation.Bmg("protein"))
    if settings == "":
        settings = str(Operation.Bmg("settings"))
    Operation.Extracting(protein, settings)
elif option == 2:
    key = input("Введите ключ из предложенного списка " + str(Operation.lsr("config.json")) + " ")
    value = input("Текующее значение - " + str(Operation.Bmg(key)) + " " + str(type(Operation.Bmg(key))) + '\n' + "Введите новое значение (Если текущее значение вас устраивает,напишите Феликсу) ")
    if value == "Феликсу":
        pass
    else:
        Operation.Sets(key,value)
