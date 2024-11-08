
from time import sleep, time
import threading
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding="utf-8") as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

# Время начала обычных вызовов
start_time = time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
# Время окончания обычных вызовов
end_time = time()
print(f"Время работы функций: {end_time - start_time}")
# Потоки
threads = []
def thread_target(word_count, file_name):
    write_words(word_count, file_name)
start_time_threads = time()
for files in [(10, 'example5.txt'), (30, 'example6.txt'),
             (200, 'example7.txt'), (100, 'example8.txt')]:
    thread = threading.Thread(target=thread_target, args = files)
    threads.append(thread)
    thread.start()
# Ожидание завершения потоков
for t in threads:
    t.join()
end_time_threads = time()
print(f"Время работы потоков: {end_time_threads - start_time_threads}")
