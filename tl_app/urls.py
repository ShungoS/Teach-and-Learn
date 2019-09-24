from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from .import views

urlpatterns = [
    path('', PostListView.as_view(), name='tl-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('tl_login/', views.about, name='tl-login'),
    path('contact/', views.contact, name='tl-contact'),
    path('otherteacher/', views.otherteacher, name='tl-otherteacher'),
    path('paymentinput/', views.paymentinput, name='tl-paymentinput'),
    path('profileedit/', views.profileedit, name='tl-profileedit'),
    path('request/', views.request, name='tl-request'),
    path('searchclass/', views.searchclass, name='tl-searchclass'),
    path('searchresult/', views.searchresult, name='tl-searchresult'),
    path('signup/', views.signup, name='tl-signup'),
    path('takeclass/', views.takeclass, name='tl-takeclass'),
    path('teacherregister/', views.teacherregister, name='tl-teacherregister'),
    path('teacherregisterconfirm/', views.teacherregisterconfirm, name='tl-teacherregisterconfirm'),  
]
