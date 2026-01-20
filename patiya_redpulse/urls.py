from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User 
from django.http import HttpResponse 

# এটি নতুন অ্যাডমিন তৈরি করার কোড
def manual_reset(request):
    try:
        # নতুন ইউজারনেম 'superadmin' এবং পাসওয়ার্ড 'Patiya@2026' দিয়ে অ্যাকাউন্ট তৈরি
        from django.contrib.auth.models import User
        if not User.objects.filter(username='superadmin').exists():
            User.objects.create_superuser('superadmin', 'admin@example.com', 'Patiya@2026')
            return HttpResponse("New Superuser 'superadmin' created successfully!")
        else:
            return HttpResponse("User 'superadmin' already exists!")
    except Exception as e:
        return HttpResponse(f"Error: {e}")

urlpatterns = [
    path('reset-admin-now/', manual_reset), 
    path('admin/', admin.site.urls),
    path('', include('blood_requests.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin-panel/', include('admin_panel.urls')),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
