from django.urls import path 
from . import views

urlpatterns = [
    path('',views.get_article,name='article'),
    path('<int:id>',views.an_article,name='an-article'),
    path('search',views.article_search,name='article-search'),
    path('create',views.article_create,name='article-create'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout')
]
