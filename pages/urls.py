from django.urls import path

from . import views

urlpatterns = [
        path('', views.HomePageView.as_view(), name='home'),
        path('dedicatoria/', views.DediPageView.as_view(), name='dedicatoria'),
]
