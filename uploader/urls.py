from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # ✅ this one is correct

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_file, name='upload'),
    path('login/', auth_views.LoginView.as_view(template_name='uploader/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('permission-denied/', views.permission_denied, name='permission_denied'),
]
