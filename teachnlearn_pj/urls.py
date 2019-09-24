"""teachnlearn_pj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from request import views as request_views

urlpatterns = [
    path('', include('tl_app.urls')),
    path('admin/', admin.site.urls),
    path('req_form/', request_views.ReqCreateView.as_view(), name='reqpost-create'),
    path('req_posts/', request_views.ReqListView.as_view(), name='reqposts'),
    path('reqpost/<int:pk>/', request_views.ReqDetailView.as_view(), name='reqpost-detail'),
    path('register/', user_views.register, name='register'),
    path('yourpage/', user_views.yourpage, name='yourpage'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)