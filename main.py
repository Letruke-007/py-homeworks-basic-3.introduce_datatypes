# Задача 1. Рекомендации по знакомству дата-сервиса

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

boys = sorted(boys)
girls = sorted(girls)

if len(boys) == len(girls):
    pairs = list(zip(boys, girls))
    print('Идеальные пары: ')
    for i in range(len(pairs)):
        print(f'{pairs[i][0]} и {pairs[i][1]}')
else:
    print('Ошибка - кто-то останется без пары!')
