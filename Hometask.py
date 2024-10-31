### Practical task ###


Journal = dict()

question = str(input('Вы хотите внести оценки ученика в журнал? (Да/Нет) '))
if question==('Да'):
    while question==('Да'):
        name = input('Введите имя ученика, чьи оценки вы желаете внести ')
        score = list(input("Введите оценки ученика (без запятых) "))
        for i in range(len(score)):
            score[i] = int(score[i])

        score = sum(score)/len(score)
        print(name,score,'\n')
        Journal.update({name:score})
        scnd_question = input('Хотите добавить ещё одного ученика? (Да/Нет) ')
        question = (scnd_question)
        if question==('Нет'):
            print( '\nВот средний балл учеников на данный момент')
            print(Journal)
            print('Вы вышли из программы. До свидания!')
        elif question==('Да'):
            print('')
        else:
            print('\nВот средний балл учеников на данный момент')
            print(Journal)
            print('Вы вышли из программы. До свидания!')


else:
    print('Вот средний балл учеников на данный момент')
    print(Journal)
    print('Вы вышли из программы. До свидания!')

######################################
### Practical task ###

Journal = dict()
scores = list()
mean_score = list()
names = set()

question = str(input('Вы хотите внести оценки учеников в журнал? (Да/Нет) '))
if question==('Да') or ('да') or ('Lf') or ('lf'):
    while question==('Да') or ('да') or ('Lf') or ('lf'):
        names.add(input('Введите имя ученика, чьи оценки вы желаете внести '))

        question = input('Хотите добавить ещё одного ученика? (Да/Нет) ')
        if question!=('Да') or ('да') or ('Lf') or ('lf'):
            break
        else:
            continue

    sort_names = sorted(names)
    for i in range(len(sort_names)):
        a = input(f'Введите оценки ученика (без запятых) '
                                     f'{sort_names[i]}: ')
        a = list(a)
        mean = (sum(a)/len(a))
        mean_score.append(mean)
        Journal.update({sort_names[i]: mean_score[i]})

else:
    print('Вот средний балл учеников на данный момент\n',
          Journal,
          '\nВы вышли из программы. До свидания!')



# question = str(input('Вы хотите внести оценки учеников в журнал? (Да/Нет) '))
# if question==('Да'):
#     while question==('Да'):
#         names.add(input('Введите имена учеников, чьи оценки вы желаете внести '))
#         sort_names = sorted(name)
#         for i in len(sort_names):
#             list.append ('Введите оценки ученика ', )
#             scnd_question = input('Хотите добавить ещё одного ученика? (Да/Нет) ')
#             question = (scnd_question)
#
#
#
#
#
#
#
#
#         if question==('Нет'):
#             print( '\nВот средний балл учеников на данный момент')
#             print(Journal)
#             print('Вы вышли из программы. До свидания!')
#         elif question==('Да'):
#             print('')
#         else:
#             print('\nВот средний балл учеников на данный момент')
#             print(Journal)
#             print('Вы вышли из программы. До свидания!')
#
#
# else:
#     print('Вот средний балл учеников на данный момент')
#     print(Journal)
#     print('Вы вышли из программы. До свидания!')
