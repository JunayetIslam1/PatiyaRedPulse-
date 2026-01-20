from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.contrib.auth.models import User
from accounts.models import Donor

# --- নতুন অ্যাডমিন তৈরি করার ফাংশন ---
def create_new_admin(request):
    try:
        # 'admin_new' নামে একটি ইউজার তৈরি হবে, পাসওয়ার্ড হবে 'Admin1234'
        if not User.objects.filter(username='admin_new').exists():
            user = User.objects.create_superuser('admin_new', 'admin@example.com', 'Admin1234')
            return HttpResponse("New Admin created! Username: admin_new, Password: Admin1234. Login now at /admin")
        else:
            return HttpResponse("Admin already exists.")
    except Exception as e:
        return HttpResponse(f"Error: {e}")

urlpatterns = [
    path('make-me-admin-now/', create_new_admin), # এই লিঙ্কে গেলে অ্যাডমিন তৈরি হবে
    path('admin/', admin.site.urls),
    path('', include('blood_requests.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin-panel/', include('admin_panel.urls')),

    # Password Reset
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
