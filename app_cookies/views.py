from django.shortcuts import render
from datetime import datetime, timedelta

def set_cookies(request):

    context = {}
    response =  render(request, 'app_cookies/set_cookie.html')
    response.set_cookie('name', 'Onkar', expires=datetime.utcnow() + timedelta(days=3))
    return response

def get_cookies(request):
    # name = request.COOKIES['name']
    name = request.COOKIES.get('name', 'Guest')
    
    context = {'name': name}
    return render(request, 'app_cookies/get_cookie.html', context)

def del_cookies(request):

    context = {}
    response = render(request, 'app_cookies/del_cookie.html', context)
    response.delete_cookie('name')
    return response