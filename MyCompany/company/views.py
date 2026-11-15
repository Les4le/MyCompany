from django.shortcuts import render


def home(request):
    return render(request, 'company/section.html', {
        'title': 'Головна сторінка',
        'description': 'Вітаємо на сайті нашої компанії!'
    })


def news(request):
    return render(request, 'company/section.html', {
        'title': 'Новини',
        'description': 'Тут знаходяться новини нашої компанії.'
    })


def management(request):
    return render(request, 'company/section.html', {
        'title': 'Керівництво компанії',
        'description': 'Інформація про керівництво компанії.'
    })


def about(request):
    return render(request, 'company/section.html', {
        'title': 'Про компанію',
        'description': 'Історія та інформація про нашу компанію.'
    })


def contacts(request):
    return render(request, 'company/section.html', {
        'title': 'Контакти',
        'description': 'Контактна інформація нашої компанії.'
    })
    
def contacts_country(request, country):
    countries = {
        'france': 'Франція',
        'ukraine': 'Україна',
        'austria': 'Австрія'
    }

    country_name = countries.get(country.lower(), country.capitalize())

    return render(request, 'company/section.html', {
        'title': 'Контакти — ' + country_name,
        'description': 'Контактна інформація компанії в країні: ' + country_name
    })