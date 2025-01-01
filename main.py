def count_characters(text):
    # Преобразуем текст в нижний регистр
    text = text.lower()
    
    # Создаем словарь для подсчета символов
    char_count = {}
    
    # Проходим по каждому символу в тексте
    for char in text:
        # Игнорируем символы, которые не являются буквами
        if char.isalpha():  # Проверяем, что символ - это буква
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count

def count_words(text):
    # Разбиваем строку на слова и возвращаем количество
    words = text.split()
    return len(words)

def print_report(word_count, char_count):
    # Сортируем символы по количеству их повторений (по убыванию)
    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    
    # Печать отчета
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    
    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

def main():
    # Указываем путь к файлу
    path_to_file = 'books/frankenstein.txt'
    
    # Открываем файл с использованием блока with
    with open(path_to_file, 'r') as f:
        # Читаем содержимое файла
        file_contents = f.read()
    
    # Считаем количество слов
    word_count = count_words(file_contents)
    
    # Считаем количество символов
    char_count = count_characters(file_contents)
    
    # Печатаем отчет
    print_report(word_count, char_count)

# Вызываем main для выполнения программы
if __name__ == "__main__":
    main()




