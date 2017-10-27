from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    print(request.POST)
    return render(request, 'page1.html', {'request':request})