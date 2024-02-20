# Домашнее задание к лекции 3. «Введение в типы данных и циклы»

## Задача 1
Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек — их число может варьироваться:```boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']```    
Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту и познакомим людей с одинаковыми индексами после сортировки.
«Познакомить» пары нам поможет функция `zip`. В цикле распакуем zip-объект и выведем информацию в виде:```Идеальные пары:Alex и EmmaArthur и KateJohn и KiraPeter и LizaRichard и Trisha```    

**Внимание. Если количество людей в списках будет не совпадать, то мы никого знакомить не будем и выведем пользователю предупреждение, что кто-то может остаться без пары.**

## Задача 2
Есть структура данных `cook_book`, в которой хранится информация об ингредиентах блюд и их количестве в расчёте на одну порцию:```cook_book = [  ['салат',      [        ['картофель', 100, 'гр.'],        ['морковь', 50, 'гр.'],        ['огурцы', 50, 'гр.'],        ['горошек', 30, 'гр.'],        ['майонез', 70, 'мл.'],      ]  ],  ['пицца',        [        ['сыр', 50, 'гр.'],        ['томаты', 50, 'гр.'],        ['тесто', 100, 'гр.'],        ['бекон', 30, 'гр.'],        ['колбаса', 30, 'гр.'],        ['грибы', 20, 'гр.'],      ],  ],  ['фруктовый десерт',      [        ['хурма', 60, 'гр.'],        ['киви', 60, 'гр.'],        ['творог', 60, 'гр.'],        ['сахар', 10, 'гр.'],        ['мед', 50, 'мл.'],        ]  ]]```    и переменная, в которой хранится количество людей, на которых нужно приготовить эти блюда:```person = 5```
Нужно вывести пользователю список покупок необходимого количества ингредиентов для приготовления блюд на определённое число персон в следующем виде:```Салат:картофель, 500гр.морковь, 250гр.огурцы, 250гр.горошек, 150гр.майонез, 350мл.Пицца:сыр, 250гр.томаты, 250гр.тесто, 500гр.бекон, 150гр.колбаса, 150гр.грибы, 100гр.Фруктовый десерт:хурма, 300гр.киви, 300гр.творог, 300гр.сахар, 50гр.мед, 250мл.```

**Внимание. Реализация не должна зависеть от количества блюд, их названий и количества ингредиентов в них.**

## Задание 3
К следующей лекции прочитайте про [типы данных](https://habr.com/ru/post/319164/).

---Инструкция по выполнению домашнего задания:
1. Зарегистрируйтесь на сайте [Repl.IT](https://repl.it/).
2. Перейдите в раздел **my repls**.
3. Нажмите кнопку **Start coding now!**, если приступаете впервые, или **New Repl**, если у вас уже есть работы.
4. В списке языков выберите Python.
5. Код пишите в левой части окна.
6. Посмотреть результат выполнения файла можно, нажав на кнопку **Run**. Результат появится в правой части окна.
7. После окончания работы нажмите кнопку **Share** и скопируйте ссылку из поля *Share link*.
8. В личном кабинете на сайте [netology.ru](http://netology.ru/) в поле комментария к домашней работе вставьте скопированную ссылку и отправьте работу на проверку.

*Никаких файлов прикреплять не нужно.*
