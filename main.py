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

# Задача 2. Cook book

cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],
      ]
  ]
]

def receipe(dish, person):
    for i in range(len(cook_book)):
        if cook_book[i][0] == dish:
            print(f'{dish.capitalize()}:')
            dish = cook_book[i][1]
            for j in range(len(dish)):
                print(f'{dish[j][0]}, {dish[j][1] * person}{dish[j][2]}')
    print()

dish = input('Название блюда: ')
person = int(input('Количество персон: '))

receipe(dish, person)
