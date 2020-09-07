from django.shortcuts import render

def set_cookies(request):

    response = render(request, 'app_signed/set_cookie.html')
    response.set_signed_cookie('name', 'Aakash', salt='personal_name')
    return response

def get_cookies(request):

    name = request.get_signed_cookie('name', default='Guest', salt='personal_name')
    context = {'name': name}
    return render(request, 'app_signed/get_cookie.html', context)