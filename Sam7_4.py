import re

def load_banned_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]
def replace_banned_words(sentence, banned_words):
    for word in banned_words:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        sentence = pattern.sub('*' * len(word), sentence)
    return sentence
def main():
    banned_words = load_banned_words('text.txt')
    sentence = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"
    result = replace_banned_words(sentence, banned_words)
    print("Результат:", result)
if __name__ == "__main__":
    main()
