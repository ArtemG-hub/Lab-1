import time            #вводим модуль time для задач со временем
import os              # Модуль для взаимодействия с операционной системой (очистка экрана)
RED = '\u001b[41m'     #для фона и пикселей 
WHITE = '\u001b[47m'
RESET = '\u001b[0m'
BLUE =  '\u001b[44m'


def flag():                           #для флага швейцарии через умножение
    pixel = '    '                    #символ пробела для цветного фона
    b=2                               #вспомогательная переменная
    length = 13*b  
    height = length                   #длина и высота флага
    for y in range (height//5):       #ширина верхней части флага и ее состав
        print (RED + pixel * (b*7+1) + RESET)
    for t in range (height//5):       #ширина второй части флага (с началом креста) и ее состав
        print (RED + pixel * (b*3) + WHITE + pixel * (b+1) + RED + pixel * (b*3) + RESET)
    for j in range (height//5):       #ширина третьей части флага (центральной) и ее состав
        print (RED + pixel * (b) + WHITE + pixel * (b*5+1) + RED + pixel * (b) + RESET)
    for k in range (height//5):       #ширина предпослед. части флага и ее состав
        print (RED + pixel * (b*3) + WHITE + pixel * (b+1) + RED + pixel * (b*3) + RESET)
    for m in range (height//5):       #ширина последней части флага (красной) и ее состав
        print (RED + pixel * (b*7+1)+ RESET)


def model():
    pixel = "\033[44m  \033[0m"       # Объявляем синий пиксель: пробел на синем фоне (\033[44m) + сброс цвета (\033[0m)
    pixell = "\033[44m \033[0m"        
    str1 = f"    {pixel}{pixell}{pixel}        {pixel}{pixell}{pixel}     "   # сам узор
    str2 = f"  {pixel}     {pixel}    {pixel}     {pixel}  " 
    str3 = f"{pixel}         {pixel}{pixel}         {pixel}"
    str4 = f"  {pixel}     {pixel}    {pixel}     {pixel}  "
    str5 = f"    {pixel}{pixell}{pixel}        {pixel}{pixell}{pixel}     "
    str6 = f"                       "

    for i in range (2):      # Выводим готовый узор в терминал
        print (str1 )
        time.sleep(0.5)
        print (str2 )
        time.sleep(0.5)
        print (str3)
        time.sleep (0.5)
        print (str4 )
        time.sleep(0.5)
        print (str5 )
        time.sleep(0.5)
        print (str6 )
        time.sleep(0.5)


def animation():                                     #для создания анимации загрузки от 1% до 100%
    for i in range(1, 101):          
        os.system('cls' if os.name == 'nt' else 'clear')              #для очистки консоли (чтобы писало на прошлом месте) на разных операционных системах - первое для windows, второе - macOS/linux
        print(BLUE + "Ожидайте, " + f' загрузка {i*1} % ' + RESET)    #вывод процента загрузки на синем фоне, f' чтобы можно было вставлять переменную напрямую, через {}
        time.sleep(0.05)                             #ждем 0.05 сек между сменой процентов
        print (RESET)                                #сбрасываем цвет фона, можно без этой команды, но так работает быстрее
    print('\x1b[H', end='Загрузка завершена')        #после загрузки до 100% выводим на экран "Загрузка завершена"
    os.system('cls' if os.name == 'nt' else 'clear') #очищаем консоль


def sequence():                         #для создания диаграммы 
    file = open ('sequence.txt', 'r')   #открываем файл для чтения (за чтение отвечает 'r')
    odds = []                           #для списка чисел в диапазоне от -3 до 3 включая обе границы
    evens = []                          #для списка остальных чисел
    for line in file:                   #преобразуем строку в число с плавающей точкой, затем в целое
        if -3 <= int(float(line)) <= 3: #проверяем, входит ли число в диапазон [-3; 3]
            odds.append(float(line))    #для преобразования прочитанных данных в числа и добавление их в список (в конец), иначе в другой список
        else:
            evens.append(float(line))
    file.close()                        #закрываем файл
    print(f'{BLUE}{' ' * int(len(odds) / 5)}{RESET}{len(odds)/(len(odds) + len(evens)) * 100}%')   # Вывод синей полосы-графика для первой группы чисел и её доли в %
    print(f'{RED}{' ' * int(len(evens) / 5)}{RESET}{len(evens)/(len(odds) + len(evens)) * 100}%')  # Вывод красной полосы-графика для второй группы чисел и её доли в %


def function():
    for y in range(10, 0, -1):                     # цикл идет от 10 до 1 включительно, шаг -1
        line = ""                                  # создаем пустую строку для текущего ряда графика, чтобы выводилось не подряд в столбец         
        for x in range(1, 32):                     # цикл идет по оси X от 1 до 31 включительно
            if round(x / 3) == y:         
                line = line + RED + " " + RESET    # если округленное деление х на 3 равно текущему у, рисуем график
            else:
                line = line + " "                  # иначе ставим пробел

        print(f"\033[34m{str(y).ljust(2)} |\033[0m{line}")  # печатаем номер строки Y и вертикальную ось "|", str преобразует число в текст, чтобы вывелось без ошибок
    print("\033[34m   +" + "-"*32 + "\033[0m")     # печатаем нижнюю границу графика (ось X) из 32 дефисов
    numbers = ""                                   # создаем пустую строку для чисел-подписей оси X 
    for x in range(0, 29, 3):                      # по х от 0 до 29 с шагом 3 
        numbers = numbers + str(x).ljust(3)        # превращаем число в строку и дополняем пробелами до ширины в 3 символа, чтобы числа 0, 3, 12, 24... стояли ровно друг за другом
    print("  \033[34m" + numbers + "\033[0m")      # печатаем строку с числами под графиком с отступом в 2 пробела


flag()
print()
model()
print
animation()
print()
sequence()
print()
function()