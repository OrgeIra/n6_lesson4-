from django.shortcuts import  render

def login_view(request):
    return render(request, 'index.html')

def register(request):
    pass