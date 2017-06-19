from django.shortcuts import render
from .forms import userForm


def main(request):
    return render(request, 'main/main.html', locals())

def home(request):
    return render(request, 'main/home.html', locals())
