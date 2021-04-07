import os
import subprocess
import csv
import shutil

import operator
from main import Operation

protein = input('Ввод белка для докинга: ')
ligand = input('Ввод лиганда для докинга: ')
water = input('Ввод колеблющейся воды: ')
settings = input("Введите настройки: ")
dockingRepeats = int(input('Кол во докингов: '))

Operation.Docking(protein, ligand, water, settings, dockingRepeats)