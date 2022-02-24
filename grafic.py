import datetime

dni = ''
while type(dni) != int:
    print('Сколько дней в неделю вы учитесь?(введите чилсо)')
    dni = input()
    if dni.isdigit():
        dni = int(dni)
        if dni not in [5, 6]:
            print('Введите число 5 или 6')
    else:
        print('Введите число 5 или 6')
parti = ''
while type(parti) != int:
    print('Сколько парт у вас в классе?(введите чилсо)')
    parti = input()
    if parti.isdigit():
        parti = int(parti)
    else:
        print('Введите число')
ryadi = 3
vchera = ''
while type(vchera) != int:
    print('Какой номер парты вчера дежурил?(введите чилсо)')
    vchera = input()
    if vchera.isdigit():
        vchera = int(vchera)
    else:
        print('Введите число')
today = datetime.date.today().weekday()
dni_nedeli = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
ci = 0
for i in range(today, dni):
    a = vchera+i
    print('{}: {}'.format(dni_nedeli[i], a-today+1))
    if a>parti:
        ci = i+1
        break
if ci>0:
    for i, j in enumerate(range(ci, dni)):
        print('{}: {}'.format(dni_nedeli[j], i+1))
