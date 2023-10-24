from django.urls import path
from . import views

urlpatterns = [
    path('', views.LangingViewPage.as_view(), name="index"),
]