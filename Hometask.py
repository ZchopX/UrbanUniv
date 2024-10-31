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

