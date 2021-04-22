# Cavishape
The pinnacle of our ohnonesness. Do you like petrichor?

(относительно) простой скрипт, работающий с программами LeadFinder (v.2012 b.1) и BuildModel (v.2004 b.1), позволяющий запускать множественные докинги и обеспечивающий удобный ввод и вывод значений

 # Установка
  1.Для работы скрипта нам требуется версия Python 3.0.0 и выше. Скачайте все файлы и положите их в одну папку, откройте консоль и пропишите следующие команды:
 
 ```cd C:\%тут идет путь к вашей папке%```
 
 ```python notsomain.py```
 
2. Создайте пустую папку в удобном вам месте и скопируйте путь к ней (в дальнейшем будем называть эту папку Repo). Пропишите команды из пункта 1 => выберите ключ ```2``` => выберите ключ ```dirPath``` => введите ваш путь к нужной папке.

3. Пропишите команды из пункта 1 => выберите ключ ```3```

Установка завершена,программа готова  к использованию

# Команды
 Докинг. Ключ - ```0```
 
```Ввод белка для докинга:``` сюда вводится ваша исходная структура,загруженная вами с PDB

```Ввод лиганда для докинга:``` сюда вводится дополнительный лиганд если вы хотите испоьзовать не тот что встроен в структуру. Храните ваши лиганды в папке ```%путь к Repo%\input\ligands```.Если вы хотите использовать встроенный в структуру лиганд то вводите ```ligandSelm.mol```. НЕ НАЗЫВАЙТЕ НИ ОДИН ИЗ ЛИГАНДОВ В ПАПКЕ ```ligands``` КАК ```ligandSelf.mol```

```Ввод внеструктурного референса``` сюда вводится дополнительный референсный лиганд если вы не хотите использовать тот что будет извлечен из структуры. Храните ваши референсы в папке ```%путь к Repo%\input\references```.Если вы хотите использовать референс извлекаемый из структуры то вводите ```reference.pdb```. НЕ НАЗЫВАЙТЕ НИ ОДИН ИЗ РЕФЕРЕНСОВ В ПАПКЕ ```references``` КАК ```reference.pdb```

```Ввод обработанного белка``` сюда вводится обработанная структура белка если вы не хотите использовать тот что будет извлечен из структуры (как правило нужно если BuildModel ломает структуру белка) . Храните ваши белки в папке ```%путь к Repo%\input\proteins```.Если вы хотите использовать белок извлекаемый из структуры то вводите ```protein.pdb```. НЕ НАЗЫВАЙТЕ НИ ОДИН ИЗ РЕФЕРЕНСОВ В ПАПКЕ ```proteins``` КАК ```protein.pdb```

```Ввод колеблющейся воды``` сюда вводятся номера воды для построения альтернативных сеток. Если вам не нужны альтернативные сетки то просто введите ```water```

```Введите настройки``` сюда вводятся имя файла содержащего особые настройки для BuildModel. Вы можете хранить разные файлы с настройками в папке ```%путь к Repo%\input\settings```. Если вам не требуются особые настройки, создайте пустой файл ```%рандомное имя%.txt``` в папке ```%путь к Repo%\input\settings``` и вводите 
 ```%рандомное имя%.txt```
 
 ```Кол во докингов``` сюда вводится кол-во докингов которое вам нужно


