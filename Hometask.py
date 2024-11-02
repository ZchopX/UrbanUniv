### Practical task ###

Journal = dict()
scores = list()
mean_score = list()
names = set()

question = str.lower(input('Вы хотите внести оценки учеников в журнал? (Да/Нет) '))
if question==('да') or ('lf'):

    while (question == 'да') or (question == 'lf'):
        names.add(input('Введите имя ученика, чьи оценки вы желаете внести '))

        question2 = str.lower(input('Хотите добавить ещё одного ученика? (Да/Нет) '))
        if (question2 == 'да') or (question2 == 'lf'):
            continue
        else:
            break

    sort_names = sorted(names)
    print(sort_names)
    for i in range(len(sort_names)):
        name = sort_names[i]
        score = list(input(f'Введите оценки ученика '
                                     f'{sort_names[i]}: '))
        score = [x for x in score if x != ' ' if x != ',']
        for i in range(len(score)):
            score[i] = int(score[i])

        mean = (sum(score)/len(score))
        mean_score.append(mean)
        Journal.update({name : mean})
    print('Вот средний балл учеников на данный момент\n',
          Journal,
          '\nВы вышли из программы. До свидания!')
else:
    print('\nВы вышли из программы. До свидания!')











#### PREVIOUS VERSION ####
# ### Practical task ###


# Journal = dict()

# question = str(input('Вы хотите внести оценки ученика в журнал? (Да/Нет) '))
# if question==('Да'):
#     while question==('Да'):
#         name = input('Введите имя ученика, чьи оценки вы желаете внести ')
#         score = list(input("Введите оценки ученика (без запятых) "))
#         for i in range(len(score)):
#             score[i] = int(score[i])

#         score = sum(score)/len(score)
#         print(name,score,'\n')
#         Journal.update({name:score})
#         scnd_question = input('Хотите добавить ещё одного ученика? (Да/Нет) ')
#         question = (scnd_question)
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


# else:
#     print('Вот средний балл учеников на данный момент')
#     print(Journal)
#     print('Вы вышли из программы. До свидания!')


