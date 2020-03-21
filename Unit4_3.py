queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

total_queries = len(queries)
print(f'всего запросов {total_queries}')

new = {}
for i in queries:
    number = len(i.split(" "))
    if number in new:
        new[number] += 1
    else:
        new[number] = 1
print(new)

for n in new:
    a = round(new[n] / total_queries * 100)
    print(f'{a} % - {n} слов ')

