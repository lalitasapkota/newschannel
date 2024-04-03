from django.urls import path
from . import views

urlpatterns = [
    path('',views.news_list,name='home'),
    path('scrape/', views.scrape, name="scrape"),

]
