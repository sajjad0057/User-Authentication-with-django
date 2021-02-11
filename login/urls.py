from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Login_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
