from django.urls  import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name = 'home'),
    path('treasure/', views.treasure, name= 'treasure'),
    path('register/', views.register, name= 'register'),
    path('login/', LoginView.as_view(), name= 'login'),
    path('logout', LogoutView.as_view(next_page = 'home'), name = 'logout'), # the second way to logout
    # first way is already mentioned on settings.py of config line 128
]