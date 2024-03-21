while True:
#выводит строку
    bits=input("Введите группу из 8 бит: ")
#условие если для завершения кода при пустой строке
    if bits=="":
        print("Пустая строка")
        break
#проверяется длина 
    if len(bits)!=8:
        print("Ошибка")
        continue
#подсчитывает сколько 1 и 0 в строке
    count_ones = bits.count('1')
    count_zero = bits.count('0')
count_jgfjfgluy
#проверка количества 1 и 0
    if count_ones + count_zero != 8:        
        print( "Ошибка: Последовательность должна состоять из 8 бит") 
        continue
#определяет четность нечетность
    if count_ones%2==0:
        print("Бит четности:", 0)
    else:
        print("Бит четности:", 1)

    



    
