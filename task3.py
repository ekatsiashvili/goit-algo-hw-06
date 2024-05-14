import timeit
import requests

# Порівнюємо ефективність алгоритмів пошуку підрядка для Статі 1

doc_id= '1_mwu_RdKKCrJ2vedxClq4VPpgkGNZsAZ'
url = f"https://drive.google.com/uc?id={doc_id}&export=download"
response = requests.get(url)
text = response.text

# Виведемо зчитаний текст
#print(text)

article1_content = text

# Функція для алгоритму Боєра-Мура
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return 0, 0

    last_occurrence = {}
    for i in range(m):
        last_occurrence[pattern[i]] = i

    i = m - 1
    j = m - 1
    iterations = 0
    while i < n:
        iterations += 1
        if text[i] == pattern[j]:
            if j == 0:
                return iterations, i
            else:
                i -= 1
                j -= 1
        else:
            if text[i] not in last_occurrence:
                shift = m
            else:
                shift = max(1, j - last_occurrence[text[i]])
            i += m - min(j, 1 + last_occurrence.get(text[i], -1))
            j = m - 1
    return iterations, -1

# Функція для алгоритму Кнута-Морріса-Пратта
def kmp(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return 0, 0

    # Створення префікс-функції
    prefix = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix[i] = j

    # Пошук підрядка в тексті
    j = 0
    iterations = 0
    for i in range(n):
        iterations += 1
        while j > 0 and text[i] != pattern[j]:
            j = prefix[j - 1]
        if text[i] == pattern[j]:
            if j == m - 1:
                return iterations, i - m + 1  # Підрядок знайдено
            else:
                j += 1
    return iterations, -1  # Підрядок не знайдено

# Функція для алгоритму Рабіна-Карпа
def rabin_karp(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return 0, 0

    # Обчислення хешу для підрядка та першого вікна тексту
    pattern_hash = hash(pattern)
    text_hash = hash(text[:m])

    # Пошук підрядка в тексті
    iterations = 0
    for i in range(n - m + 1):
        iterations += 1
        if text_hash == pattern_hash and text[i:i + m] == pattern:
            return iterations, i  # Підрядок знайдено
        if i < n - m:
            # Обновлення хешу для наступного вікна тексту
            text_hash = hash(text[i + 1:i + m + 1])
    return iterations, -1  # Підрядок не знайдено

# Рядок для існуючого тексту
existing_text = "public static int linearSearch(int arr[], int elementToSearch"

# Рядок для неіснуючого тексту
non_existing_text = "Javac"

# Вимірюємо час виконання для підрядка, який існує в тексті, для алгоритмів Боєра-Мура, Кнута-Морріса-Пратта і Рабіна-Карпа
print("Порівнюємо ефективність алгоритмів пошуку підрядка для Статі 1:")
print("=============================================================")
print("Для підрядка, який існує в тексті:")
print("+++++++++++++++++++++++++++++++++")
print("Алгоритм Боєра-Мура:", timeit.timeit(lambda: boyer_moore(article1_content, existing_text), number=1000))
print("Алгоритм Кнута-Морріса-Пратта:", timeit.timeit(lambda: kmp(article1_content, existing_text), number=1000))
print("Алгоритм Рабіна-Карпа:", timeit.timeit(lambda: rabin_karp(article1_content, existing_text), number=1000))
print()

# Вимірюємо час виконання для вигаданого підрядка для алгоритмів Боєра-Мура, Кнута-Морріса-Пратта і Рабіна-Карпа
print("Для вигаданого підрядка:")
print("-----------------------")
print("Алгоритм Боєра-Мура:", timeit.timeit(lambda: boyer_moore(article1_content, non_existing_text), number=1000))
print("Алгоритм Кнута-Морріса-Пратта:", timeit.timeit(lambda: kmp(article1_content, non_existing_text), number=1000))
print("Алгоритм Рабіна-Карпа:", timeit.timeit(lambda: rabin_karp(article1_content, non_existing_text), number=1000))
print()

# Порівнюємо ефективність алгоритмів пошуку підрядка для Статі 2
doc_id= '1Q9oZBFn4P4xi7LXCyYgHpVWqLSq4VMJwF-XX8jimMQk'
url = f"https://drive.google.com/uc?id={doc_id}&export=download"
response = requests.get(url)
text = response.text

article2_content = text

# Рядок для існуючого тексту
existing_text = "СУБД типу NoSQL"

# Рядок для неіснуючого тексту
non_existing_text = "Java"

# Вимірюємо час виконання для підрядка, який існує в тексті, для алгоритмів Боєра-Мура, Кнута-Морріса-Пратта і Рабіна-Карпа
print("Порівнюємо ефективність алгоритмів пошуку підрядка для Статі 2:")
print("=============================================================")
print("Для підрядка, який існує в тексті:")
print("+++++++++++++++++++++++++++++++++")
print("Алгоритм Боєра-Мура:", timeit.timeit(lambda: boyer_moore(article2_content, existing_text), number=1000))
print("Алгоритм Кнута-Морріса-Пратта:", timeit.timeit(lambda: kmp(article2_content, existing_text), number=1000))
print("Алгоритм Рабіна-Карпа:", timeit.timeit(lambda: rabin_karp(article2_content, existing_text), number=1000))
print()

# Вимірюємо час виконання для вигаданого підрядка для алгоритмів Боєра-Мура, Кнута-Морріса-Пратта і Рабіна-Карпа
print("Для вигаданого підрядка:")
print("-----------------------")
print("Алгоритм Боєра-Мура:", timeit.timeit(lambda: boyer_moore(article2_content, non_existing_text), number=1000))
print("Алгоритм Кнута-Морріса-Пратта:", timeit.timeit(lambda: kmp(article2_content, non_existing_text), number=1000))
print("Алгоритм Рабіна-Карпа:", timeit.timeit(lambda: rabin_karp(article2_content, non_existing_text), number=1000))
print()

# Порівнюємо ефективність алгоритмів пошуку підрядка для обох текстів в цілому

doc_id= '1yy9vfC3PGJtdRjGzkeM_FxVwE-0kc2FIeubPNbuHuW8'
url = f"https://drive.google.com/uc?id={doc_id}&export=download"
response = requests.get(url)
text1 = response.text

doc_id= '1Q9oZBFn4P4xi7LXCyYgHpVWqLSq4VMJwF-XX8jimMQk'
url = f"https://drive.google.com/uc?id={doc_id}&export=download"
response = requests.get(url)
text2 = response.text

text=text1+text2

article_content = text

# Рядок для існуючого тексту
existing_text = "return previousStep;"

# Рядок для неіснуючого тексту
non_existing_text = "Java L"

# Вимірюємо час виконання для підрядка, який існує в тексті, для алгоритмів Боєра-Мура, Кнута-Морріса-Пратта і Рабіна-Карпа
print("Порівнюємо ефективність алгоритмів пошуку підрядка для обох текстів в цілому:")
print("============================================================================")
print("Для підрядка, який існує в тексті:")
print("+++++++++++++++++++++++++++++++++")
print("Алгоритм Боєра-Мура:", timeit.timeit(lambda: boyer_moore(article_content, existing_text), number=1000))
print("Алгоритм Кнута-Морріса-Пратта:", timeit.timeit(lambda: kmp(article_content, existing_text), number=1000))
print("Алгоритм Рабіна-Карпа:", timeit.timeit(lambda: rabin_karp(article_content, existing_text), number=1000))
print()

# Вимірюємо час виконання для вигаданого підрядка для алгоритмів Боєра-Мура, Кнута-Морріса-Пратта і Рабіна-Карпа
print("Для вигаданого підрядка:")
print("-----------------------")
print("Алгоритм Боєра-Мура:", timeit.timeit(lambda: boyer_moore(article_content, non_existing_text), number=1000))
print("Алгоритм Кнута-Морріса-Пратта:", timeit.timeit(lambda: kmp(article_content, non_existing_text), number=1000))
print("Алгоритм Рабіна-Карпа:", timeit.timeit(lambda: rabin_karp(article_content, non_existing_text), number=1000))
print()