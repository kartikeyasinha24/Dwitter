from django.urls import path
from django.contrib.auth import views as auth_views
from .views import dashboard, profile_list, profile

app_name="dwitter"

urlpatterns = [		
	path('', dashboard, name='dashboard'),
	path('login/', auth_views.LoginView.as_view(template_name='dwitter/login.html'), name='login'),

	path('profile_list/', profile_list, name = 'profile_list'),
	path('profile/<int:pk>', profile, name='profile'),
]
