
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
            path('', views.signin, name='admin_signin'),
            path('sign/', views.sign, name='admin_signed'),

]