from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import TaskForm
from .models import Task #se llama para hacer una consula a la bd
#


def home(request):
    return render(request, "home.html")


def signup(request):
    if request.method == "GET":
        print("enviando formulario")
    else:
        if request.POST["password1"] == request.POST["password2"]:
            # register user
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect('tasks')
            except:
                return render(request, "signup.html", {
                    "form": UserCreationForm,
                    "error": "Username allready exist"})

        return render(request, "signup.html", {
            "form": UserCreationForm,
            "error": "Password do not match"})


def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True) #esto devuelve todas las tareas que estan en la bd
    return render(request, 'tasks.html', {'tasks':tasks})
# de all se pasa a filter para filtrar la info por usuario y que no se acceda a datos
#de otros usuarios por medio de un usuario normal
#dentro del filtro se busca la info correspondiente al usuario actual en inicio de sesion

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': TaskForm
        })
    else:
        try:
            # le pasa los datos ingresados de post a la clase taskform
            form = TaskForm(request.POST)
            # este commit devuelve los datos dentro del form
            new_task = form.save(commit=False)
            new_task.user = request.user  # es necesario llamar al usuario de la sesion por
            new_task.save()
            return redirect('tasks')#al guardar redirecciona a la pag tasks
        except ValueError:#se activa cuando consideremos un error
            return render(request, 'create_task.html', {
                'form': TaskForm,
                'error':'please provide valida data'#mensaje de error sino funciona
            })


def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'],
            password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('tasks')
