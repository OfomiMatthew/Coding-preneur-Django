from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def get_article(request):
  obj = Article.objects.get(id=1)
  articles = Article.objects.all()
  my_list = [1,2,4]
  return render(request,'home.html',{'articles':articles})

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
  context ={"form":ArticleForm()}
  if request.method == 'POST':
    
    title = request.POST.get('title')
    content = request.POST.get('content')
    print("title:",title)
    print("content:",content)
    article_object = Article.objects.create(title=title,content=content)
    context['object'] = article_object
    context['created'] = True
    # context['content'] = content
  
  
  return render(request,'create.html',context=context)

def login_view(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request,username=username,password=password)
    if user is None:
      context = {"error":"Invalid credentials"}
      return render(request,'login.html',context)
    login(request,user)
    return redirect('article')
      
  return render(request,'login.html')

def logout_view(request):
  if request.method == 'POST':
    logout(request)
    return redirect('login')
  return render(request,'logout.html')
  
  