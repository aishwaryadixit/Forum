from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


@login_required
def hello_world(request):
    return HttpResponse("hello, world")
