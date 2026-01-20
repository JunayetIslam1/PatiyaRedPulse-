from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.contrib.auth.models import User
from accounts.models import Donor
from django.utils import timezone

# --- সব সমস্যার এক সমাধান ফাংশন ---
def master_fix(request):
    try:
        all_users = User.objects.all()
        fixed_profiles = 0
        password_resets = 0
        
        for user in all_users:
            # ১. প্রোফাইল ফিক্স (ফেক ডোনার হবে না)
            if not hasattr(user, 'donor'):
                Donor.objects.create(
                    user=user,
                    full_name=user.username,
                    blood_group='O+', 
                    mobile_number='01000000000',
                    district='Update Needed',
                    upazila='Update Needed',
                    is_active=False # লিস্টে দেখাবে না
                )
                fixed_profiles += 1
            
            # ২. পাসওয়ার্ড রিসেট (পুরনো ইউজারদের জন্য)
            # আপনি চাইলে শুধু নির্দিষ্ট ইউজারদের জন্য করতে পারেন, 
            # এখানে সবার জন্য একটি কমন পাসওয়ার্ড সেট হচ্ছে যাতে লগইন নিশ্চিত হয়।
            user.set_password('Patiya123')
            user.save()
            password_resets += 1
            
        return HttpResponse(f"""
            <div style="text-align: center; margin-top: 50px; font-family: sans-serif;">
                <h1 style="color: #2ecc71;">Master Fix Complete!</h1>
                <p>Profiles Created: {fixed_profiles}</p>
                <p>Passwords Reset: {password_resets}</p>
                <div style="background: #f8f9fa; padding: 20px; display: inline-block; border-radius: 10px; border: 1px solid #ddd;">
                    <p><strong>Login Info for Users:</strong></p>
                    <p>Username: Their old username</p>
                    <p>Password: <code style="font-size: 1.2rem;">Patiya123</code></p>
                </div>
                <br><br>
                <a href="/accounts/login/" style="background: #e74c3c; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Go to Login Page</a>
            </div>
        """)
    except Exception as e:
        return HttpResponse(f"Error: {e}")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('master-fix-now/', master_fix), # এই লিঙ্কে একবার ভিজিট করবেন
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
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
