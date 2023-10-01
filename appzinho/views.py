from django.shortcuts import render, redirect
from .models import FilmesFamosos, TopFilmes, Nomeados
from .forms import FilmesForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

@login_required
def homepage(request):
  filmes = FilmesFamosos.objects.all()
  top = TopFilmes.objects.all()
  nomeados = Nomeados.objects.all()
  return render(request, "home.html", context={
    "filmes":filmes,
    "top_filmes":top,
    "nomeados_filmes": nomeados
  })

@login_required
def top_movies(request):
  options = TopFilmes.feelings.field.choices
  if request.method=="POST":
    TopFilmes.objects.create(
      title = request.POST["title"],
      main_character = request.POST["main_character"],
      feelings = request.POST["feelings"],
      position_in_top = request.POST["position_in_top"],
      release_date = request.POST["release_date"]
    )
    return redirect("home")  
    
  return render(request,"forms.html", context={"action":"Adicionar","options":options})

@login_required
def update_top_movies(request,id):
  top = TopFilmes.objects.get(id=id)
  options = TopFilmes.feelings.field.choices
  if request.method=="POST":
    top.title = request.POST["title"]
    top.main_character = request.POST["main_character"]
    top.feelings = request.POST["feelings"]
    top.position_in_top = request.POST["position_in_top"]
    top.release_date = request.POST["release_date"]
    top.save()
    return redirect("home")  
  return render(request,"forms.html", context={"action":"Atualizar","top_filmes":top,"options":options})

@login_required
def delete_top_movies(request,id):
  top = TopFilmes.objects.get(id=id)
  if request.method=="POST":
    if "confirm" in request.POST:
      top.delete()
    return redirect("home")  
  return render(request,"are_you_sure.html", context={"top_filmes":top})

@login_required
def movies(request):
  form = FilmesForm()
  if request.method =='POST':
    form = FilmesForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("home") 
  return render(request, "forms1.html", context={"action":"Adicionar","form":form})

@login_required
def update_movies(request,id):
  filmes = FilmesFamosos.objects.get(id=id)
  form = FilmesForm(instance = filmes)
  if request.method=="POST":
    form = FilmesForm(request.POST, instance=filmes)
    if form.is_valid():
      form.save()
      return redirect("home") 
  return render(request,"forms1.html", context={"action":"Atualizar","form":form})

@login_required
def delete_movies(request,id):
  filmes = FilmesFamosos.objects.get(id=id)
  if request.method=="POST":
    if "confirm" in request.POST:
      filmes.delete()
    return redirect("home")  
  return render(request,"are_you_sure.html", context={"filmes":filmes})

def create_user(request):
  if request.method == "POST":
    user = User.objects.create_user(
      request.POST["username"],
      request.POST["email"],
      request.POST["password"]      
    )
    user.save()
    return redirect("home")
  return render(request,"register.html", context={"action":"Adicionar"})

def login_user(request):
  if request.method =="POST":
    user = authenticate(
      username = request.POST["username"],
      password = request.POST["password"] 
    )
    if user != None:
      login(request, user)
    else:
      return render(request,"login.html",context={"error_msg":"Usuário não encontrado! =c"})
    if request.user.is_authenticated:
      return redirect("home")
    return render(request,"login.html",context={"error_msg":"Usuário não conseguiu ser logado! =c"})
  return render(request,"login.html")

def logout_user(request):
  logout(request)
  return redirect("login")