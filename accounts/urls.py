from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from accounts import views
from django.conf.urls.static import static 
from django.conf import settings
urlpatterns = [
    path('register', views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)