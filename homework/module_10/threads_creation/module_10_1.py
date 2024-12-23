import threading
import time
import datetime

def time_track_generator(name):
    def time_track(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Время работы {name}: {datetime.timedelta(seconds=elapsed_time % (24 * 60), 
                                                             minutes=elapsed_time // 60, 
                                                             hours=elapsed_time // (24 * 60), 
                                                             milliseconds=(elapsed_time % (24 * 60)) * 1000)}")
        return wrapper
    return time_track

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово №{i}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

word_counts = (10, 30, 200, 100)
func_file_names = (f'example{i}.txt' for i in range(1, 5))
threads_file_names = (f'example{i}.txt' for i in range(5, 9))

@time_track_generator("функций")
def func_write_words():
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')

@time_track_generator("потоков")
def thread_write_words():
    thread_1 = threading.Thread(target=write_words, kwargs={'word_count': 10, 'file_name': 'example5.txt'})
    thread_2 = threading.Thread(target=write_words, kwargs={'word_count': 30, 'file_name': 'example6.txt'})
    thread_3 = threading.Thread(target=write_words, kwargs={'word_count': 200, 'file_name': 'example7.txt'})
    thread_4 = threading.Thread(target=write_words, kwargs={'word_count': 100, 'file_name': 'example8.txt'})

    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()

    thread_1.join()
    thread_2.join()
    thread_3.join()
    thread_4.join()

func_write_words()
thread_write_words()