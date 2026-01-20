from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.contrib.auth.models import User
from accounts.models import Donor
from django.utils import timezone

# --- সব ইউজারকে একবারে ফিক্স করার ম্যাজিক ফাংশন ---
def fix_all_users_at_once(request):
    try:
        all_users = User.objects.all()
        fixed_count = 0
        for user in all_users:
            # যদি ইউজারের ডোনার প্রোফাইল না থাকে, তবে তৈরি করবে
            if not hasattr(user, 'donor'):
                Donor.objects.create(
                    user=user,
                    full_name=user.username,
                    blood_group='O+', # ডিফল্ট গ্রুপ
                    mobile_number='01700000000',
                    district='Patiya',
                    upazila='Patiya',
                    last_donation_date=timezone.now().date()
                )
                fixed_count += 1
        return HttpResponse(f"<h1>Success!</h1><p>Fixed {fixed_count} users. Now everyone can login!</p>")
    except Exception as e:
        return HttpResponse(f"Error occurred: {e}")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fix-everyone/', fix_all_users_at_once), # এই লিঙ্কটি রান করবেন
    path('', include('blood_requests.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin-panel/', include('admin_panel.urls')),

    # Password Reset URLs
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
