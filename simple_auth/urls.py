
from django.contrib import admin
from django.urls import path, include
# from django.contrib.auth import views as auth
import django.contrib.auth.urls
from apps import views 
from apps.views import home, register
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', include(django.contrib.auth.urls)),    
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('register/', views.register, name="register"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)