from collections import Counter
import re


def analyze_text_file(directory):
    try:
        with open(directory, 'r', encoding='utf-8') as file:
            text = file.read()
        words = re.findall(r'\b\w+\b', text.lower())
        word_count = len(words)
        word_frequency = Counter(words)
        most_common_word, most_common_count = word_frequency.most_common(1)[0]
        print(f"Количество слов в файле: {word_count}")
        print(f"Самое часто встречающееся слово: '{most_common_word}' (встречается {most_common_count} раз)")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
analyze_text_file(r'C:\Users\Aleks\PycharmProjects\Tema7\bananacat.txt')
