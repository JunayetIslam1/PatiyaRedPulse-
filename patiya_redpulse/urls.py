from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.contrib.auth.models import User
from accounts.models import Donor
from django.utils import timezone

# --- Master Fix Function: Solves profile and login issues at once ---
def master_fix_everything(request):
    try:
        all_users = User.objects.all()
        fixed_profiles = 0
        password_resets = 0
        
        for user in all_users:
            # 1. Profile Sync: Adds age and gender to avoid Database Integrity Errors
            if not hasattr(user, 'donor'):
                Donor.objects.create(
                    user=user,
                    full_name=user.username,
                    blood_group='O+', 
                    age=25,          # Default age to satisfy database constraints
                    gender='Male',    # Default gender to satisfy database constraints
                    mobile_number='01000000000',
                    district='Update Needed',
                    upazila='Update Needed',
                    is_active=False   # Set to False so they don't show as "Fake Donors"
                )
                fixed_profiles += 1
            
            # 2. Password Reset: Ensures everyone can log in with a known password
            user.set_password('Patiya123')
            user.save()
            password_resets += 1
            
        return HttpResponse(f"""
            <div style="text-align: center; margin-top: 50px; font-family: 'Segoe UI', sans-serif;">
                <h1 style="color: #27ae60;">🎉 Master Fix Successful!</h1>
                <p style="font-size: 1.1rem;">Profiles Linked: <b>{fixed_profiles}</b> | Passwords Reset: <b>{password_resets}</b></p>
                <div style="background: #fdf2f2; padding: 20px; border-radius: 10px; display: inline-block; border: 1px solid #fab1a0;">
                    <p><strong>New Login Information:</strong></p>
                    <p>Username: Their old username</p>
                    <p>Password: <span style="color: #d63031; font-weight: bold; font-size: 1.2rem;">Patiya123</span></p>
                </div>
                <p style="margin-top: 20px; color: #636e72;">Everyone can now log in. They must update their profiles to appear in the Donor List.</p>
                <a href="/accounts/login/" style="background: #e74c3c; color: white; padding: 12px 25px; text-decoration: none; border-radius: 5px; font-weight: bold;">Go to Login Page</a>
            </div>
        """)
    except Exception as e:
        return HttpResponse(f"<h2 style='color: red;'>Error: {e}</h2><p>Check if your model has other required fields.</p>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('final-master-fix/', master_fix_everything), # Visit this URL once to fix everything
    path('', include('blood_requests.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin-panel/', include('admin_panel.urls')),

    # Password Reset URLs
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]

# Static and Media Config
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
