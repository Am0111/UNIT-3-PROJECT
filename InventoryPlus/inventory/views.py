from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

def home(request:HttpRequest):

    return render(request, "inventory/home.html")
