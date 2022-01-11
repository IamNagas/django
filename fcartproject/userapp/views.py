from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display (req):
    return HttpResponse("<h1>chandan</h1>")

def login (req):
    return HttpResponse("<h1>welcome to psa</h1>")
def logout(req):
    return HttpResponse("<h1>thank you psa</h1>")

def getindex(req):
    return render(req,'index.html')

