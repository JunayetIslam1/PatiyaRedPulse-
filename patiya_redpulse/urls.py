from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from accounts.models import Donor
from django.utils import timezone

def fix_users(request):
    try:
        # লগআউট করে সেশন ক্লিয়ার করবে
        logout(request)
        users = User.objects.all()
        count = 0
        for user in users:
            if not hasattr(user, 'donor'):
                Donor.objects.create(
                    user=user,
                    full_name=user.username,
                    blood_group='O+',
                    gender='Male',
                    mobile_number='01700000000',
                    district='Patiya',
                    upazila='Patiya',
                    last_donation_date=timezone.now().date()
                )
                count += 1
        return HttpResponse(f"Fixed {count} profiles and cleared sessions. Try to login now!")
    except Exception as e:
        return HttpResponse(f"Error: {e}")

urlpatterns = [
    path('fix-old-users/', fix_users),
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
