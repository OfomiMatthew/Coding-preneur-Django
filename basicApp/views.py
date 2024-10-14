from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib.auth import authenticate,login,logout
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Create your views here.

def get_article(request):
  # obj = Article.objects.get()
  articles = Article.objects.all().order_by('-id')

  return render(request,'home.html',{'articles':articles})

@login_required
def an_article(request,id):
  try:
    
    article = Article.objects.get(id=id)
  except:
    raise Http404
  return render(request,'details.html',{'article':article})



def article_search(request):
 
  query_dict = request.GET
  query = query_dict.get('query')
  article_obj = None
  if query is not None:
    try:
      article_obj = Article.objects.get(id=query)
    except Exception as e:
      raise Http404
  # context ={'obj':article_obj}
  return render(request,'search.html',{"object":article_obj})

@login_required
def article_create(request):
  form = ArticleForm(request.POST or None)
  context ={
   'form':form
 }

  if form.is_valid():
      article_object = form.save()
      context['form'] = ArticleForm()
      context['article_object'] = article_object
      return redirect('article')
     
   
  
  
  return render(request,'create.html',context=context)

def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(request,data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request,user)
      return redirect('article')
    # username = request.POST.get('username')
    # password = request.POST.get('password')
    # user = authenticate(request,username=username,password=password)
    # if user is None:
    #   context = {"error":"Invalid credentials"}
    #   return render(request,'login.html',context)
    # login(request,user)
    # return redirect('article')
  else:
    form = AuthenticationForm(request)
      
  return render(request,'login.html',{'form':form})

def logout_view(request):
  if request.method == 'POST':
    logout(request)
    return redirect('login')
  return render(request,'logout.html')

def register_view(request):
  form = UserCreationForm(request.POST or None)
  context = {'form':form}
  if form.is_valid():
    user_obj = form.save()
    context['user_obj'] = user_obj
    return redirect('login')
  return render(request,'register.html',context)
  
  