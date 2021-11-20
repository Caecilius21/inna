from django.urls import path
from . import views

urlpatterns = [
    path('api/word/', views.WordListCreate.as_view() ),
]
