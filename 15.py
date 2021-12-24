def max_sum(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        before_current = i - 1
        while (before_current >= 0 and current < arr[before_current]):
            arr[before_current + 1] = arr[before_current]
            before_current -= 1
            arr[before_current + 1] = current    
    half_of_lenth = len(arr) // 2
    l = []
    for i in range(0, half_of_lenth):
        b = [arr[half_of_lenth -1 - i], arr[half_of_lenth + i]]
        l.append(b)
    mmm = []
    for i in l:
        mmm.append(sum(i))
    return mmm[-1]

if __name__ == '__main__':
    import time
    
    a = input('''Добро пожаловать!\nЭта программа объединяет числа в пары так, что:\n1) Для каждого числа есть своя пара;\n2) Максимальная парная сумма является наименьшей возможной.\n\nЕсли вы хотите выйти, введите "exit". Чтобы продолжить, нажмите Enter.\n''')
    
    while True:
        if a == 'exit':
            print('До новых встреч!')
            time.sleep(1)
            break
        nums = input('Введите четное количество чисел через пробел\n')
        nums = nums.split()
        array = []   
        for i in nums:
            array.append(int(i))
        print(f'Наименьшая возможная максимальная пара - {max_sum(array)}')
        
        a = input('\nЕсли вы хотите выйти, напишите "exit". Если хотите остаться, нажмите Enter\n')

