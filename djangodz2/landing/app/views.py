from collections import Counter
from django.http import HttpResponse
from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    lending_type = request.GET.get('from-landing')

    if lending_type == 'original':
        counter_click['original'] += 1

    if lending_type == 'test':
        counter_click['test'] += 1

    return render(request, 'index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов

    lending_type = request.GET.get('ab-test-arg', 'original')
    if lending_type == 'original':
        counter_show['original'] += 1
        return render(request, 'landing.html')

    if lending_type == 'test':
        counter_show['test'] += 1
        return render(request, 'landing_alternate.html')

    msg = 'Некорректный GET параметр ab-test-arg. Пожалуйста, введите "original" или "test"'
    return HttpResponse(msg)


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:

    context = {
        'test_conversion': counter_click['test'] / counter_show['test'],
        'original_conversion': counter_click['original'] / counter_show['original'],
    }

    return render(request, 'stats.html', context=context)
