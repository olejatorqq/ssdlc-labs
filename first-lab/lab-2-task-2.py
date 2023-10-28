# import hashlib
# import string
# import itertools
# import threading
# import time

# # Функция для проверки хеш-значения пароля
# def check_password(password, hash_value):
#     hashed_password = hashlib.sha256(password.encode()).hexdigest()
#     return hashed_password == hash_value

# # Функция для генерации пятибуквенных паролей
# def generate_passwords():
#     alphabet = string.ascii_lowercase
#     return (''.join(candidate) for candidate in itertools.product(alphabet, repeat=5))

# # Функция для выполнения перебора паролей
# def brute_force(hash_value, num_threads):
#     passwords = list(generate_passwords())
#     found = False
#     start_time = time.time()
    
#     def worker(passwords):
#         nonlocal found
#         for password in passwords:
#             if check_password(password, hash_value):
#                 print(f"Найден пароль: {password}")
#                 found = True
#                 break

#     if num_threads == 1:
#         worker(passwords)
#     else:
#         chunk_size = len(passwords) // num_threads
#         threads = []
#         for i in range(num_threads):
#             start = i * chunk_size
#             end = start + chunk_size if i < num_threads - 1 else len(passwords)
#             thread = threading.Thread(target=worker, args=(passwords[start:end],))
#             threads.append(thread)
#             thread.start()
#         for thread in threads:
#             thread.join()

#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     if not found:
#         print("Пароль не найден.")
#     print(f"Время выполнения: {elapsed_time:.2f} секунд")

# if __name__ == "__main__":
#     print("Введите хеш-значение для проверки:")
#     hash_value = input()
    
#     print("Введите количество потоков (1 для однопоточного режима):")
#     num_threads = int(input())
    
#     brute_force(hash_value, num_threads)

import hashlib
import itertools
import string
import time
import threading

# Функция для вычисления хэша SHA-256
def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

# Функция для перебора паролей
def brute_force_passwords(target_hashes, password_length, num_threads):
    characters = string.ascii_lowercase
    passwords_to_check = itertools.product(characters, repeat=password_length)
    found_passwords = []
    found_passwords_lock = threading.Lock()

    def check_passwords():
        prev_time = time.time()
        while True:
            with found_passwords_lock:
                if len(found_passwords) >= len(target_hashes):
                    break

            password = next(passwords_to_check, None)
            if password is None:
                break

            password_str = ''.join(password)
            hashed_password = sha256_hash(password_str)

            if hashed_password in target_hashes:
                with found_passwords_lock:
                    found_passwords.append((password_str, hashed_password))
                current_time = time.time()
                elapsed_time = current_time - prev_time
                prev_time = current_time
                print(f"Password: {password_str}, Hash: {hashed_password}, Time taken: {elapsed_time:.6f} seconds")

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=check_passwords)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return found_passwords

if __name__ == "__main__":
    target_hashes = [
        "1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad",
        "3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b",
        "74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f"
    ]

    password_length = 5
    try:
        num_threads = int(input("Введите количество потоков: "))
    except ValueError:
        print("Ошибка: Введите целое число")
    else:
        found_passwords = brute_force_passwords(target_hashes, password_length, num_threads)


    # for password, hashed_password, elapsed_time in found_passwords:
    #     print(f"Password: {password}, Hash: {hashed_password}, Time taken: {elapsed_time:.6f} seconds")

