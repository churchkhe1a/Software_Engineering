from collections import Counter

def top_10_words(file_path):

  with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read().lower()
    words = text.split()
    word_counts = Counter(words)
    top_10 = word_counts.most_common(10)
    return top_10

file_path = 'text.txt'
top_words = top_10_words(file_path)

print("10 самых частых слов:")
for word, count in top_words:
  print(f"{word}: {count}")
