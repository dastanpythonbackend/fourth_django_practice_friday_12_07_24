from django.urls import path
from .views import home_page_view, register_view, profile_view, create_repair_request_view, repair_request_list_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home_page_view, name='home_page'),
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('profile/', profile_view, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('repair_request/', create_repair_request_view, name='repair_request'),
    path('repair_request_list/', repair_request_list_view, name='repair_request_list'),
]
