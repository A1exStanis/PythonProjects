from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

month_info = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
types_dict = {
    'Fire': ['aries', 'leo', 'sagittarius'],
    'Earth': ['taurus', 'virgo', 'capricorn'],
    'Air': ['gemini', 'libra', 'aquarius'],
    'Water': ['cancer', 'scorpio', 'pisces']
}

calculation_dict = {
    'aries': range(80, 110),
    'taurus': range(110, 142),
    'gemini': range(142, 173),
    'cancer': range(173, 204),
    'leo': range(204, 234),
    'virgo': range(234, 267),
    'libra': range(267, 297),
    'scorpio': range(297, 327),
    'sagittarius': range(327, 357),
    'capricorn': range(357, 365) and range(21),
    'aquarius': range(21, 51),
    'pisces': range(51, 80)
}

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}


def index(request):
    zodiacs = list(zodiac_dict)
    # f'<li><a href="{redirect_path}">{sign.title()} </a></li>'
    context = {
        'zodiacs': zodiacs
    }
    return render(request, 'horoscop/index.html', context=context)


def get_info(request, sign_zodiac: str):
    if sign_zodiac in zodiac_dict:
        description = zodiac_dict.get(sign_zodiac)
        data = {
            'description_zodiac': description,
            'description_title': sign_zodiac,
            'zodiacs': zodiac_dict
        }
        return render(request, 'horoscop/info_zodiac.html', context=data)



def get_info_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f"Неправильно вказаний порядковий номер знаку зодіака {sign_zodiac}")
    name = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name,))
    return HttpResponseRedirect(redirect_url)


def make_types(request):
    types = list(types_dict)
    rez = ''
    for sign in types:
        redirect_path = reverse('horoscope-name', args=(sign,))
        rez += f'<li><a href="{redirect_path}">{sign.title()} </a></li>'
    response = f"""
        <ol>
        {rez}
        </ol>
        """
    return HttpResponse(response)


def get_info_by_date(request, month, day):
    count_day = sum(month_info[:(month - 1)]) + day
    for sign in calculation_dict:
        if count_day in calculation_dict.get(sign):
            redirect_url = reverse('horoscope-name', args=(sign,))
            return HttpResponseRedirect(redirect_url)
