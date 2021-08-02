from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmopqrstuvwxyz')
    uppercase_characters = list('ABCDEFGHIJKLMOPQRSTUVWXYZ')
    numbers = list('1234567890')
    special = '!@#$%^&*()_-+={}?'

    if request.GET.get('uppercase'):
        characters.extend(uppercase_characters)
    if request.GET.get('special'):
        characters.extend(special)
    if request.GET.get('numbers'):
        characters.extend(numbers)

    length = int(request.GET.get('length', 12))  # 12 - значение по умолчанию

    the_password = ''

    for x in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})


def about(request):
    return render(request, 'generator/about.html')