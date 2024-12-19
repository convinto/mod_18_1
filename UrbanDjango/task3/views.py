from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def resurs(request):
    resurses = [
        {'name': 'Преимущества цифрового образования для детей', 'price':'Узнать подробнее'},
        {'name': 'Проблемы и вызовы в сфере детского цифрового образования', 'price': 'Узнать подробнее'},
        {'name': 'Примеры успешных практик', 'price': 'Узнать подробнее'},
        {'name': 'Лучшие учебные платформы для детей', 'price': 'Узнать подробнее'},
        {'name': 'Государственная поддержка детского образования', 'price': 'Узнать подробнее'},
    ]
    return render(request, 'resurs.html', {'resurs':resurses})
def about(request):
    return render(request, 'about.html')