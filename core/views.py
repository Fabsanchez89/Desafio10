from django.shortcuts import render

def viewsIndex(request):
    return render(request, 'index.html' ,{})

def viewsNosotros(request):
    return render(request, 'nosotros.html' ,{})