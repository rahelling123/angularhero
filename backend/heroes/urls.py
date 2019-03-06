from django.urls import path
from .views import HeroList

urlpatterns = [
    path('', HeroList.as_view())
]