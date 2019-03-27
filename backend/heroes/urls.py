from django.urls import path
from .views import HeroList, HeroDetail

urlpatterns = [
    path('', HeroList.as_view()),
    path('<int:number>', HeroDetail.as_view()),
]