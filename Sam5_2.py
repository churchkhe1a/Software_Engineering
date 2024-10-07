results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

top_3 = sorted(results)[:3]

worst_3 = sorted(results, reverse=True)[:3]

results_from_10 = results[9:]

print(f"Три лучших результата: {top_3}")
print(f"Три худших результата: {worst_3}")
print(f"Все результаты начиная с 10: {results_from_10}")
