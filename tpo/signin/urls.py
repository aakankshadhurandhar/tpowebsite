
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[

                    path('',views.signin,name='signin'),
                    path('postsign/',views.postsign),
                    path('logout/',views.logout,name='log'),
                    path('signup/',views.signup,name='signup'),
                    path('postsignup/',views.postsignup),
                    path('profile/', views.profile,name='profile'),
                    path('postprofile/',views.postprofile),







]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)