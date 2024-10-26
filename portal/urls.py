from django.urls import path
from portal import views

app_name = 'portal'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
