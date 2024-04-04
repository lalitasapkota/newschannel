from django.urls import path
from . import views

urlpatterns = [
    path('',views.news_list,name='home'),
    path('scrape/', views.scrape, name="scrape"),
    path('break',views.index,name='break'),
    path('base/',views.base,name='base'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login')

]
