from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request):
    lucky_no = random.randint(1,42)
    numbers = list()
    for i in range(6):
        numbers.append(random.randint(1,42))
    return render(request,"index.html",locals())