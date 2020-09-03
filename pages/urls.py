from django.urls import path

from . import views

urlpatterns = [
        path('', views.HomePageView.as_view(), name='home'),
        path('dedic/', views.DediPageView.as_view(), name='dedicatoria'),
        path('нераскрытым/', views.RussPageView.as_view(), name='нераскрытым'),
]
