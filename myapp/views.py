from django.shortcuts import render

# Create your views here.
def index (request) :
    context = {'mensaje' = 'bienvenidos a mi app en django'}
    return render (request, "myapp/index.html",context)
