
from django.urls import path
from . import views

urlpatterns=[

                    path('',views.signin,name='signin'),
                    path('postsign/',views.postsign),
                    path('logout/',views.logout,name='log'),
                    path('signup/',views.signup,name='signup'),










]