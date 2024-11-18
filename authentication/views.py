from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
from django.contrib.auth import logout as auth_logout

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return JsonResponse({"username": user.username, "status": True, "message": "Successful login!"}, status=200)
        else:
            return JsonResponse({"status": False, "message": "Unsuccessful login, account deactivated."}, status=401)

    else:
        return JsonResponse({"status": False, "message": " Failed login, please enter the correct credentials."}, status=401)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password1 = data['password1']
        password2 = data['password2']

        if password1 != password2:
            return JsonResponse({"status": False, "message": "Passwords don't match. Try again!"}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({"status": False, "message": "Username already exists. Try again!"}, status=400)

        user = User.objects.create_user(username=username, password=password1)
        user.save()
        
        return JsonResponse({"username": user.username, "status": 'success', "message": "User created!"}, status=200)
    
    else:
        return JsonResponse({"status": False, "message": "Request method is invalid."}, status=400)

@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout successful!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout failed."
        }, status=401)