from django.urls import path
from . import views
from .models import Headline


app_name = "news"
urlpatterns = [
    path('', views.index, name="index"),
    #path('headlines/',views.headlines_view, name="headlines_view"),
    path('get_news/', views.get_headlines, name='get_headlines'),
]
