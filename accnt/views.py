from django.shortcuts import render, redirect

from django.contrib.auth.models import User

# Create your views here.

# def login(request):
#     if request.method == 'POST':
#         email = request.POST['num1']
#         password = request.POST['num2']
#         result = int(email) + int(password)
#         c = {
#             'email':result,
#         }
#         return render(request,'home.html',c)
#     else :
#         return render(request,'login.html')


def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        pass1 = request.POST["password"]

        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=pass1,
        )
        user.save()
        print("user created ")
        return redirect("/")

    else:
        return render(request, "register.html")
