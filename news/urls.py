from django.urls import path
from . import views
from .models import Headline


app_name = "news"
urlpatterns = [
    path('', views.index, name="index"),
    path('crypto/',views.crypto_news),
    path('get_news/', views.get_headlines, name='get_headlines'),
]
