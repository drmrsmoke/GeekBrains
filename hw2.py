def user_profile(name, surname, burn_year, sity):
    print(f'{name} {surname} вы родились в {burn_year} году и проживаете в городе {sity}')


user_profile(name=input('Введите ваше Имя '), surname=input('Ваща фамилия '),
             burn_year=input('Год рождения '), sity=input('Город проживания '))