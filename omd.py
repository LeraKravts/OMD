def step1():
    print('Что мы будем делать - плавать или идти?')
    options = {'плавать': True, 'идти': False}
    option = input()
    while option not in options:
        print('Скажи {} или {}'.format(*options))
        option = input()

    if options[option]:
        return step2()
    return step3()

#     location = input('Что будем делать - плавать или идти?')    
#     if location == 'плавать':
#         print('Спасибо! Я люблю плавать :)')
#         step2()
#         quit()

#     if location == 'идти':
#         print('Что ж! Пойдем пешком..')
#         small_talk = input('Как твои дела?')
#         print('Честно, я больше люблю плавать')
#         step3()
#         quit()

#     else:
#         print('Прости, я могу только идти или плавать. Напиши, что мне делать!')
#         step1()

def step2():
    player_answer = str(input('Ты умеешь плавать?'))
    if player_answer == 'да':
        print('Какая удача!')
    elif player_answer == 'нет':
        print('Чувствую, плыть мне сегодня одной..')
    else:
        print('отвечай "да" или "нет"')
        step2()


def step3():
    try:
        distance = int(input('Cколько километров еще идти?'))
        if distance <= 1:
            print('Думаю, я справлюсь! С тобой весело)) ')
        elif distance > 1:
            print('Далекооооо!!')
            step4()

    except ValueError:
        print('Напиши число!')
        step3()
        
        
def step4():
    print('Может вернемся домой?')
    option = ''
    options = {'да': True, 'нет': False}
    option = input()
    while option not in options:
        print('Скажи: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return print('ураа!')
    return print(':(')

if __name__=='__main__':
    print('Уточка решила погулять. ')
    step1()






