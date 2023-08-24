from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

def register(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_user(username=username, email=email, password=password)
    return JsonResponse({'status': 'success'})

def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'failure'})