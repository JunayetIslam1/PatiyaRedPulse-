from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register_donor, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
<<<<<<< HEAD
    # LogoutView আগের মতোই থাকবে, তবে টেমপ্লেটে পরিবর্তন আনতে হবে
=======
>>>>>>> 37d8f18213b0ff290b28b28f914acac1d43f7d74
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('donors/', views.donor_list, name='donor_list'),
]