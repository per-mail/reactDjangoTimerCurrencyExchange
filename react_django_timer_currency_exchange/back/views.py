from django.shortcuts import render


# def index(request):
#     return render(request, 'index.html')


import requests


def index(request):
    # делаем запрос к api
    response = requests.get(url='https://api.exchangerate-api.com/v4/latest/USD').json()
    # получаем словарь  с ключами название валюты и значениеми их стоимость относительно доллара
    # сохраняем результат в переменную currencies
    currencies = response.get('rates')

    if request.method == 'GET':  # если страница загрузилась
        # получаем словарь context в котором словарь currencies
        context = {
            'currencies': currencies
            # currencies словарь с ключом название валюты и значением её стоимость относительно доллара
        }

        # формируем ответ файл index.html с данными из словаря context
        return render(request, 'index.html', context)

    if request.method == 'POST':  # если пользователь ввёл данные в таблицу
        from_amount = float(request.POST.get('from-amount'))  # получаем введённое число
        from_curr = request.POST.get('from-curr')  # получаем валюту которую меняем
        to_curr = request.POST.get('to-curr')  # получаем валюту на которую меняем

        # делаем  конвертацию результат округляем до второго знака после запятой
        # из словаря currencies берём значения валют, значение валюты которую меняем  делим на значение валюты на которую меняем и умножаем на введённое число преведённое в дробную форму
        converted_amount = round((currencies[to_curr] / currencies[from_curr]) * float(from_amount), 2)

        # создаём словарь с данными,
        context = {
            'from_curr': from_curr,  # необходимо передать для того чтобы заполненные значения полей не сбрасывались
            'to_curr': to_curr,  # необходимо передать для того чтобы заполненные значения полей не сбрасывались
            'from_amount': from_amount,  # необходимо передать для того чтобы заполненные значения полей не сбрасывались
            'currencies': currencies,
            'converted_amount': converted_amount
        }

        return render(request, 'index.html', context)

# python3 manage.py runserver