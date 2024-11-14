import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if len(line) == 0:
                break
            all_data.append(line.strip())  # Убираем перенос строки
    # Возвращать или выводить можно, но в этом примере мы просто читаем информацию

if __name__ == '__main__':
    filenames = [f'./Files/file {number}.txt' for number in range(1, 4)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print(f'{end_time - start_time:.6f} (линейный)')

    # # Многопроцессный вызов
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f'{end_time - start_time:.6f} (многопроцессный)')